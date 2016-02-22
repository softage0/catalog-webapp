import json
import dicttoxml
from flask import jsonify, Response

from database_setup import User, Category, CategoryItem

from . import app
from . import session


# json endpoints
@app.route('/catalog/categories.json')
def categories_json():
    """ Category list """
    items = session.query(Category).all()
    return jsonify(CategoryItems=[i.serialize for i in items])


@app.route('/catalog/all_items.json')
def all_items_json():
    """ All item list """
    items = session.query(CategoryItem).all()
    return jsonify(CategoryItems=[i.serialize for i in items])


@app.route('/catalog/<string:category_name>.json')
def category_items_json(category_name):
    """
    Item list of each category
    Args:
        category_name: category name of the item list
    """
    items = session.query(CategoryItem).join(Category).filter(Category.name == category_name).all()
    return jsonify(CategoryItems=[i.serialize for i in items])


@app.route('/catalog/<string:category_name>/<string:category_item_title>.json')
def category_item_description_json(category_name, category_item_title):
    """
    Description of each category item
    Args:
        category_name: name of category
        category_item_title: name of item
    """
    item = session.query(CategoryItem).join(Category).filter(Category.name == category_name,
                                                             CategoryItem.title == category_item_title).all()[0]
    return jsonify(CategoryItem=item.serialize)


@app.route('/catalog/user.json')
def user_json():
    """ All user list """
    items = session.query(User).all()
    return jsonify(Users=[i.serialize for i in items])


# xml endpoints
def return_xml(json_response):
    """
    Convert json to xml
    Args:
        json_response: json response for web rendering

    Returns: converted xml return

    """
    return Response(dicttoxml.dicttoxml(json.loads(json_response.data)), mimetype='text/xml')


@app.route('/catalog/categories.xml')
def categories_xml():
    """ Category list """
    return return_xml(categories_json())


@app.route('/catalog/all_items.xml')
def all_items_xml():
    """ All item list """
    return return_xml(all_items_json())


@app.route('/catalog/<string:category_name>.xml')
def category_items_xml(category_name):
    """
    Item list of each category
    Args:
        category_name: category name of the item list
    """
    return return_xml(category_items_json(category_name))


@app.route('/catalog/<string:category_name>/<string:category_item_title>.xml')
def category_item_description_xml(category_name, category_item_title):
    """
    Description of each category item
    Args:
        category_name: name of category
        category_item_title: name of item
    """
    return return_xml(category_item_description_json(category_name, category_item_title))


@app.route('/catalog/user.xml')
def user_xml():
    """ All user list """
    return return_xml(user_json())
