from .base import *

DEBUG = 'False'
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
        'NAME': 'topdown',
        'USER': 'root',
        'PASSWORD': 'zaverih99',
        'PORT': 3306,
        'HOST': 'localhost'
    }
}

STRIPE_PUBLIC_KEY='sk_test_51HaBStAJk6sbxMgtIvyp2IXOY66io7qXiVPHVHUxvk70ynmJe2kqqAVjmt5iNWP2wBekoO97xZybYpLxkZU2yX5g00zvB8Ubd4'
STRIPE_SECRET_KEY='sk_test_51HaBStAJk6sbxMgtIvyp2IXOY66io7qXiVPHVHUxvk70ynmJe2kqqAVjmt5iNWP2wBekoO97xZybYpLxkZU2yX5g00zvB8Ubd4'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = 'jhaverihussain@gmail.com'
EMAIL_HOST_PASSWORD = 'osoeiovwepnfontk'
ACCOUNT_EMAIL_VERIFICATION = 'none'