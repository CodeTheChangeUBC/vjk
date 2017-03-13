from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^home/', views.index, name='index'),
    url(r'^search/', views.index, name='index'),
    url(r'^email/', views.index, name='index'),
    url(r'^edit-entries/', views.index, name='index'),
    url(r'^add-entries/', views.index, name='index'),
    url(r'^delete-entries/', views.index, name='index'),
]