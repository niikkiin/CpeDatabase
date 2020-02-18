from django import forms
from home.models import Section, Student
from home.choices import *

# validation 
# from django.core.validators import RegexValidator
# student_number_validator = RegexValidator(r"^(199\d|200\d|2020)-(\b\d{5}\b)-(MN|mn)-(0|1)$", "Please follow the correct format for student number. e.g.(2015-02986-MN-0)")

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
    student_number  = forms.CharField(max_length=17)

    class Meta():
        model = Student
        fields = ('student_number', 'last_name', 'first_name', 'middle_name', 'gender')

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
