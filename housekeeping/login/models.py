from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, timedelta
class Complainee(User):
    room_no = models.CharField(max_length=15, blank=True)
    mobile_no = models.CharField(max_length=15, blank=True)
    class Meta:
        verbose_name="Complainee"
        verbose_name_plural="Complainee"

class Admin(User):
    class Meta:
        verbose_name = "Admin"
        verbose_name_plural = "Admin"

class Complaint(models.Model):
    user = models.ForeignKey(User, related_name='+',null=True)
    status=models.CharField(max_length=20,blank=False,default="New")
    subject = models.CharField(max_length=150, blank=True)
    feedback = models.TextField(max_length=500, blank=True)
    lodge_date=models.DateField(blank=True,default=datetime.today().date())
    addressing_date=models.DateField(blank=True,default=datetime.today().date()+timedelta(days=1))

    def __str__(self):
        return self.status + "   " + str(self.id) +"    " +self.subject

    def setFeedback(self,f):
        self.feedback=f

    def setStatus(self,s):
        self.status=s

