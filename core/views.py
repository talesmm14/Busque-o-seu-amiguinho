from django.contrib import messages
from django.contrib.auth import login, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Profile

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
def profile_change_password(request):
    template_name = "pythonistas-area-password-change.html"
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
    template = "pythonistas-area-info-change.html"
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


# create view_profiles
def profiles_view(request):
    user = Profile.user
    github = Profile.github
    bio = Profile.github
    return render(request, "pages/profiles.html", {"user": user, "github": github, "bio": bio})

# create view_rooms
