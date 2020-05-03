from django.shortcuts import render
from .models import Profile

# Create your views here.

def page_home_view(request):
    return render(request, "pages/index.html")

#create view_profiles
def profiles_view(request):
    user = Profile.user
    github = Profile.github
    bio = Profile.github
    return render(request, "pages/profiles.html", {"user": user, "github": github, "bio": bio})

#create view_rooms

