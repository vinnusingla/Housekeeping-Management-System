from django.conf.urls import url,include
from . import views


app_name = 'login'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^main_staff/$', views.main, name='main_staff'),
    url(r'^login_user/$', views.Login, name='login_user'),
    url(r'^login_staff/$', views.Login, name='login_staff'),
    url(r'^logout_user/$', views.Logout, name='logout_user'),
    url(r'^logout_staff/$', views.Logout, name='logout_staff'),
    url(r'^register/$', views.registration, name='register'),
    url(r'^addComplaint/$', views.addComplaint, name='addComplaint'),
    url(r'^flushComplaint/$', views.flushComplaint, name='flushComplaint'),
    url(r'^complaints/$', views.fetchComplaint, name='complaints'),
    url(r'^complaints_staff/$', views.fetchComplaint, name='complaints_staff'),
    url(r'^reopenComplaint/(\d+)/$', views.reopenComplaint, name='reopenComplaint'),
    url(r'^updateComplaint_staff/(\d+)/$', views.updateStatus, name='updateComplaint_staff'),
    url(r'^showClosedComplaints/$', views.showClosedComplaints, name='showClosedComplaints'),
    url(r'^feedback/(\d+)/$', views.feedback, name='feedback'),
    url(r'^main/$', views.main, name='main'),
    url(r'^print_tasks/$', views.generateToDoList, name='print_tasks'),
]