from django.conf.urls import url,include
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from . import views


app_name = 'login'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login_user/$', views.login_user, name='login_user'),
    url(r'^logout_user/$', views.logout_user, name='logout_user'),
    url(r'^register/$', views.register, name='register'),
    url(r'^addComplaint/$', views.addComplaint, name='addComplaint'),
    url(r'^main/$', views.main, name='main'),
]