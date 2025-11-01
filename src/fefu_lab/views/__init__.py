from .about import AboutView
from .course import CourseDetailView, course_list
from .custom_404 import custom_404
from .feedback import feedback
from .index import IndexView
from .registration import registration
from .student import StudentDetailView, student_list

__all__ = [
    "AboutView",
    "CourseDetailView",
    "IndexView",
    "StudentDetailView",
    "course_list",
    "custom_404",
    "feedback",
    "registration",
    "student_list",
]
