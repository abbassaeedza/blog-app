# BLOGGING APP (mainly backend)

solely for learning purposes

## Technologies Used:

-   Django Framework
-   Bootstrap (for shitty frontend)

### Concepts learned:

-   Setting up django project
-   Views (Custom and Built-in classes)
-   Customizing Forms
-   Models
-   Template

## How to host (locally)

Navigate to the project directory, then

1. Make virtual environment `python -m venv .venv`
2. Activate virtual env
    ```
    Linux: source .venv/Script/activate
    Windows: .venv\Script\activate.bat
    ```
3. Install dependencies `pip install -r requirements.txt`
4. Set **EMAIL_HOST_USER** and **EMAIL_HOST_PASSWORD**
5. make superuser(admin) `python manage.py createsuperuser`
6. run migrations:
    ```
    python manage.py makemigrations
    python manage.py migrate
    ```
7. run server `python manage.py runserver`

## Pages

Home Page
![Main Page](./screenshots/image.png)

User Page
![User Page](./screenshots/image1.png)

## Credits

-   Corey Schafer: [Youtube Channel](https://www.youtube.com/@coreyms/)
