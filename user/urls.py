from django.urls import path
from django.contrib.auth.views import LogoutView

from user import views

app_name = "user"
urlpatterns = [
    path("register/", views.UserRegisterView.as_view(), name="register"),
    path("login/", views.UserLoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),

]