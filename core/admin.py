from django.contrib import admin

# Register your models here.
from core.models import *

admin.site.register(Profile)
admin.site.register(StudyRoom)
admin.site.register(Tag)