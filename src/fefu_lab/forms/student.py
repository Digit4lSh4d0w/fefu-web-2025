from typing import final

from django import forms

from fefu_lab.models import Student


@final
class StudentCreationForm(forms.ModelForm):
    first_name = forms.CharField(
        label="Имя студента:",
        required=True,
        min_length=3,
        max_length=20,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Введите имя студента",
                "class": "form-input",
            },
        ),
    )

    last_name = forms.CharField(
        label="Фамилия студента:",
        required=True,
        min_length=3,
        max_length=50,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Введите фамилию студента",
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
                "placeholder": "Введите почту студента",
                "class": "form-input",
            },
        ),
    )

    birthday = forms.DateField(
        label="День рождения:",
        widget=forms.TextInput(
            attrs={
                "placeholder": "Введите день рождения студента",
                "class": "form-input",
            },
        ),
    )

    faculty = forms.ChoiceField(
        label="Факультет:",
        choices=Student.FACULTY_CHOICES,
        widget=forms.Select(
            attrs={
                "class": "form-input",
            },
        ),
    )

    @final
    class Meta:
        model = Student
        fields = [
            "first_name",
            "last_name",
            "email",
            "birthday",
            "faculty",
        ]
