from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin

from core.models import Course, Subject


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
