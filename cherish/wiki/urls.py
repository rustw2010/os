from django.conf.urls import url
from wiki import views


urlpatterns = [
 url(r'^$', views.wiki, name='wiki'),
]