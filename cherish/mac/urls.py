from django.conf.urls import url
from mac import views


urlpatterns = [
 url(r'^$', views.mac, name='mac'),
 url(r'^category/(?P<categoryID>[0-9]+)/$', views.category, name='category'),
 
]