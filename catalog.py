from flask import Flask, render_template, request, redirect, jsonify, url_for, flash
from sqlalchemy import create_engine, asc
from sqlalchemy.orm import sessionmaker
from database_setup import Base, User, Category, Item
from flask import session as login_session
import random
import string

# IMPORTS FOR THIS STEP
from oauth2client.client import flow_from_clientsecrets
from oauth2client.client import FlowExchangeError
import httplib2
import json
from flask import make_response
import requests


app = Flask(__name__)

engine = create_engine('sqlite:///catalog.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


@app.route('/')
@app.route('/categories/')
def showCatalog():
    categories = session.query(Category).all()

    #creator = getUserInfo(restaurant.user_id)
    items = session.query(Item).all()

    #if 'username' not in login_session or creator.id != login_session['user_id']:
     #   return render_template('publicmenu.html', restaurant=restaurant, items=items)
    #else:
    return render_template('index.html', categories=categories, items=items)


@app.route('/categories/<int:category_id>/')
def showCategory(category_id):
    categories = session.query(Category).all()

    #creator = getUserInfo(restaurant.user_id)
    items = session.query(Item).filter_by(category_id=category_id).all()

    #if 'username' not in login_session or creator.id != login_session['user_id']:
     #   return render_template('publicmenu.html', restaurant=restaurant, items=items)
    #else:
    return render_template('index.html', categories=categories, items=items, category_id=category_id)


@app.route('/categories/<int:category_id>/items/<int:item_id>', methods=['GET'])
def showItem(category_id, item_id):
    categories = session.query(Category).all()

    #creator = getUserInfo(restaurant.user_id)
    item = session.query(Item).filter_by(id=item_id).one()

    #if 'username' not in login_session or creator.id != login_session['user_id']:
     #   return render_template('publicmenu.html', restaurant=restaurant, items=items)
    #else:
    return render_template('showItem.html', categories=categories, item=item, category_id=category_id)

@app.route('/categories/<int:category_id>/items/new', methods=['GET', 'POST'])
def newItem(category_id):
    #if 'username' not in login_session:
     #   return redirect('/login')

    if request.method == 'POST':
        newItem = Item(category_id=category_id,
                       name=request.form['name'],
                       description=request.form['description'])
        session.add(newItem)
        session.commit()
        #flash("new restaurant created")
        return redirect(url_for('showCategory',category_id = category_id))
    else:
        return render_template('newItem.html', category_id=category_id)

@app.route('/categories/<int:category_id>/items/<int:item_id>/edit', methods=['GET', 'POST'])
def editItem(category_id,item_id):
    #if 'username' not in login_session:
     #   return redirect('/login')
    edited_item = session.query(Item).filter_by(id=item_id).one()

    if request.method == 'POST':

        if request.form['name']:
            edited_item.name= request.form['name']
        if request.form['description']:
            edited_item.name = request.form['description']
        session.add(newItem)
        session.commit()

        #flash("new restaurant edited")
        return redirect(url_for('showCategory',category_id = category_id))
    else:
        return render_template('editItem.html', category_id=category_id, item=edited_item)

@app.route('/categories/<int:category_id>/items/<int:item_id>/delete', methods=['GET', 'POST'])
def deleteItem(category_id, item_id):
    #if 'username' not in login_session:
     #   return redirect('/login')
    categories = session.query(Category).all()
    item2Delete = session.query(Item).filter_by(id=item_id).one()

    if request.method == 'POST':

        session.delete(item2Delete)
        session.commit()
        #flash("new restaurant created")
        return redirect(url_for('showCategory',category_id=category_id, categories=categories))
    else:
        return render_template('deleteItem.html',category_id=category_id, item=item2Delete)


if __name__ == '__main__':
    #app.secret_key= 'super_secret_key'
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
