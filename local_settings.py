# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-2=+*e#d)hp=sjh1)&&bod0ycwu0l+)*+z#vgz)8$-+yh2opyam'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'finesauces',
        'USER': 'postgres',
        'PASSWORD': 'qwe',
        'HOST': 'localhost'
    }
}
print(1)
