from . import app
from . import session
from flask import render_template, request, redirect, url_for, flash, jsonify
from database_setup import User, Category, CategoryItem


@app.route('/catalog/<string:category_name>.json')
def category_items_json(category_name):
    items = session.query(CategoryItem).join(Category).filter(Category.name == category_name).all()
    return jsonify(CategoryItems=[i.serialize for i in items])


@app.route('/catalog/<string:category_name>/<string:category_item_title>.json')
def category_item_description_json(category_name, category_item_title):
    item = session.query(CategoryItem).join(Category).filter(Category.name == category_name,
                                                             CategoryItem.title == category_item_title).all()[0]
    return jsonify(CategoryItem=item.serialize)
