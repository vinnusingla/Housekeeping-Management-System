from django.conf.urls import url,include
from . import views


app_name = 'login'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login_user/$', views.login_user, name='login_user'),
    url(r'^logout_user/$', views.logout_user, name='logout_user'),
    url(r'^register/$', views.register, name='register'),
    url(r'^addComplaint/$', views.addComplaint, name='addComplaint'),
    url(r'^complaints/$', views.complaints, name='complaints'),
    url(r'^updateComplaint/(\d+)/$', views.updateComplaint, name='updateComplaint'),
    url(r'^main/$', views.main, name='main'),
]