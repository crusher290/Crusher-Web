from django.shortcuts import render
from django.views import View
from .models import Skill, SkillValue, Resume, SocialLink

class HomePageView(View):

    def get(self, request):
        skills = Skill.objects.all()
        resume = Resume.objects.filter(is_active=True).order_by("-updated_at").first()
        sociallink = SocialLink.objects.filter(is_active=True)
        return render(request, "home.html", {
            "skills" : skills,
            "resume" : resume,
            "contacts" : sociallink
            })

