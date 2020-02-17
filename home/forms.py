from django import forms
from home.models import Section, Student
from home.choices import *

class SectionForm(forms.ModelForm):

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

    class Meta():
        model = Student
        fields = ('student_number', 'last_name', 'first_name', 'section', 'gender')

    def __init__(self, *args, **kwargs):
        kwargs.setdefault('label_suffix', '')  # globally override the Django >=1.6 default of ':'
        super(StudentForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control theme-input muli-font'
            # self.fields['name'].widget.attrs['placeholder'] = 'Enter the section name'
            # self.fields['academic_year'].widget.attrs['placeholder'] = 'Enter the academic year'
