from django.db import models

# Create your models here.
class Student(models.Model):
    Student_Key = models.IntegerField(primary_key=True)
    School_Key = models.IntegerField(default=0)
    Local_Student_ID = models.CharField(max_length=25)
    Last_Name = models.CharField(max_length=35)
    First_Name = models.CharField(max_length=35)
    Middle_Name = models.CharField(max_length=35)
    Preferred_Name = models.CharField(max_length=80)
    Birth_Date = models.DateField()
    Gender = models.CharField(max_length=30)
    Grade_Level = models.CharField(max_length=30)
    Location_Type = models.CharField(max_length=30)
    Street_Addr_Line1 = models.CharField(max_length=100)
    City = models.CharField(max_length=30)
    State = models.CharField(max_length=2)
    Zip_Code = models.CharField(max_length=10)
    Phone_Number = models.CharField(max_length=15)
    Date_Stamp = models.DateTimeField()

