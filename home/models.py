from django.db import models
from django.urls import reverse


# from django.core.validators import RegexValidator

from home.choices import GENDER_CHOICES



# Create your models here.
class Section(models.Model):
    name            = models.CharField(max_length=10, unique=True)
    academic_year   = models.CharField(max_length=10)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("home:sections")

class Student(models.Model):
    section         = models.ForeignKey(Section, on_delete=models.CASCADE, null=True)
    student_number  = models.CharField(max_length=17, unique=True)
    last_name       = models.CharField(max_length=30)
    first_name      = models.CharField(max_length=30)
    middle_name     = models.CharField(max_length=30, blank=True, default='')
    gender          = models.IntegerField(choices=GENDER_CHOICES, default=0)
    
    def __str__(self):
        return self.last_name
    
    def get_absolute_url(self):
        return reverse("home:student-list-view", kwargs={"pk": self.section.pk})