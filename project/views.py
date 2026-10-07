from django.shortcuts import render
from .models import Projcet
from django.views import View
from django.views.generic import ListView


class ProjectListView(ListView):
    model = Projcet
    template_name = "project.html"
    context_object_name = "projects"

