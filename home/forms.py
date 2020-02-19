from django import forms
from home.models import Section, Student
from home.choices import *

# validation 
from django.core.exceptions import ValidationError
import re

# def validate_student_number(value):
#     student = Student.objects.filter(student_number=value)
#     if student: # check if any object exists
#         raise ValidationError('This student number is already registered in our system.') 
#     if not student:
#         reg = re.compile('^(199\d|200\d|2020)-(\b\d{5}\b)-(MN|mn)-(0|1)$')
#         if not reg.match(value):
#             raise ValidationError('Please follow the correct format for student number. e.g.(2015-02986-MN-0)') 
#         else:
#             return value

class SectionForm(forms.ModelForm):
    academic_year = forms.ChoiceField(choices=ACADEMIC_YEAR_CHOICES)
    class Meta():
        model = Section
        fields = ('name', 'academic_year')
        labels = {
            "name" : "Name",
            "academic_year": "A.Y."
        }


    def __init__(self, *args, **kwargs):
        kwargs.setdefault('label_suffix', '')  # globally override the Django >=1.6 default of ':'
        super(SectionForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control theme-input muli-font'
            self.fields['name'].widget.attrs['placeholder'] = 'Enter the section name'
            self.fields['academic_year'].widget.attrs['placeholder'] = 'Enter the academic year'

class StudentForm(forms.ModelForm):
    gender = forms.ChoiceField(choices=GENDER_CHOICES)
    # student_number  = forms.CharField(validators=[student_number_validator])
    # student_number  = forms.CharField(validators=[validate_student_number])

    class Meta():
        model = Student
        fields = ('student_number', 'last_name', 'first_name', 'middle_name', 'gender')

    # def clean_student_number(self):
    #     student_number = self.cleaned_data['student_number']
    #     try:
    #         student_number = student_number.objects.filter(student_number=self.instance.student_number)
    #     except student_number.DoesNotExist:
    #         return student_number
    #     raise forms.ValidationError(_("This student number is already registered in our system."))
    
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('label_suffix', '')  # globally override the Django >=1.6 default of ':'
        super(StudentForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control theme-input muli-font'
            # self.fields['name'].widget.attrs['placeholder'] = 'Enter the section name'
            # self.fields['academic_year'].widget.attrs['placeholder'] = 'Enter the academic year'
            self.fields['student_number'].widget.attrs['placeholder'] = 'e.g. 2015-00000-MN-0'
            self.fields['last_name'].widget.attrs['placeholder'] = 'Dela Cruz'
            self.fields['first_name'].widget.attrs['placeholder'] = 'Juan'
            self.fields['middle_name'].widget.attrs['placeholder'] = 'Abad'
            
    # def __str__(self):
    #     return self.first_name
