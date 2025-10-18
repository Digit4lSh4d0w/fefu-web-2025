from typing import final

from django import forms

from fefu_lab.models import Course


@final
class CourseCreationForm(forms.ModelForm):
    title = forms.CharField(
        label="Название курса:",
        required=True,
        max_length=200,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Введите название курса",
                "class": "form-input",
            },
        ),
    )

    slug = forms.SlugField(
        label="Идентификатор курса:",
        required=True,
        max_length=200,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Введите идентификатор курса",
                "class": "form-input",
            },
        ),
    )

    @final
    class Meta:
        model = Course
        fields = ["title", "slug"]
