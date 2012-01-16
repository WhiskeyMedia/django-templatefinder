django-templatefinder
=====================

Django templatefinder is a very simple template loader fo Django 1.3. It
extends the `cached template loader
<https://docs.djangoproject.com/en/1.3/ref/templates/api/#loader-types>`_ from
Django. During initialization it goes throught all directories containing
templates and composes a list of available templates. When a template is then
requested and is not in this set, `TemplateDoesNotExist` is raised immediately.

Setup
-----

Put `'templatefinder.Loader'` into `TEMPLATE_LOADERS` in your `settings.py` as
you would 'django.template.loaders.cached.Loader'. For example::

    TEMPLATE_LOADERS = ( 
        ('templatefinder.Loader', (
            'django.template.loaders.filesystem.Loader',
            'django.template.loaders.app_directories.Loader',
        )), 
    )   

