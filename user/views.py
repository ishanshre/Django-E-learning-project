from django.shortcuts import render, redirect, get_object_or_404

from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin

from django.contrib.auth.views import LoginView, PasswordChangeView
from django.contrib.auth.mixins import LoginRequiredMixin

from django.views.generic.edit import CreateView
from django.views import View

from django.urls import reverse, reverse_lazy

from user.forms import (
    CustomUserCreationForm, 
    LoginUserForm, 
    ProfileForm, 
    UserForm, 
)
from user.models import Profile
# Create your views here.

class UserRegisterView(SuccessMessageMixin, CreateView):
    form_class = CustomUserCreationForm
    template_name = "user/register.html"
    success_message = "New User Created Successfully"
    success_url = reverse_lazy("user:login")

    def form_valid(self, form):
        user = form.save(commit=False)
        user.save()
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.add_message(self.request, messages.ERROR, "Failed to create user! try again")
        return super().form_invalid(form)
    
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect("core:index")
        return super().dispatch(request, *args, **kwargs)



class UserLoginView(SuccessMessageMixin, LoginView):
    form_class = LoginUserForm
    template_name = "user/login.html"
    success_message = "Login Successfull"
    success_url = reverse_lazy("core:index")

    def form_invalid(self, form):
        messages.add_message(self.request, messages.ERROR, "Login Failed!")
        return super().form_invalid(form)
    
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect("core:index")
        return super().dispatch(request, *args, **kwargs)


class UserProfileDetailEditView(LoginRequiredMixin, View):
    template_name = "user/profile.html"
    
    def get(self, request, *args, **kwargs):
        profile = get_object_or_404(Profile, user=request.user)
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=profile)
        context = {
            "user_form":user_form,
            "profile_form":profile_form,
            "profile":profile,
        }
        return render(request, self.template_name, context)
    
    def post(self, request, *args, **kwargs):
        profile = get_object_or_404(Profile, user=request.user)
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, request.FILES, instance=profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, "Profile Updated Successfully")
            return redirect("user:profile")
        context = {
            "user_form":user_form,
            "profile_form":profile_form,
            "profile":profile,
        }
        return render(request, self.template_name, context)

class PasswordChangeView(LoginRequiredMixin, SuccessMessageMixin, PasswordChangeView):
    template_name = "user/password_change.html"
    success_url = reverse_lazy("user:profile")
    success_message = "Password Change Successfull"
    


class BeacomeInstructor(LoginRequiredMixin, View):
    def post(self, request):
        user = request.user
        user.is_instructor = True
        user.save()
        messages.success(request, "You have successfull become a instructor")
        return redirect("core:index")
