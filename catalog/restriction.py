from functools import wraps

from flask import request, redirect, url_for, flash
from flask import session as login_session

from database_setup import Category, CategoryItem
from . import session


def login_required(f):
    """
    Login status check for function 'f'
    Args:
        f: function that login status needs to be checked
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'username' in login_session:
            return f(*args, **kwargs)
        else:
            flash("You need to login first")
            return redirect(url_for('show_login', next=request.url))
    return decorated_function


def owner_required(f):
    """
    Item owner check for function 'f'
    Args:
        f: function that item owner needs to be checked
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        item = session.query(CategoryItem).join(Category)\
            .filter(Category.name == kwargs['category_name'],
                    CategoryItem.title == kwargs['category_item_title']).all()[0]
        if 'username' in login_session and item.user_id == login_session['user_id']:
            kwargs['item'] = item
            return f(*args, **kwargs)
        else:
            flash("You are not allowed to access there")
            return redirect(url_for('catalog_main'))
    return decorated_function
