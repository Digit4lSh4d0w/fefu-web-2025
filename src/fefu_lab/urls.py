from django.urls import path

from fefu_lab import views

app_name = "fefu_lab"
urlpatterns = [
    # Root
    path("", views.index, name="index"),
    # About
    path("about/", views.AboutView.as_view(), name="about"),
    # Students
    path("students/", views.student_list, name="student_list"),
    path("students/<int:pk>/", views.StudentDetailView.as_view(), name="student_detail"),
    # Courses
    path("courses/", views.course_list, name="course_list"),
    path("courses/<slug:slug>/", views.CourseDetailView.as_view(), name="course_detail"),
    # Feedback
    path("feedback/", views.feedback, name="feedback"),
    # Registration
    path("registration/", views.registration, name="registration"),
]
