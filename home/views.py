from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, ListView

from home.models import Section
from home.forms import SectionForm, StudentForm

# Create your views here.

class DashBoardView(TemplateView):
    template_name = 'home/dashboard.html'

class SectionsListView(ListView):
    template_name = 'home/sections.html'
    model = Section

class SectionCreateView(CreateView):
    template_name = 'home/section_form.html'
    form_class = SectionForm

    def form_valid(self, form):
        print(form.instance.name)

        return super().form_valid(form)

class StudentsListView(TemplateView):
    template_name = 'home/student_view.html'

class StudentCreateView(CreateView):
    template_name = 'home/student_form.html'
    form_class = StudentForm

    def form_valid(self, form):
        print(form.instance.last_name)
        return super().form_valid(form)