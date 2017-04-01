# create new

from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^testapp/$', 'testapp.views.main'),
)

(venv)ubuntu@www:~/venv/testproject$ vi testproject/settings.py
# add testapp like follows

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'testapp',

) 
