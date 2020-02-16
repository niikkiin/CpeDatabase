from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class DashBoardView(TemplateView):
    template_name = 'home/dashboard.html'

class SectionsView(TemplateView):
    template_name = 'home/sections.html'
