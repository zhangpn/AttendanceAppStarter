from django.contrib import admin
from attendance.models import School, CohortGroup, Student, StudentCohortGroup, EnhancementPartner

# Register your models here.

class SchoolAdmin(admin.ModelAdmin):
    list_display = ('School_Key', 'District_ID')

class CohortGroupAdmin(admin.ModelAdmin):
    list_display = ('Cohort_Group_Key', 'Program_Key', 'Session_Key', 'School_Key')

class StudentAdmin(admin.ModelAdmin):

    list_display = ('Student_Key', 'Last_Name', 'First_Name', 'Preferred_Name', 'Gender')
    #list_filter = ['pub_date']
    #search_fields = ['question_text']

class StudentCohortGroupAdmin(admin.ModelAdmin):
    list_display = ('Cohort_Group_Key', 'Program_Key', 'Session_Key', 'School_Key', 'Student_Key',
    'Effective_Date', 'Ending_Date', 'Date_Stamp')

class EnhancementPartnerAdmin(admin.ModelAdmin):
    list_display = EnhancementPartner._meta.get_all_field_names()

admin.site.register(School, SchoolAdmin)
admin.site.register(CohortGroup, CohortGroupAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(StudentCohortGroup, StudentCohortGroupAdmin)
admin.site.register(EnhancementPartner, EnhancementPartnerAdmin)

