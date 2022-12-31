from django.shortcuts import render, redirect

from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin

from django.contrib.auth.views import LoginView

from django.views.generic.edit import CreateView

from django.urls import reverse, reverse_lazy

from user.forms import CustomUserCreationForm, LoginUserForm
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