from .base import *

DEBUG = True
ALLOWED_HOSTS = ['127.0.0.1']

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'}
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'hulidb2',
        'USER': 'root',
        'PASSWORD': 'rocktofakie',
        'PORT': 3306,
        'HOST': 'localhost'
    }
}

STRIPE_PUBLIC_KEY='sk_test_51HaBStAJk6sbxMgtIvyp2IXOY66io7qXiVPHVHUxvk70ynmJe2kqqAVjmt5iNWP2wBekoO97xZybYpLxkZU2yX5g00zvB8Ubd4'
STRIPE_SECRET_KEY='sk_test_51HaBStAJk6sbxMgtIvyp2IXOY66io7qXiVPHVHUxvk70ynmJe2kqqAVjmt5iNWP2wBekoO97xZybYpLxkZU2yX5g00zvB8Ubd4'
ACCOUNT_EMAIL_VERIFICATION = 'none'