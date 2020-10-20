## Requirements

* Docker
* Docker Compose

## Initialisation

1. Clone project from github to local folder

2. Locate the folder with the command line and run the following commands

3. docker-compose run web python manage.py makemigrations

4. docker-compose run web python manage.py migrate

## Run the app

1. docker-compose up

## Navigating the app

1. For the root directory go to local host: http://0.0.0.0:8000/
2. To add a customer go to http://0.0.0.0:8000/customer/
3. To add a book http://0.0.0.0:8000/book/
4. To view books added over the last 7 days http://0.0.0.0:8000/book/last_week/
5. To view books added over the last 14 days http://0.0.0.0:8000/book/last_week/

'''
Better app structure I released too late:
1. The customer should extend the user model, allowing authentication - signup / login / logout
2. Views should then query books based on the user currently logged in.
3. Add a view that allows user to query for any time period.
'''

# UNIT TESTING

1. run docker-compose run web python manage.py test

# BDD testing

'''
Note this is not complete. I was not familiar with behave. I have setup a skeleton with TODOs.
'''

1. docker-compose run web behave  
