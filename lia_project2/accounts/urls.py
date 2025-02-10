from django.urls import path
from accounts.views import (
    user_login, user_logout, user_signup,
    password_reset_request, password_reset_verify, password_reset_confirm, password_update
)

app_name = "accounts"

urlpatterns = [
    path("login/", user_login, name="login"),
    path("logout/", user_logout, name="logout"),
    path("signup/", user_signup, name="signup"),

    path("dashboard/", dashboard, name="dashboard"),
    
    path("password_reset/", password_reset_request, name="password_reset"),
    path("password_reset_verify/<str:username>/", password_reset_verify, name="password_reset_verify"),
    path("password_reset_confirm/<str:username>/", password_reset_confirm, name="password_reset_confirm"),
    path("password_update/", password_update, name="password_update"),
]
