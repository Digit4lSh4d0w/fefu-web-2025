from django import forms

from fefu_lab.models import Student


class StudentCreationForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ["name"]
