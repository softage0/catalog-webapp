import datetime

from sqlalchemy import desc
from flask import render_template, request, redirect, url_for, flash
from flask import session as login_session

from database_setup import Category, CategoryItem
from . import app
from . import session
from . import restriction


@app.route('/')
def catalog_main():
    """ Main page of Item Catalog """
    categories = session.query(Category).all()
    items = session.query(CategoryItem).order_by(desc(CategoryItem.modified_date)).limit(10).all()
    return render_template('catalog_main.html', categories=categories, items=items, title='Latest Items', main=True)


@app.route('/catalog/<string:category_name>')
def category_items(category_name):
    """
    Item list of each category
    Args:
        category_name: category name of the item list
    """
    categories = session.query(Category).all()
    items = session.query(CategoryItem).join(Category).filter(Category.name == category_name).all()
    title = category_name + ' Items (' + str(len(items)) + ' items)'
    return render_template('catalog_main.html', categories=categories, items=items,
                           title=title, category_name=category_name)


@app.route('/catalog/<string:category_name>/<string:category_item_title>')
def category_item_description(category_name, category_item_title):
    """
    Description of each category item
    Args:
        category_name: name of category
        category_item_title: name of item
    """
    categories = session.query(Category).all()
    item = session.query(CategoryItem).join(Category).filter(Category.name == category_name,
                                                             CategoryItem.title == category_item_title).all()[0]
    return render_template('category_item.html', item=item, category_name=category_name, categories=categories)


@app.route('/catalog/new', methods=['GET', 'POST'])
@restriction.login_required
def new_category_item():
    """ Page to create new item - login member only """
    if request.method == 'POST':
        item = CategoryItem(title=request.form['title'], description=request.form['description'],
                            category_id=request.form['category_id'], user_id=login_session['user_id'])
        session.add(item)
        session.commit()
        flash(item.title + " added!")
        return redirect(url_for('catalog_main'))
    else:
        categories = session.query(Category).all()
        return render_template('category_item_new.html', categories=categories)


@app.route('/catalog/<string:category_name>/<string:category_item_title>/edit', methods=['GET', 'POST'])
@restriction.owner_required
def edit_category_item(category_name, category_item_title, item):
    """
    Page to edit the item - owner who created the item only
    Args:
        category_name: name of category
        category_item_title: name of item
        item: item info responded from owner_required decorator
    """
    if not item:
        item = session.query(CategoryItem).join(Category) \
            .filter(Category.name == category_name,
                    CategoryItem.title == category_item_title).all()[0]
    if request.method == 'POST':
        item.modified_date = datetime.datetime.now()
        item.title = request.form['title']
        item.description = request.form['description']
        item.category_id = request.form['category_id']
        session.commit()
        flash(item.title + " modified!")
        return redirect(url_for('catalog_main'))
    else:
        categories = session.query(Category).all()
        return render_template('category_item_edit.html', item=item, categories=categories, category_name=category_name)


@app.route('/catalog/<string:category_name>/<string:category_item_title>/delete', methods=['GET', 'POST'])
@restriction.owner_required
def delete_category_item(category_name, category_item_title, item):
    """
    Page to delete the item - owner who created the item only
    Args:
        category_name: name of category
        category_item_title: name of item
        item: item info responded from owner_required decorator
    """
    if request.method == 'POST':
        if not item:
            item = session.query(CategoryItem).join(Category).filter(Category.name == category_name,
                                                                     CategoryItem.title == category_item_title).all()[0]
        session.delete(item)
        session.commit()
        flash(item.title + " deleted!")
        return redirect(url_for('catalog_main'))
    else:
        categories = session.query(Category).all()
        return render_template('category_item_delete.html', category_name=category_name,
                               category_item_title=category_item_title, categories=categories)
