from django.conf.urls import url
from windows import views


urlpatterns = [
 url(r'^$', views.windows, name='windows'),
]