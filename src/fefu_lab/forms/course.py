from typing import final

from django import forms

from fefu_lab.models import Course, TeacherProfile


@final
class CourseCreationForm(forms.ModelForm):
    title = forms.CharField(
        label="Название:",
        required=True,
        min_length=10,
        max_length=200,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Введите название курса",
                "class": "form-input",
            },
        ),
    )

    slug = forms.SlugField(
        label="Идентификатор:",
        required=True,
        min_length=10,
        max_length=200,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Введите идентификатор курса",
                "class": "form-input",
            },
        ),
    )

    description = forms.CharField(
        label="Описание:",
        max_length=1500,
        widget=forms.Textarea(
            attrs={
                "placeholder": "Введите описание курса",
                "class": "form-input",
            },
        ),
    )

    duration = forms.IntegerField(
        label="Продолжительность:",
        required=True,
        # ~ 1 неделя с занятиями по 3 часа в день
        min_value=900,
        # ~ 6 месяцев с занятиями по 3 часа в день
        max_value=21600,
        initial=900,
        widget=forms.NumberInput(
            attrs={
                "placeholder": "Введите продолжительность курса (в минутах)",
                "class": "form-input",
            },
        ),
    )

    @final
    class Meta:
        model = Course
        fields = [
            "title",
            "slug",
            "description",
            "duration",
        ]
