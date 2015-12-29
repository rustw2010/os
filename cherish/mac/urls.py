from django.conf.urls import url
from mac import views


urlpatterns = [
 url(r'^$', views.mac, name='mac'),
 
]