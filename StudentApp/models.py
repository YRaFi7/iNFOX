from django.db import models

# Create your models here.
class Student_details(models.Model):
    s_name=models.CharField(max_length=100)
    s_age=models.IntegerField()
    s_address=models.TextField()
    s_joining_date=models.DateField()
    s_email_id=models.CharField(max_length=50)
    s_qualifications=models.CharField(max_length=50)
    s_gender=models.CharField(max_length=50)
    s_phone=models.CharField(max_length=12)
    
