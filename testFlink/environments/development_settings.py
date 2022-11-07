import os

PG_USER = os.getenv('PG_USER', '')
PG_DATABASE = os.getenv('PG_DATABASE', '')
PG_HOST = os.getenv('PG_HOST', '')
PG_PORT = os.getenv('PG_PORT', '')
PG_PASSWORD = os.getenv('PG_PASSWORD', '')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': PG_DATABASE,
        'USER': PG_USER,
        'PASSWORD': PG_PASSWORD,
        'HOST': PG_HOST,
        'PORT': PG_PORT,
    }
}
