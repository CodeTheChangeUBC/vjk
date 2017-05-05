from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'', views.home, name='home'),
    url(r'^search/', views.search, name='search'),
    url(r'^email/', views.email, name='email'),
    url(r'^edit-entries/', views.edit, name='edit'),
    url(r'^add-entries/', views.add, name='add'),
    url(r'^delete-entries/', views.delete, name='delete'),
]
