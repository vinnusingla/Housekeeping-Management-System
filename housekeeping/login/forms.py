from django import forms
from django.contrib.auth.models import User
from .models import Complainee,Complaint

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

class RegForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username','first_name','last_name', 'email', 'password']

class ComplaineeForm(forms.ModelForm):
    class Meta:
        model = Complainee
        fields = ('room_no', 'mobile_no')

class AddComplaintForm(forms.ModelForm):
    class Meta:
        model = Complaint
        fields = ('subject',)

class feedbackForm(forms.ModelForm):
    class Meta:
        model = Complaint
        fields = ('feedback',)
class UpdateComplaint_staffForm(forms.ModelForm):
    class Meta:
        model = Complaint
        fields = ('status', 'addressing_date',)
class SelectDateForm(forms.ModelForm):
    class Meta:
        model = Complaint
        fields= ('addressing_date',)

