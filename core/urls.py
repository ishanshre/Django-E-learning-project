from django.urls import path
from core import views

app_name = "core"
urlpatterns = [
    path("", views.index, name="index"),
    path("courses/manage", views.ManageCourseListView.as_view(), name="manage_course_list"),
]