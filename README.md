# Django-demo-app

This is a simple Django web application called **Django-demo-app**.

## Features

- Welcome homepage for new Data Scientists at Blackcoffer
- Uses Django 5.2
- Bootstrap 5 for styling

## Project Structure

```
mysite/
    manage.py
    db.sqlite3
    hello/
        admin.py
        apps.py
        models.py
        tests.py
        urls.py
        views.py
        templates/
            hello/
                home.html
    mysite/
        __init__.py
        asgi.py
        settings.py
        urls.py
        wsgi.py
```

## Getting Started

1. **Install dependencies**  
   Make sure you have Python and Django installed:
   ```sh
   pip install django
   ```

2. **Run migrations**
   ```sh
   python manage.py migrate
   ```

3. **Start the development server**
   ```sh
   python manage.py runserver
   ```

4. **Visit the app**  
   Open [http://127.0.0.1:8000/](http://127.0.0.1:8000/) in your browser.

## App Details

- The homepage is rendered by the [`home`](mysite/hello/views.py) view in the [`hello`](mysite/hello/) app.
- The template used is [`home.html`](mysite/hello/templates/hello/home.html).
- The joining date is passed as context from the view.

## License

This project is for demonstration.