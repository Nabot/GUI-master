# log/urls.py
from django.conf.urls import url
from . import views

# We are adding a URL called /home
urlpatterns = [
    url(r'^$', views.home, name='home'),
url(r'^nata', views.nata, name='nata'),
url(r'^temp', views.temp, name='temp'),

]