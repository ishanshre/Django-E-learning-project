from django.urls import path
from django.contrib.auth.views import LogoutView

from user import views

app_name = "user"
urlpatterns = [
    path("register/", views.UserRegisterView.as_view(), name="register"),
    path("login/", views.UserLoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("password/change/", views.PasswordChangeView.as_view(), name="password_change"),
    path('profile/', views.UserProfileDetailEditView.as_view(), name='profile'),
    path('beacome-instructor/', views.BeacomeInstructor.as_view(), name='become-instructor'),
]