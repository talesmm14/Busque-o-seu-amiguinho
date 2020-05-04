from django.contrib import messages
from django.contrib.auth import login, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Profile, Tag, StudyRoom

# Create your views here.
from core.forms import RegisterForm, PasswordChangeForm, EditProfileForm


def page_home_view(request):
    return render(request, "pages/index.html")


def page_signup(request):
    context = {"form": RegisterForm(request.POST or None)}

    if request.method == "POST" and context["form"].is_valid():
        user = context["form"].save()
        login(request, user)
        return redirect("/")
    return render(request, "signup.html", context)


@login_required
def profile_area(request):
    return render(request, "profile-area.html")


@login_required
def profile_change_password(request):
    template_name = "profile-area-password-change.html"
    context = {"form": PasswordChangeForm(request.user)}

    if request.method == "POST":
        if context["form"].is_valid():
            context["form"] = PasswordChangeForm(request.user, request.POST)
            user = context["form"].save()
            context["message"] = "Sua senha foi alterada com sucesso!"
            update_session_auth_hash(request, user)
            return render(request, template_name, context)
        else:
            context["form"] = PasswordChangeForm(request.user, request.POST)
            context["message"] = "Por favor, corrija os erros abaixo."
    return render(request, "password-reset.html", context)


@login_required
def profile_change_info(request):
    profile = request.user.profile
    template = "profile-area-info-change.html"
    context = {"form": EditProfileForm(instance=profile)}

    if request.method == "POST":
        context["form"] = EditProfileForm(instance=profile, data=request.POST)
        if context["form"].is_valid():
            user = context["form"].save()
            context["message"] = "Suas informações foram atualizadas com sucesso!"
            return render(request, template, context)
        else:
            context["message"] = "Por favor, corrija os erros abaixo."
            messages.error(request, "Por favor, corrija os erros abaixo.")

    return render(request, template, context)


# Create your views here.

def page_home_view(request):
    return render(request, "pages/index.html")


# view_profiles (Visualizar Amiguinhos)
def profiles_view(request):
    profiles = Profile.objects.all()
    return render(request, "profiles.html", {'profiles': profiles})


# create view_rooms

# study_room creation
class RegisterRoom(object):
    pass


def study_room_creation(request):
    context = {"form": RegisterRoom(request.POST or None)}

    if request.method == "POST" and context["form"].is_valid():
        user = context["form"].save()
        login(request, user)
        return redirect("/")
    return render(request, "study_room_creation.html", context)
