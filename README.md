# Project: Item Catalog
# CodeName: Pycatalog

## Description
    This project provides a list of items within a variety of categories as well as 
    provide a user registration and authentication system. 
    Registered users will have the ability to post, edit and delete their own items.

## Understand the purpose of the main files
 * database_setup.sql  - this file is used to set up your database schema (the table representation of your data structure).
 * lots_of_items.py - This file is used to set up fixture data in order to render some new information in the webapp
 * catalog.py - this is the main file where all the code had been implemented. Included the webserver implementation that runs on
    localhost:5000
 * client_secrets.json - In order to run the google authentication services we need this file, with the google information that we get when we
    create the OAuth 2.0 client ID for this webapp for more info visit: https://support.google.com/cloud/answer/6158857
 

## Running the project!
 * Prerequisities: python2.7 and python-pip in order to install libraries from python
    * Python libraries
        - python-flask 
        - python-sqlalchemy
        - oauth2client
        - requests
        - httplib2
        - flask-httpauth
        
 * In order to create the schema you need to:
 	* 1- run this command in the terminal
 		$ python database_setup.py
 	* 2- once created the schema you need to run this command, in order to add some data into the database 
 		$ python lots_of_items.py
 * To run the webserver you need to run this command from the terminal:
    - $ python catalog.py
    - this will fire up the webserver, after this you should access this URL from a webbrowser
        http://localhost:5000/


## JSON APIS URLS

    ### GET ALL THE CATEGORIES
        - http://localhost:5000/api/v1/categories
    ### GET THE DETAILS INFORMATION OF A CATEGORY
        - http://localhost:5000/api/v1/categories/[CATEGORY_ID]
    ### GET ALL THE ITEMS
        - http://localhost:5000/api/v1/items
    ### GET THE DETAILS INFORMATION OF A ITEM
        - http://localhost:5000/api/v1/items/[ITEM_ID]