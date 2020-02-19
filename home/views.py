from django.shortcuts import render, redirect,get_object_or_404
from django.urls import reverse
from django.views.generic import TemplateView, CreateView, ListView, UpdateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

from django.contrib import messages

from home.models import Section, Student
from home.forms import SectionForm, StudentForm

from account.models import Log


# validation 
from django.core.exceptions import ValidationError
import re


# Create your views here.

class DashBoardView(LoginRequiredMixin, TemplateView):
    login_url = '/'
    template_name = 'home/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        sections = Section.objects.all()
        student_count = Student.objects.count()
        logs = Log.objects.order_by('-created_at')

        context["sections"] = sections 
        context["all_student_count"] = student_count 
        context["logs"] = logs
        return context
    

class SectionsListView(LoginRequiredMixin, ListView):
    login_url = '/'
    template_name = 'home/sections.html'
    model = Section

    def get_context_data(self, **kwargs):
        student_count = Student.objects.count()
        context = super(SectionsListView, self).get_context_data(**kwargs)
        context['all_student_count'] = student_count
        return context
    
class ManageSectionsListView(LoginRequiredMixin, ListView):
    login_url = '/'
    template_name = 'home/view_all_section.html'
    model = Section

    def get_context_data(self, **kwargs):
        student_count = Student.objects.count()
        context = super(ManageSectionsListView, self).get_context_data(**kwargs)
        context['all_student_count'] = student_count
        return context
    

class SectionCreateView(LoginRequiredMixin, CreateView):
    login_url = '/'
    template_name = 'home/section_form.html'
    form_class = SectionForm

    def form_valid(self, form):

        create_action = "{} added section {}".format(self.request.user, form.instance.name)
        action = Log.objects.create(
            user = self.request.user,
            action = create_action,
        )

        return super().form_valid(form)

class SectionUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/'
    template_name = 'home/section_form.html'
    model = Section
    form_class = SectionForm

    def form_valid(self, form):
        update_action = "{} updated the data of Section {}".format(self.request.user, form.instance.name)
        action = Log.objects.create(
            user = self.request.user,
            action = update_action,
        )

        return super().form_valid(form)

    



def delete_section(request, pk):
    section = Section.objects.get(pk=pk)

    delete_action = "{} deleted the data of Section {}".format(request.user, section.name)
    action = Log.objects.create(
        user = request.user,
        action = delete_action,
    )

    section.delete()
    return redirect('home:sections-manage')

class StudentList(LoginRequiredMixin, ListView):
    login_url = '/'
    template_name = 'home/student_view.html'
    model = Student

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

        create_action = "{} added {} to section {}".format(self.request.user, form.instance.last_name, section)
        action = Log.objects.create(
            user = self.request.user,
            action = create_action,
        )
        
        return super().form_valid(form)
        
    def form_invalid(self, form, **kwargs):
        student = Student.objects.filter(student_number=form.instance.student_number)
        
        if len(form.instance.last_name) == 0:
            messages.error(self.request, 'Last Name Field is required.')
        if len(form.instance.first_name) == 0:
            messages.error(self.request, 'First Name Field is required.')
            
        if student.exists():
            # raise ValidationError('This student number is already registered in our system.')
            messages.error(self.request, 'The student number is already registered in our system.')
        else:
            reg = re.compile('^(199\d|200\d|2020)-(\b\d{5}\b)-(MN|mn)-(0|1)$')
            if len(form.instance.student_number) > 0:
                if not reg.match(form.instance.student_number):
                    # raise ValidationError('Please follow the correct format for student number. e.g.(2015-02986-MN-0)') 
                    messages.error(self.request, 'Please follow the correct format for the student number. e.g.(2015-02986-MN-0)')
            else:
                messages.error(self.request, 'Student Number Field is required.')
                
                
        pk = self.kwargs['pk']
        return redirect('home:create-student', pk=pk)
        

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs['pk']
        section = get_object_or_404(Section, pk=pk)

        context["section"] = section
        return context

class StudentDetailView(DetailView):
    template_name = 'home/student_individual_view.html'
    context_object_name = 'student'
    model = Student


class StudentUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/'
    template_name = 'home/student_form.html'
    model = Student
    form_class = StudentForm
    
    def form_valid(self, form):
        update_action = "{} updated the data of {}".format(self.request.user, form.instance.last_name)
        action = Log.objects.create(
            user = self.request.user,
            action = update_action,
        )

        return super().form_valid(form)

    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs['pk']
        student = get_object_or_404(Student, pk=pk)
        section = Section.objects.get(pk=student.section.pk)

        context["section"] = section
        return context

def delete_student(request, pk):
    student = Student.objects.get(pk=pk)
    section = student.section.pk

    delete_action = "{} deleted the data of {}".format(request.user, student.last_name)
    action = Log.objects.create(
        user = request.user,
        action = delete_action,
    )

    student.delete()
    return redirect('home:student-list-view', pk=section)
