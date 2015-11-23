from .base import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'chembiohub_db', # Or path to database file if using sqlite3.
        'USER': 'chembiohub', # Not used with sqlite3.
        'PASSWORD': '', # Not used witis oracle
        'HOST': '/home/chembiohub/postgressocket/.s.PGSQL.5432', # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '', # Set to empty string for default. Not used with sqlite3.
    },
}


CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/1",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}



SESSION_ENGINE = "django.contrib.sessions.backends.cache"
SESSION_CACHE_ALIAS = "default"

RQ_QUEUES = {
    'default': {
        'USE_REDIS_CACHE': 'default',
    },
}