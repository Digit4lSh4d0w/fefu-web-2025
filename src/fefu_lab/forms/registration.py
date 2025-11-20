from typing import final

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from fefu_lab.models import StudentProfile


@final
class RegistrationForm(UserCreationForm):
    ROLE_CHOICES = {
        "student": "Студент",
        "teacher": "Преподаватель",
    }

    username = forms.CharField(
        label="Логин:",
        required=True,
        min_length=3,
        max_length=20,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Придумайте логин",
                "class": "form-input",
            },
        ),
    )

    email = forms.EmailField(
        label="Почта:",
        required=True,
        max_length=50,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Введите вашу почту",
                "class": "form-input",
            },
        ),
    )

    first_name = forms.CharField(
        label="Имя:",
        required=True,
        min_length=3,
        max_length=20,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Введите ваше имя",
                "class": "form-input",
            },
        ),
    )

    last_name = forms.CharField(
        label="Фамилия:",
        required=True,
        min_length=3,
        max_length=50,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Введите вашу фамилию",
                "class": "form-input",
            },
        ),
    )

    password1 = forms.CharField(
        label="Пароль:",
        required=True,
        min_length=3,
        max_length=50,
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Введите пароль",
                "class": "form-input",
            },
        ),
    )

    password2 = forms.CharField(
        label="Повторите пароль:",
        required=True,
        min_length=3,
        max_length=50,
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Введите пароль",
                "class": "form-input",
            },
        ),
    )

    birthday = forms.DateField(
        label="День рождения:",
        widget=forms.TextInput(
            attrs={
                "placeholder": "Введите ваш день рождения",
                "class": "form-input",
            },
        ),
    )

    role = forms.ChoiceField(
        label="Регистрация в качестве:",
        choices=ROLE_CHOICES,
        widget=forms.RadioSelect(
            attrs={
                "class": "form-input",
            },
        ),
    )

    faculty = forms.ChoiceField(
        label="Факультет:",
        choices=StudentProfile.FACULTY_CHOICES,
        widget=forms.Select(
            attrs={
                "class": "form-input",
            },
        ),
    )

    @final
    class Meta:
        model = User
        fields = [
            "username",
            "email",
            "first_name",
            "last_name",
            "password1",
            "password2",
        ]

    def clean(self):
        cleaned_data = super().clean()
        role = cleaned_data.get("role")

        if role == "student" and not cleaned_data.get("faculty"):
            self.add_error("faculty", "Студент должен выбрать факультет")
