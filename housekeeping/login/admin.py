from django.contrib import admin

# Register your models here.
from  .models import Complainee,Complaint
admin.site.register(Complainee)
admin.site.register(Complaint)