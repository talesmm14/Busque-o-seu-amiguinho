from django.urls import path

from core.views import *
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', page_home_view, name='page_home_view'),
    path('signup/', page_signup, name='page_signup'),
    path('profile/', profile_area, name='profile_area'),
    path('profiles/', profiles_view, name='profiles_view'),
    path('login/', auth_views.LoginView.as_view(template_name="login.html"), name="login", ),
    path('logout/', auth_views.LogoutView.as_view(next_page="/"), name="logout"),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name="password-reset.html"),
         name="password_reset", ),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name="password_reset_done", ),
    #path('reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/',
    #auth_views.PasswordResetConfirmView.as_view(), name="password_reset_confirm", ),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name="password_reset_complete", ),
    path('info/', profile_change_info, name="change_info"),
    path('password/', profile_change_password, name="change_password"),
    path('create-group/', study_room_creation, name="study_room_creation")
    #path('create-group/', study_room_creation, name="study_room_creation")
]
