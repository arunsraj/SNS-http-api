
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include
from views import *
# from views import dput

admin.autodiscover()
urlpatterns = [url(r'^api/', dput, name='dput'),
                      ]