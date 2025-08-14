# Django-demo-app

A simple Django web application to welcome new Data Scientists to Blackcoffer.

---

## Table of Contents

- [Project Overview](#project-overview)
- [Folder Structure](#folder-structure)
- [How It Works](#how-it-works)
- [Setup Instructions](#setup-instructions)
- [Main Files Explained](#main-files-explained)
- [Customization](#customization)
- [License](#license)

---

## Project Overview

This app displays a Bootstrap-styled homepage with a welcome message and joining date for new Data Scientists. It demonstrates basic Django concepts: views, templates, URL routing, and context passing.

---

## Folder Structure

```
mysite/
│   db.sqlite3
│   manage.py
│
├── hello/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   ├── views.py
│   ├── migrations/
│   │   └── __init__.py
│   └── templates/
│       └── hello/
│           └── home.html
│
└── mysite/
    ├── __init__.py
    ├── asgi.py
    ├── settings.py
    ├── urls.py
    └── wsgi.py
```

---

## How It Works

1. **URL Routing**  
   - The main project `urls.py` includes the `hello` app's URLs.
   - The `hello/urls.py` maps the root URL (`/`) to the `home` view.

2. **View Logic**  
   - The `home` view (in `hello/views.py`) renders the `home.html` template.
   - It passes a context variable `joining_date` to the template.

3. **Template Rendering**  
   - The template (`hello/templates/hello/home.html`) uses Bootstrap for styling.
   - It displays a welcome message and the joining date using `{{ joining_date }}`.

---

## Setup Instructions

1. **Install Django**
   ```sh
   pip install django
   ```

2. **Run Migrations**
   ```sh
   python manage.py migrate
   ```

3. **Start the Server**
   ```sh
   python manage.py runserver
   ```

4. **Access the App**  
   Open [http://127.0.0.1:8000/](http://127.0.0.1:8000/) in your browser.

---

## Main Files Explained

### 1. `mysite/urls.py`
```python
urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("hello.urls")),
]
```
- Includes the `hello` app's URLs at the root.

### 2. `hello/urls.py`
```python
urlpatterns = [
    path("", views.home, name="home"),
]
```
- Maps the root URL to the `home` view.

### 3. `hello/views.py`
```python
from django.shortcuts import render
from datetime import date

def home(request):
    context = {"joining_date": date.today().strftime("%B %d, %Y")}
    return render(request, "hello/home.html", context)
```
- Renders the homepage and passes the current date as `joining_date`.

### 4. `hello/templates/hello/home.html`
- Uses Bootstrap for styling.
- Displays a welcome message and the joining date.

---

## Customization

- **Change Welcome Text:**  
  Edit `home.html` to update the message.
- **Change Joining Date:**  
  Modify the logic in `views.py` to pass a different date or user-specific info.

---
