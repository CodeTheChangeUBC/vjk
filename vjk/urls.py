from django.conf.urls import url

from . import views

app_name = 'vjk'
urlpatterns = [
    url(r'^$', views.search, name='search'),
]
