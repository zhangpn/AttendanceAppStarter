from django.contrib import admin
from attendance.models import Student

# Register your models here.


class StudentAdmin(admin.ModelAdmin):

    list_display = ('Student_Key', 'Last_Name', 'First_Name', 'Preferred_Name', 'Gender')
    #list_filter = ['pub_date']
    #search_fields = ['question_text']

admin.site.register(Student, StudentAdmin)