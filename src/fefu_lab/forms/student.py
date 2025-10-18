from typing import final

from django import forms

from fefu_lab.models import Student


@final
class StudentCreationForm(forms.ModelForm):
    name = forms.CharField(
        label="Имя студента:",
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Введите имя студента",
                "class": "form-input",
            },
        ),
    )

    @final
    class Meta:
        model = Student
        fields = ["name"]
