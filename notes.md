```
python manage.py runserver

django-admin startproject project_name (Dot dosen't create outer directory )
django-admin startapp app_name
after creating an app settings.py-> add your app into the INSTALLED_APPS list.
presence  of __init()__.py makes it a package

in the admin.py file we register all models we made..

apps.py Configuration file for the app (meta data)

models.py contains fields and behaviour about your app.

test.py Where you add tests for the app.

python manage.py createsuperuser
```



```python
{% tag %} 
{{variable}}
{{variable |filter}}

project_directory ->templates->app_name->HTML files
project_directory ->static ->app_name->CSS,BS files

Add function to render html files into app_directory/views.py.
Then Go to project_directory/urls.py
	Import include along with path
create urls.py in app_directory and import views

Add the following into settings.py in the project_directory


SETTINGS_PATH = os.path.dirname(os.path.dirname(__file__))

//Add under TEMPLATES//
'DIRS': [os.path.join(SETTINGS_PATH, 'templates'),]

STATICFILES_DIRS = (
os.path.join(BASE_DIR, "static"),
'/var/www/static/',
)


{%load static%}

change href="{%static 'todolist/styles.css'%}"

```

```python
Write functions in models and make migrations

dynamic content

views define our context varibale and add to to the render function
Add necessary for loops and if conditions.
```

```python
Create forms.py in app_directory
from django import forms

class class_name(forms.Form):

text= forms.CharField(max_length=45,required=True,
        widget=forms.TextInput(
            attrs={'id':'field','placeholder':'Type Here'}))

import forms to views
add form to context
import redirect,require_POST

```

