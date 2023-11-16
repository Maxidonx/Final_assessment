# This is a Project for Littlelemon Restaurant.

### To get started, do the following
- clone the repository 
```bash
https://github.com/Maxidonx/Final_assessment.git
```
- install the following:
    -virtual environment
    ```bash
     python -m venv venv 
     venv/Scripts/activate
    ```
    - Install Django
    ```bash
    pip inatall django
    ```
    - install Rest Framework
    ```bash
    pip install djangorestframework
    ```
    - install coreshearders
    ```bash
    pip install django-cors-headers
    ```
    - make migrations
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```
    - run the server
    ```bash
    python manage.py runserver
    ```
## Testing the end points
** /api/register/ **

- ** DESCRIPTION: ** To register new users
- ** METHOD: **  POST

** /api/get_user/<int:user_id>/ **

- ** DESCRIPTION: ** To get users
- ** METHOD: **  GET

** /api/update_user/<int:user_id>/ **

- ** DESCRIPTION: ** To Update users
- ** METHOD: ** PUT

** /api/delete_user/<int:user_id>/ **

- ** DESCRIPTION: ** To delete users
- ** METHOD: **  DELETE

** localhost **

- ** DESCRIPTION: ** Home page
- ** METHOD: **  GET

** /menu **

- ** DESCRIPTION: ** desplay menu
- ** METHOD: **  get

** /book **

- ** DESCRIPTION: ** To make booking
- ** METHOD: **  POST

** /reservations/ **

- ** DESCRIPTION: ** To make reservations
- ** METHOD: **  POST




