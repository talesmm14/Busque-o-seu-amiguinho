from django.urls import path

from core.views import page_home_view

urlpatterns = [
    path('', page_home_view, name='page_home_view'),
]
