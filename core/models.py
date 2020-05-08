from colorful.fields import RGBColorField
from django.db import models
from django.contrib.auth.models import User
from datetime import date
from django.urls import reverse


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    github = models.URLField(verbose_name="GitHub", blank=True, default="")
    telegram_nick = models.TextField(verbose_name="Telegram", blank=True, default="")
    discord_nick = models.TextField(verbose_name="Discord", blank=True, default="")
    tags = models.ManyToManyField("Tag")
    bio = models.TextField(
        "Sobre você",
        default="",
        help_text="Descreva sobre você para os amiginhos poderem te conhecer melhor!!",
    )

    def __str__(self):
        return "{} {}".format(self.user.first_name, self.user.last_name)

    def __repr__(self):
        return "{} {}".format(self.user.first_name, self.user.last_name)

    class Meta:
        verbose_name = "Perfil"
        verbose_name_plural = "Perfis"


class StudyRoom(models.Model):
    group_name = models.CharField("Nome do grupo", max_length=500, blank=False)
    telegram_group = models.URLField(verbose_name="Telegram", blank=True, default="")
    discord_group = models.URLField(verbose_name="Discord", blank=True, default="")
    # users_group = models.ManyToManyField("Profile")
    tags_group = models.ManyToManyField("Tag")
    limit_date = models.DateField(verbose_name="Data expiracao do Grupo", default=date.today)

    def __str__(self):
        return self.group_name

    def __repr__(self):
        return self.group_name

    def get_absolute_url(self):
        return reverse('create-group', kwargs={'pk': self.pk})


class Tag(models.Model):
    name = models.CharField("Tag", max_length=100, default="", blank=False)
    color = RGBColorField()

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name
