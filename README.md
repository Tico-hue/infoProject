# Kakuaa for Entrepeneurs
## infoProject.

It is a webb app mainly directed to starting entrepeneurs that want to extend their reach, visibility to pontential clients and engagement.

Its purpose is to boost these businesses exposure allowing the user to personalize their profile and showcase their products or services.

We aim to provide a space for opportunity to local entrepeneurs to help kickstart their business. 

## Features
##### User Registration 
##### User authentication
##### Profile customisation
##### Catalog CRUD allowing images
##### Profile search and filtering 




## Technologies used
#### Django 
#### Ajax
#### SqlServer
#### Bootstrap



## Home Page Screenshot
![](screenshots/homepage.jpg? "Home Page")

## Overview video
##### its in spanish but it shows the web 
[![infoProject](https://img.youtube.com/vi/xL6QrUc2ShQ/3.jpg)](https://www.youtube.com/watch?v=xL6QrUc2ShQ&feature=youtu.be​)

## Installation

Place yourself in 
```console
infoProject\requiremnts
``` 
and run in your console (You can use virtualenv) 
```console
pip intall -r requirements.txt
```

After that, you have to create a DB called 'ProjectInfo' in SQLServer
or if you want to use another DB you must change it in 
```console
\infoProject\infoProject\infoProject\settings\local.py
```
```json 
DATABASES = {
    'default': {
        'ENGINE': 'sql_server.pyodbc',
        'NAME': 'ProjectInfo',
        'Trusted_Connection':'yes',
        'HOST':'localhost\SQLEXPRESS',
        'OPTIONS':{
            'driver':'SQL Server Native Client 11.0'
        },
    },
 ```
Then, place yourself in infoProject\infoProject\infoProject and run 
```console
python manage.py makemigrations 
python manage.py migrate
python manage.py runserver
```
Now you can just open it in your browser
```console
localhost:8000 
```
