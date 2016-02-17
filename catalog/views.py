import datetime

from sqlalchemy import desc
from flask import render_template, request, redirect, url_for, flash
from flask import session as login_session

from database_setup import Category, CategoryItem
from . import app
from . import session


@app.route('/')
def catalog_main():
    categories = session.query(Category).all()
    items = session.query(CategoryItem).order_by(desc(CategoryItem.modified_date)).limit(10).all()
    return render_template('catalog_main.html', categories=categories, items=items, title='Lastest Items', main=True)


@app.route('/catalog/<string:category_name>')
def category_items(category_name):
    categories = session.query(Category).all()
    items = session.query(CategoryItem).join(Category).filter(Category.name == category_name).all()
    title = category_name + ' Items (' + str(len(items)) + ' items)'
    return render_template('catalog_main.html', categories=categories, items=items, title=title)


@app.route('/catalog/<string:category_name>/<string:category_item_title>')
def category_item_description(category_name, category_item_title):
    item = session.query(CategoryItem).join(Category).filter(Category.name == category_name,
                                                             CategoryItem.title == category_item_title).all()[0]
    return render_template('category_item.html', item=item, category_name=category_name)


@app.route('/catalog/new', methods=['GET', 'POST'])
def new_category_item():
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
def edit_category_item(category_name, category_item_title):
    item = session.query(CategoryItem).join(Category).filter(Category.name == category_name,
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
def delete_category_item(category_name, category_item_title):
    if request.method == 'POST':
        item = session.query(CategoryItem).join(Category).filter(Category.name == category_name,
                                                                 CategoryItem.title == category_item_title).all()[0]
        session.delete(item)
        session.commit()
        flash(item.title + " deleted!")
        return redirect(url_for('catalog_main'))
    else:
        return render_template('category_item_delete.html', category_name=category_name,
                               category_item_title=category_item_title)
