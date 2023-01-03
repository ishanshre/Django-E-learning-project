from django.urls import path
from core import views

app_name = "core"
urlpatterns = [
    path("", views.index, name="index"),
    path("courses/manage", views.ManageCourseListView.as_view(), name="manage_course_list"),
    path("subjects/<slug:slug>", views.SubjectDetailView.as_view(), name="subject_detail"),
    path("courses/<slug:slug>", views.CourseDetailView.as_view(), name="course_detail"),
]