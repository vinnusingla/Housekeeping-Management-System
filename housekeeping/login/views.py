from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404 ,redirect,Http404
from .models import Complainee,Complaint
from .forms import UserForm,RegForm,ComplaineeForm,AddComplaintForm,feedbackForm,UpdateComplaint_staffForm,SelectDateForm
#from xhtml2pdf.utils import generate_pdf
from datetime import datetime , timedelta
def index(request):
   return render(request, "login/index.html", {})

def Login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None and user.is_superuser:
            login(request,user)
            return redirect('http://127.0.0.1:8000/login/main_staff/')
        elif user is not None:
            login(request,user)
            return redirect('http://127.0.0.1:8000/login/main/')
        else:
            return render(request, 'login/login_user.html')
    return render(request, 'login/login_user.html')


def generateToDoList(request):
    if request.user.is_authenticated() and request.user.is_superuser:
        form = SelectDateForm(request.POST or None)
        if form.is_valid():
            list = Complaint.objects.filter(addressing_date =request.POST['addressing_date'])
            List=[]
            if not list:
                return render(request, 'login/noJob.html')
            for li in list:
                usern=li.user.username
                Comp=Complainee.objects.filter(username=usern)
                List.extend(Comp)
            list_new=zip(list,List)
            context = {"list_new": list_new }
            return render(request, 'login/print_tasks2.html',context)
        context= {"form":form}
        return render(request, 'login/print_tasks.html',context)
    else:
        if(request.user.is_authenticated()):
            return  redirect('http://127.0.0.1:8000/login/main/')
        else:
            return redirect('http://127.0.0.1:8000/login/')

def main(request):
    if request.user.is_authenticated() and request.user.is_superuser:
        context = {'username': request.user}
        return render(request, 'login/main_staff.html', context)
    elif request.user.is_authenticated():
        context = {'username': request.user}
        return render(request, 'login/main.html', context)
    else:
        return redirect('http://127.0.0.1:8000/login/')

def Logout(request):
    logout(request)
    form = UserForm(request.POST or None)
    context = {
        "form": form,
    }
    return redirect('http://127.0.0.1:8000/login/')

def registration(request):
    form = RegForm(request.POST or None)
    pform =ComplaineeForm(request.POST or None)
    if form.is_valid() and pform.is_valid():
        user=User(username=request.POST['username'],password=request.POST['password'],first_name=request.POST['first_name'],last_name=request.POST['last_name'],email=request.POST['email'])
        password = form.cleaned_data['password']
        user.set_password(password)
        p = Complainee(username=request.POST['username'],password=request.POST['password'],first_name=request.POST['first_name'],last_name=request.POST['last_name'],email=request.POST['email'],room_no=request.POST['room_no'], mobile_no=request.POST['mobile_no'])
        p.set_password(password)
        p.save()
        return redirect('http://127.0.0.1:8000/login/')
    context = {
        "form": form,
        "pform":pform,
    }
    return render(request, 'login/register.html', context)

def addComplaint(request):
    if request.user.is_authenticated():
        form = AddComplaintForm(request.POST or None)
        if form.is_valid():
            comp = Complaint()
            comp.subject = request.POST['subject']
            comp.user = request.user
            comp.save()
            return render(request, 'login/main.html')
        context = {"form": form}
        return render(request, 'login/make_complaint.html', context)
    else:
        return redirect('http://127.0.0.1:8000/login/')

def fetchComplaint(request):
    if request.user.is_authenticated() and request.user.is_superuser:
        list=Complaint.objects.all()
        context={"list":list}
        return render(request, 'login/complaints_staff.html',context)
    elif request.user.is_authenticated():
        list=Complaint.objects.filter(user=request.user)
        context={"list":list}
        return render(request, 'login/complaints.html',context)
    else:
        return redirect('http://127.0.0.1:8000/login/')
def flushComplaint(request):
    if request.user.is_authenticated() and request.user.is_superuser:
        today=datetime.today().date()
        targetday=today - timedelta(days=7)
        Complaint.objects.filter(status ="Closed").filter(addressing_date__lte=targetday).delete()
        return redirect('http://127.0.0.1:8000/login/complaints')
    else:
        return redirect('http://127.0.0.1:8000/login/')
def showClosedComplaints(request):
    list = Complaint.objects.filter(status="Closed")
    if request.user.is_authenticated() and request.user.is_superuser:
        context = {"list": list}
        return render(request, 'login/showClosedComplaints.html', context)
    elif request.user.is_authenticated():
        list=list.filter(user=request.user)
        context = {"list": list}
        return render(request, 'login/showClosedComplaints.html', context)
    else:
        return redirect('http://127.0.0.1:8000/login/')

def feedback(request , offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    if request.user.is_authenticated():
        instance=get_object_or_404(Complaint,id=offset)
        form=feedbackForm(request.POST or None,instance=instance)
        if form.is_valid():
            instance.feedback=request.POST['feedback']
            instance.save()
            return redirect('http://127.0.0.1:8000/login/complaints/')
        context = {"form": form}
        return render(request, 'login/feedback.html', context)
    else:
        return redirect('http://127.0.0.1:8000/login/')
def reopenComplaint(request , offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    if request.user.is_authenticated():
        instance=get_object_or_404(Complaint,id=offset)
        if instance.status=="Closed":
            instance.status="Reopen"
            instance.save()
        return redirect('http://127.0.0.1:8000/login/complaints/')
    else:
        return redirect('http://127.0.0.1:8000/login/')

def updateStatus(request , offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    if request.user.is_authenticated():
        instance=get_object_or_404(Complaint,id=offset)
        form=UpdateComplaint_staffForm(request.POST or None)
        if form != None and form.is_valid():
            instance.status = request.POST['status']
            instance.addressing_date=request.POST['addressing_date']
            instance.save()
            return redirect('http://127.0.0.1:8000/login/complaints_staff/')
        context = {"form": form , "feedback":instance.feedback}
        return render(request, 'login/update_complaint_staff.html', context)
    else:
        return redirect('http://127.0.0.1:8000/login/')
