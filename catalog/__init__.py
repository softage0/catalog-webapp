import datetime
from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from sqlalchemy import create_engine, desc
from sqlalchemy.orm import sessionmaker
from database_setup import Base, User, Category, CategoryItem

app = Flask(__name__)

engine = create_engine('postgres://oiuhydyuipflby:wA2Dn17rl-Y_ckX6krEHMcHITG@ec2-54-83-29-133.compute-1.amazonaws.com:5432/d8quo2rmar6mro')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


# JSON endpoints
@app.route('/catalog/<string:category_name>.json')
def category_items_json(category_name):
    items = session.query(CategoryItem).join(Category).filter(Category.name == category_name).all()
    return jsonify(CategoryItems=[i.serialize for i in items])


@app.route('/catalog/<string:category_name>/<string:category_item_title>.json')
def category_item_description_json(category_name, category_item_title):
    item = session.query(CategoryItem).join(Category).filter(Category.name == category_name,
                                                             CategoryItem.title == category_item_title).all()[0]
    return jsonify(CategoryItem=item.serialize)


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
        # admin = session.query(User).one()
        item = CategoryItem(title=request.form['title'], description=request.form['description'],
                            category_id=request.form['category_id'], user=admin)
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


# if __name__ == '__main__':
app.secret_key = 'super_secret_key'
app.debug = True
# app.run(host='0.0.0.0', port=8000)
