import os
from form.settings import *
import dj_database_url

ALLOWED_HOSTS = ['frontendmentor-intro-component.herokuapp.com']

CSRF_TRUSTED_ORIGINS = ['https://frontendmentor-intro-component.herokuapp.com']

SECRET_KEY = os.environ.get('SECRET_KEY')

DATABASES['default'] = dj_database_url.config(default=os.environ.get('DATABASE_URL'))

DEBUG = os.environ.get('DEBUG', None) == 'true'

# Email settings for production. Uses Gmail free account. Will not be possible after 2022-05-30.
# Will be set up to another protocol/provider will be needed - mailchimp or another. Use some API 
# from this solutions and  use the API keys instead of username/password from gmail account. 
# For using send_mail function it will need the change of the backend for emails sending,
# the best way seems to be write smth own. It will separate the command of sending of the emails 
# from the process of send/receive emails itself. 
EMAIL_HOST = os.environ.get('EMAIL_HOST')
EMAIL_PORT = int(os.environ.get('EMAIL_PORT'))
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')
EMAIL_USE_TLS = True