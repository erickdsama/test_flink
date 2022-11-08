import os

PG_USER = os.getenv('PG_USER', '')
PG_DATABASE = os.getenv('PG_DATABASE', '')
PG_HOST = os.getenv('PG_HOST', '')
PG_PORT = os.getenv('PG_PORT', '')
PG_PASSWORD = os.getenv('PG_PASSWORD', '')

CORS_ORIGIN_WHITELIST = [
    'http://localhost:8080',
    'http://0.0.0.0:8080',
]

ALLOWED_HOSTS = [
    "test.petwarn.me"
]


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
