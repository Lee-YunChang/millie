
from millie.settings.env import ENV

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': ENV.str('MILLIE_DB_DEFAULT_NAME', 'millie_db'),
        'USER': ENV.str('DB_USER', 'test'),
        'PASSWORD': ENV.str('DB_PASSWORD', '1q2w3e!@#'),
        'HOST': ENV.str('DB_HOST', 'localhost'),
        'PORT': ENV.str('DB_PORT', '3306'),
        'OPTIONS': {
            'charset': 'utf8mb4',
        }
    }
}

