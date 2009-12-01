# Run `python -m smtpd -n -c DebuggingServer localhost:1025` to start a 
# local email server on port 1025
EMAIL_HOST = 'localhost'
EMAIL_PORT = 1025

# django-debug-toolbar
INTERNAL_IPS = ('127.0.0.1',)
LOCAL_INSTALLED_APPS = (
    'debug_toolbar',
)
LOCAL_MIDDLEWARE_CLASSES = (
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)
