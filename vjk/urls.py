from django.conf.urls import url

from . import views

app_name = 'vjk'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^student-intake', views.student_form, name='studentform'),
    url(r'^success', views.success, name='success')
]
