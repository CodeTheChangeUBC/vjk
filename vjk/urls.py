from django.conf.urls import url

from . import views

app_name = 'vjk'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^search/', views.search, name='search'),
    # url(r'^delete-entries/', views.delete, name='delete')
]
