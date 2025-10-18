from django import forms

from fefu_lab.models import Course


class CourseCreationForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ["title", "slug"]
