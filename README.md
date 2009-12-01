# django-exampleproject

A pre-configured Django 1.1 project that can be used as a starting point.
The following changes were made:

- Import settings_local.py in settings.py
- Sqlite3 database saved in project directory
- Static media in "media/" served by static.serve
- TEMPLATE_DIRS set to "templates/" directory
- E-mail settings configured for Python DebuggingServer
- GZipMiddleware installed
- example base.html template with basic HTML4.01 skeleton
- example 404.html/500.html error page templates
- custom error 500 handler with MEDIA_URL in context
- contrib.admin installed
- initial_data.json fixture with superuser
    - User: admin
    - Password: admin
- django-debug-toolbar configured (run `pip install django-debug-toolbar`)
- change ADMIN_MEDIA_PREFIX to "/media/admin/"
- CACHE_BACKEND set to locmem

If you want to rename the project, remember to change the ROOT_URLCONF
variable in settings.py to the new project name.
