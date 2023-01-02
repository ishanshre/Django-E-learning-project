from django.shortcuts import render
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin

from core.models import Course


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
    