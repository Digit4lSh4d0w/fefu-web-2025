from django import forms

from fefu_lab.models import Course, Student


class StudentCreationForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ["name"]


class CourseCreationForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ["title", "slug"]
