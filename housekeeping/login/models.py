from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, timedelta
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

def validateSubjectFeedback(value):
    mode=0
    for c in value:
        if(c=='0' or c=='1' or c=='2' or c=='3' or c=='4' or c=='5' or c=='6' or c=='7' or c=='8' or c=='9' or c==' ' ):
          mode=mode+1
    if mode == len(value):
        raise ValidationError(
            _('%(value)s is not a valid input'),
            params={'value': value},
        )

def validateAddressingDate(value1):
    def func(value2):
        if(value1.date()>value2):
            raise ValidationError(
                _('addressing date should be greater than %(value1)s'),
                params={'value1':value1.date()}
            )
    return func

class Complainee(User):
    room_no = models.PositiveIntegerField(max_length=4, blank=False)
    mobile_no = models.PositiveIntegerField(max_length=10, blank=False)
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
    subject = models.CharField(max_length=150, blank=False ,validators=[validateSubjectFeedback])
    feedback = models.TextField(max_length=500, blank=False ,validators=[validateSubjectFeedback])
    lodge_date=models.DateField(blank=False,default=datetime.today().date())
    ld=datetime.now()
    addressing_date=models.DateField(blank=False,default=datetime.today().date()+timedelta(days=1) ,validators=[validateAddressingDate(ld)])

    def __str__(self):
        return self.status + "   " + str(self.id) +"    " +self.subject

    def setFeedback(self,f):
        self.feedback=f

    def setStatus(self,s):
        self.status=s

