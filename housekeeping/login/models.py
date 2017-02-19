from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

class Complainee(models.Model):
    user = models.ForeignKey(User,related_name='+',null=True)
    room_no = models.CharField(max_length=15, blank=True)
    mobile_no = models.CharField(max_length=15, blank=True)

    def __str__(self):
        return self.user.username





class Complaint(models.Model):
    user = models.ForeignKey(User, related_name='+',null=True)
    status=models.CharField(max_length=20,blank=False,default="New")
    subject = models.CharField(max_length=150, blank=True)
    feedback = models.TextField(max_length=500, blank=True)
    lodge_date=models.DateField(blank=True,default=datetime.today().date())
    addressing_date=models.DateField(blank=True,default=datetime.today().date())

    def __str__(self):
        return self.status + "   " + str(self.id) +"    " +self.subject

    def setFeedback(self,f):
        self.feedback=f

    def setStatus(self,s):
        self.status=s

    def has_feedback(self):
        if(self.feedback==""):
            return False
        else:
            return True

    def is_reopen(self):
        if(self.status=="Reopen"):
            return True
        else:
            return False