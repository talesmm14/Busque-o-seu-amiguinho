from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm
from django import forms

from core.models import Profile, Tag
from django_select2.forms import Select2MultipleWidget, Select2Widget
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
    github = forms.URLField(
        label="Github (opcional)",
        widget=forms.TextInput(attrs={"placeholder": "Link do seu GitHub"}),
        required=False,
    )

    tags_ = forms.ModelMultipleChoiceField(
        label="Tags", queryset=Tag.objects.all(), widget=Select2MultipleWidget
    )

    class Meta:
        model = User
        fields = ("first_name", "last_name", "email", "username")

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)

        for fieldname in ["password1", "password2"]:
            self.fields[fieldname].help_text = None

    def save(self, commit=True):
        instance = super(RegisterForm, self).save(commit=False)

        if commit:
            instance.save()

            profile = Profile(
                user=instance,
                github=self.cleaned_data["github"],
                on_mailing_list=self.cleaned_data["on_mailing_list"],
            )
            authenticate(
                username=instance.username, password=self.cleaned_data.get("password1")
            )
            profile.save()
            profile.tags.set(self.cleaned_data["tags_"])
            profile.save()
        return instance
