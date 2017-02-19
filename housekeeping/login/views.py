from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404 ,redirect
from .models import Complainee
from .forms import UserForm,RegForm,ComplaineeForm

def index(request):
   return render(request, "login/index.html", {})

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_superuser:
                return redirect('http://127.0.0.1:8000/admin/')
            else:
                return render(request, 'login/success.html')
    return render(request, 'login/login.html')

def logout_user(request):
    logout(request)
    form = UserForm(request.POST or None)
    context = {
        "form": form,
    }
    return render(request, 'login/login.html', context)

# def register(request):
#     form = RegForm(request.POST or None)
#     pform =ProfileForm(request.POST or None)
#     if form.is_valid() and pform.is_valid():
#         user = form.save(commit=False)
#         Profile = pform.save(commit=False)
#         password = form.cleaned_data['password']
#         user.set_password(password)
#         user.save()
#         Profile.save()
#     context = {
#         "form": form,
#         "pform":pform,
#     }
#     return render(request, 'login/register.html', context)
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
        return render(request, 'login/success.html')
    context = {
        "form": form,
        "pform":pform,
    }
    return render(request, 'login/register.html', context)
