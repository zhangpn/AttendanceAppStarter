import datetime
from django.db import models

# Create your models here.

class School(models.Model):
    School_Key = models.CharField(primary_key=True, max_length=15)
    District_ID = models.CharField(max_length=15)
    def __str__(self):
        return self.School_Key

class CohortGroup(models.Model):
    Cohort_Group_Key = models.IntegerField(default=0)
    Program_Key = models.IntegerField(default=0)
    Session_Key = models.IntegerField(default=0)
    School_Key = models.ForeignKey('School')
    Type = models.CharField(max_length=30, default=None)
    Program_Group = models.CharField(max_length=11, default=None)
    Session_Teacher_ID = models.CharField(max_length=50, default=None)
    Session_Teacher_Last_Name = models.CharField(max_length=35, default=None)
    Session_Teacher_First_Name = models.CharField(max_length=35, default=None)
    Session_Teacher_Birth_Date = models.DateField(default=None)
    Session_Teacher_Email = models.CharField(max_length=70, default=None)
    Start_Date = models.DateField(default=None)
    End_Date = models.DateField(default=None)
    Date_Stamp = models.DateTimeField(default=None)

    class Meta:
        unique_together = (('Cohort_Group_Key', 'Program_Key', 'Session_Key', 'School_Key'),)

# student demographics data
class Student(models.Model):
    Student_Key = models.CharField(primary_key=True, max_length=25)
    School_Key = models.ForeignKey('School')
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
    Date_Stamp = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.Student_Key

class StudentCohortGroup(models.Model):
    School_Key = models.ForeignKey('School')
    Cohort_Group_Key = models.IntegerField(default=0)
    Program_Key = models.IntegerField(default=0)
    Session_Key = models.IntegerField(default=0)
    Student_Key = models.ForeignKey('Student')
    Effective_Date = models.DateTimeField()
    Ending_Date = models.DateTimeField()
    Date_Stamp = models.DateTimeField()

class EnhancementPartner(models.Model):
    SEMESTER_CODE = (
        ('F', 'Fall'),
        ('S', 'Spring'),
    )

    START_YEAR = 2008
    YEAR_IN_ADVANCE = 2 # the number of years the enhancement partners can be scheduled in advanced

    YEAR_CHOICES = []
    for r in range(START_YEAR, (datetime.datetime.now().year + YEAR_IN_ADVANCE)):
        YEAR_CHOICES.append((r,r))

    Partner_ID = models.CharField(primary_key=True, max_length=12)
    Partner_Name = models.CharField(max_length=50)
    Semester = models.CharField(max_length=1, choices=SEMESTER_CODE)
    School_Year = models.IntegerField(max_length=4, choices=YEAR_CHOICES, default=datetime.datetime.now().year)
