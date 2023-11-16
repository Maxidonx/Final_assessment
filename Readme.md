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
** http://127.0.0.1/api/register/ **

- ** DESCRIPTION: ** To register new users
- ** METHOD: **  POST

** http://127.0.0.1/api/get_user/<int:user_id>/ **

- ** DESCRIPTION: ** To get users
- ** METHOD: **  GET

** http://127.0.0.1/api/update_user/<int:user_id>/ **

- ** DESCRIPTION: ** To Update users
- ** METHOD: ** PUT

** http://127.0.0.1/api/delete_user/<int:user_id>/ **

- ** DESCRIPTION: ** To delete users
- ** METHOD: **  DELETE

** http://127.0.0.1/ **

- ** DESCRIPTION: ** Home page
- ** METHOD: **  GET

** http://127.0.0.1/menu **

- ** DESCRIPTION: ** desplay menu
- ** METHOD: **  get

** localhost:8000/book **

- ** DESCRIPTION: ** To make booking
- ** METHOD: **  POST

** http://127.0.0.1/reservations/ **

- ** DESCRIPTION: ** To make reservations
- ** METHOD: **  POST




