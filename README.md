# endear
Minerva Dating App on Heroku

```
python manage.py collectstatic
python manage.py makemigrations
python manage.py migrate


python manage.py runserver
```

```
endear
├─ 📁endearapp
│  ├─ 📁migrations
│  │  ├─ 📄0001_initial.py
│  │  └─ 📄__init__.py
│  ├─ 📄__init__.py
│  ├─ 📄admin.py
│  ├─ 📄apps.py
│  ├─ 📄backends.py
│  ├─ 📄middleware.py
│  ├─ 📄models.py
│  ├─ 📄tests.py
│  ├─ 📄urls.py
│  └─ 📄views.py
├─ 📁endearproject
│  ├─ 📄__init__.py
│  ├─ 📄asgi.py
│  ├─ 📄settings.py
│  ├─ 📄urls.py
│  └─ 📄wsgi.py
├─ 📁templates
│  ├─ 📁static
│  │  ├─ 📁css
│  │  │  └─ 📄index.css
│  │  ├─ 📁img
│  │  │  ├─ 📄avatar.jpg
│  │  │  ├─ 📄endear_logo.ico
│  │  │  ├─ 📄endear_logo.png
│  │  │  └─ 📄endear_logo_white.png
│  │  ├─ 📁js
│  │  │  └─ 📄index.js
│  │  └─ 📄people.json
│  ├─ 📄dashboard.html
│  ├─ 📄error.html
│  ├─ 📄index.html
│  ├─ 📄solution.html
│  └─ 📄war.html
├─ 📁venv
├─ 📄.gitignore
├─ 📄LICENSE
├─ 📄Procfile
├─ 📄README.md
├─ 📄manage.py
├─ 📄requirements.txt
└─ 📄vercel.json
```