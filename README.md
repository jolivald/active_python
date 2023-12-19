# python code

[source](https://docs.djangoproject.com/en/5.0/howto/windows/)


## upgrade pip
```sh
python.exe -m pip install --upgrade pip
```


## create a virtual env in windows

```sh
python -m venv my_env_name
cd my_env_name
./Script/ativate.bat
```

Before working on a project it needs to by activated !


## install django

```sh
python -m pip install Django
```


## create project
```sh
django-admin startproject my_project
cd my_project
```

## run dev server
```sh
python manage.py runserver
```

## create application
```sh
python manage.py startapp my_app
```

## create database migrations

If db is already implemented [look here](https://djangoadventures.com/how-to-integrate-django-with-existing-database/)  
Generate models from database and initialise django with this commands:  

```sh
python3 manage.py inspectdb > generated_models.py
python3 manage.py makemigrations
manage.py migrate --fake-initial
```

Else configure database credentials in *my_project/my_project/settings.py*  
Then run migration script:  

```sh
python manage.py migrate
```