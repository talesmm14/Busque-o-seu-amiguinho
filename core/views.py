from django.contrib.auth import login
from django.shortcuts import render, redirect



# Create your views here.
from core.forms import RegisterForm
from .models import Profile

def page_home_view(request):
    return render(request, "pages/index.html")


def page_signup(request):
    context = {"form": RegisterForm(request.POST or None)}

    if request.method == "POST" and context["form"].is_valid():
        user = context["form"].save()
        login(request, user)
        return redirect("/")
    return render(request, "signup.html", context)

#Create your views here.

def page_home_view(request):
    return render(request, "pages/index.html")

#create view_profiles
def profiles_view(request):
    profiles = Profile.objects.all()
    return render(request, "profiles.html", {"profiles": profiles})

#create view_rooms