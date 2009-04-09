django-exampleproject serves me as a solid basis to start from when initiating 
a new Django project. It integrates stuff that I use on every project 
and thus saves me some time and eliminates boring repetitive tasks.

- Import `settings_local.py` in `settings.py`
- `sqlite3` database saved in project directory
- Static media in "static_media/" served by `static.serve` when `DEBUG = True`
- `TEMPLATE_DIRS` set to "templates/" directory in project directory.
- Email settings configured for Python DebuggingServer on port 1025 (see `settings.py` for information on how to start the server)
- GZipMiddleware installed
- base.html template with basic HTML4.01 skeleton
- 404.html/500.html error page templates
- custom error 500 handler with MEDIA_URL in context
- django.contrib.admin installed
- initial_data.json fixture with superuser for admin
    - User: admin
    - Password: admin
- django-debug-toolbar installed
- django-command-extensions installed
