from typing import final

from django import forms

from fefu_lab.models import TeacherProfile


@final
class TeacherRegistrationForm(forms.ModelForm):
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

    birthday = forms.DateField(
        label="День рождения:",
        widget=forms.TextInput(
            attrs={
                "placeholder": "Введите ваш день рождения",
                "class": "form-input",
            },
        ),
    )

    @final
    class Meta:
        model = TeacherProfile
        fields = [
            "first_name",
            "last_name",
            "email",
            "birthday",
        ]
