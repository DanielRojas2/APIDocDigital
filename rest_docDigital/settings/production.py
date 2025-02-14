import dj_database_url

from .base import *
from dotenv import load_dotenv

load_dotenv()

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.getenv('DEBUG')=='True'

ALLOWED_HOSTS = ['localhost']

CSRF_TRUSTED_ORIGINS = ['http://']


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': dj_database_url.config(default=os.getenv('DB_URL'))
}