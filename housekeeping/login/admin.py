from django.contrib import admin
from  .models import Complainee,Complaint,Admin

class ComplaintAdmin(admin.ModelAdmin):
    list_display = ('status', 'id', 'subject','lodge_date')
    search_fields = ('status', 'id')
    list_filter = ('lodge_date',)
    date_hierarchy = 'lodge_date'
    ordering = ('-lodge_date',)
    #fields = ('user', 'id', 'subject','status','subject','feedback','addressing_date')


admin.site.register(Complainee)
admin.site.register(Admin)
admin.site.register(Complaint,ComplaintAdmin)