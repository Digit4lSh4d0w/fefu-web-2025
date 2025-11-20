from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from fefu_lab import views

app_name = "fefu_lab"
urlpatterns = [
    # Root
    path("", views.IndexView.as_view(), name="index"),
    # Login / Logout
    path(
        "login/",
        LoginView.as_view(template_name="fefu_lab/auth/login.html"),
        name="login",
    ),
    path("logout/", LogoutView.as_view(), name="logout"),
    # Registration
    path("registration/", views.registration, name="registration"),
    # Profile
    path("profile/", views.ProfileView.as_view(), name="profile"),
    # About
    path("about/", views.AboutView.as_view(), name="about"),
    # Students
    path("students/", views.student_list, name="students_list"),
    path("student/<int:pk>/", views.StudentDetailView.as_view(), name="student_detail"),
    # Courses
    path("courses/", views.course_list, name="courses_list"),
    path("course/<slug:slug>/", views.CourseDetailView.as_view(), name="course_detail"),
    # Feedback
    path("feedback/", views.feedback, name="feedback"),
]
