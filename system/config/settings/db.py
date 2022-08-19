from .base import BASE_DIR, get_secret_env


SQLITE3 = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR.child("config", get_secret_env("DB_LOCAL")),
    }
}
