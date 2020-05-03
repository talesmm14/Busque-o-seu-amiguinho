from django.urls import path

from core.views import page_home_view, page_signup, profiles_view

urlpatterns = [
    path('', page_home_view, name='page_home_view'),
    path('signup/', page_signup, name='page_signup'),
    path('profiles/', profiles_view, name='profiles_view'),
]
