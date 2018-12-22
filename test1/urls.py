from django.conf.urls import url
from django.urls import path

from test1 import views

urlpatterns = [
    url(r'^$', views.googleCap, name='googleCap'),
    url(r'^googleconfirm$', views.googleconfirm, name='googleconfirm'),
]


