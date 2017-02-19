from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404 ,redirect
from .models import Complainee,Complaint
from .forms import UserForm,RegForm,ComplaineeForm,AddComplaintForm,UpdateComplaintForm

def index(request):
   return render(request, "login/index.html", {})

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request,user)
            if user.is_superuser:
                return redirect('http://127.0.0.1:8000/admin/')
            else:
                return redirect('http://127.0.0.1:8000/login/main/')
    return render(request, 'login/login.html')

def main(request):
    if request.user.is_authenticated():
        context = {'username': request.user}
        return render(request, 'login/main.html', context)
    else:
        return redirect('http://127.0.0.1:8000/login/')

def logout_user(request):
    logout(request)
    form = UserForm(request.POST or None)
    context = {
        "form": form,
    }
    return redirect('http://127.0.0.1:8000/login/')

def register(request):
    form = RegForm(request.POST or None)
    pform =ComplaineeForm(request.POST or None)
    if form.is_valid() and pform.is_valid():
        user=User(username=request.POST['username'],password=request.POST['password'],first_name=request.POST['first_name'],last_name=request.POST['last_name'],email=request.POST['email'])
        password = form.cleaned_data['password']
        user.set_password(password)
        user.save()
        p = Complainee(room_no=request.POST['room_no'], mobile_no=request.POST['mobile_no'],user=user)
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
        context = {"form": form}
        return render(request, 'login/make_complaint.html', context)
    else:
        return redirect('http://127.0.0.1:8000/login/')

def complaints(request):
    if request.user.is_authenticated():
        list=Complaint.objects.filter(user=request.user)
        context={"list":list}
        return render(request, 'login/complaints.html',context)
    else:
        return redirect('http://127.0.0.1:8000/login/')

def UpdateComplaint(request):
    form=AddComplaintForm(request.POST or None)
    if form.is_valid():
        comp=Complaint()
        comp.subject=request.POST['subject']
        comp.user=request.user
        comp.save()
    context ={"form":form}
    return  render(request ,'login/complaint.html',context)