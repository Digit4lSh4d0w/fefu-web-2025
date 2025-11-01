from typing import final

from django import forms

from fefu_lab.models import User


@final
class RegistrationForm(forms.Form):
    ROLE_CHOICES = {
        "student": "Студент",
        "teacher": "Преподаватель",
    }

    role = forms.ChoiceField(
        label="Регистрация в качестве:",
        choices=ROLE_CHOICES,
        widget=forms.RadioSelect(
            attrs={
                "class": "form-input",
            },
        ),
    )
