from django.contrib import admin
from home.models import Section, Student
# Register your models here.

class SectionAdmin(admin.ModelAdmin):
    list_display = ('name', 'academic_year')
    search_fields = ('name', 'academic_year')
    readonly_fields = ()
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(Section, SectionAdmin)

class StudentAdmin(admin.ModelAdmin):
    list_display = ('student_number', 'last_name', 'section', 'gender')
    search_fields = ('student_number', 'last_name')
    readonly_fields = ()
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(Student, StudentAdmin)