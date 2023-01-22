from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy

from core.models import Course, Subject, Module
from core.forms import CourseCreateForm, ModuleCreateForm


# Create your views here.
def index(request):
    return render(request, "index.html")


class ManageCourseListView(LoginRequiredMixin, ListView):
    model = Course
    context_object_name = "my_courses"
    template_name = "courses/manage/course/list.html"

    def get_queryset(self):
        query = super().get_queryset()
        return query.filter(owner=self.request.user)


class SubjectDetailView(DetailView):
    model = Subject
    context_object_name = "subject"
    template_name = "subjects/subject.html"

    def get_queryset(self):
        return Subject.objects.filter(slug=self.kwargs['slug'])


class CourseDetailView(DetailView):
    model = Course
    context_object_name = "course"
    template_name = "courses/course_detail.html"

    def get_queryset(self):
        return Course.objects.filter(slug=self.kwargs['slug'])


class CourseCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Course
    form_class = CourseCreateForm
    template_name = "courses/manage/course/create_course.html"
    success_url = reverse_lazy("core:manage_course_list")
    success_message = "Course Added"

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super(CourseCreateView, self).form_valid(form)


class ModuleCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Module
    form_class = ModuleCreateForm
    template_name = "courses/partials/module_add.html"
    success_message = "Module Added"

    def form_valid(self, form):
        course = Course.objects.get(slug=self.kwargs['course_slug'])
        form.instance.course = course
        return super().form_valid(form)
    
    def get_success_url(self) -> str:
        return reverse_lazy('core:course_detail', args=[self.kwargs['course_slug']])