from django.db import models

from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    github = models.URLField(verbose_name="GitHub", blank=True, default="")

    def __str__(self):
        return "{} {}".format(self.user.first_name, self.user.last_name)

    def __repr__(self):
        return "{} {}".format(self.user.first_name, self.user.last_name)


class StudyRoom(models.Model):
    pass
