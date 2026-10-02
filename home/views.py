from django.shortcuts import render
from django.views import View
from .models import Skill, SkillValue

class HomePageView(View):

    def get(self, request):
        skills = Skill.objects.all()
        return render(request, "home.html", {"skills" : skills})