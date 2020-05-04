from django.db import models

from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    github = models.URLField(verbose_name="GitHub", blank=True, default="")
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
    telegram = models.URLField(verbose_name="Telegram", blank=True, default="")
    discord = models.URLField(verbose_name="Discord", blank=True, default="")
    users = models.ManyToManyField(Profile, blank=True)
    tags = models.ManyToManyField("Tag")


class Tag(models.Model):
    name = models.CharField("Tag", max_length=100, default="", blank=False)

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name