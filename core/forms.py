from django import forms
from core.models import Course, Module


class CourseCreateForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['subject','title','slug','description','preview','level','duration']


class ModuleCreateForm(forms.ModelForm):
    class Meta:
        model = Module
        fields = ['title','description','order']