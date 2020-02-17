from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, CreateView, ListView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin

from home.models import Section, Student
from home.forms import SectionForm, StudentForm

# Create your views here.

class DashBoardView(LoginRequiredMixin, TemplateView):
    login_url = '/'
    template_name = 'home/dashboard.html'

class SectionsListView(LoginRequiredMixin, ListView):
    login_url = '/'
    template_name = 'home/sections.html'
    model = Section

class SectionCreateView(LoginRequiredMixin, CreateView):
    login_url = '/'
    template_name = 'home/section_form.html'
    form_class = SectionForm

    def form_valid(self, form):
        print(form.instance.name)

        return super().form_valid(form)

class StudentsListView(LoginRequiredMixin, ListView):
    login_url = '/'
    template_name = 'home/student_view.html'

    def get_queryset(self):
        pk = self.kwargs['pk']
        section = get_object_or_404(Section, pk=pk)

        return Student.objects.filter(section=section)
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs['pk']
        section = get_object_or_404(Section, pk=pk)

        context["section"] = section
        return context
    

class StudentCreateView(LoginRequiredMixin, CreateView):
    login_url = '/'
    template_name = 'home/student_form.html'
    form_class = StudentForm

    def form_valid(self, form, **kwargs):
        pk = self.kwargs['pk']
        section = get_object_or_404(Section, pk=pk)

        form.instance.section = section
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs['pk']
        section = get_object_or_404(Section, pk=pk)

        context["section"] = section
        return context

class StudentIndividualView(TemplateView):
    template_name = 'home/student_individual_view.html'


class StudentUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/'
    template_name = 'home/student_form.html'
    model = Student
    form_class = StudentForm
