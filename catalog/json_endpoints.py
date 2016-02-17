from . import app
from . import session
from flask import jsonify
from database_setup import User, Category, CategoryItem


@app.route('/catalog/categories.json')
def categories_json():
    items = session.query(Category).all()
    return jsonify(CategoryItems=[i.serialize for i in items])


@app.route('/catalog/all_items.json')
def all_items_json():
    items = session.query(CategoryItem).all()
    return jsonify(CategoryItems=[i.serialize for i in items])


@app.route('/catalog/<string:category_name>.json')
def category_items_json(category_name):
    items = session.query(CategoryItem).join(Category).filter(Category.name == category_name).all()
    return jsonify(CategoryItems=[i.serialize for i in items])


@app.route('/catalog/<string:category_name>/<string:category_item_title>.json')
def category_item_description_json(category_name, category_item_title):
    item = session.query(CategoryItem).join(Category).filter(Category.name == category_name,
                                                             CategoryItem.title == category_item_title).all()[0]
    return jsonify(CategoryItem=item.serialize)


@app.route('/catalog/user.json')
def user_json():
    items = session.query(User).all()
    return jsonify(Users=[i.serialize for i in items])
