from typing import final

from django import forms

from fefu_lab.models import Course, Student, User


class StudentCreationForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ["name"]


class CourseCreationForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ["title", "slug"]


class FeedbackForm(forms.Form):
    name = forms.CharField(
        label="Имя",
        min_length=2,
        max_length=50,
        required=True,
        widget=forms.TextInput(attrs={"placeholder": "Введите ваше имя"}),
    )

    email = forms.EmailField(
        label="Email",
        required=True,
        widget=forms.EmailInput(attrs={"placeholder": "Введите ваш Email"}),
    )

    subject = forms.CharField(
        label="Тема сообщения",
        required=True,
        max_length=150,
        widget=forms.TextInput(attrs={"placeholder": "Введите тему сообщения"}),
    )

    message = forms.CharField(
        label="Текст сообщения",
        min_length=10,
        required=True,
        widget=forms.Textarea(attrs={"placeholder": "Введите текст сообщения"}),
    )


@final
class RegistrationForm(forms.ModelForm):  # pyright: ignore[reportMissingTypeArgument]
    username = forms.CharField(
        label="Имя пользователя",
        required=True,
        min_length=4,
        max_length=30,
        widget=forms.TextInput(attrs={"placeholder": "Введите ваше имя"}),
    )

    email = forms.EmailField(
        label="Email",
        required=True,
        widget=forms.EmailInput(attrs={"placeholder": "Введите ваш Email"}),
    )

    password = forms.CharField(
        label="Пароль",
        required=True,
        min_length=16,
        max_length=128,
        widget=forms.PasswordInput(attrs={"placeholder": "Придумайте пароль"}),
    )

    password_confirm = forms.CharField(
        label="Подтверждение пароля",
        required=True,
        min_length=16,
        max_length=128,
        widget=forms.PasswordInput(attrs={"placeholder": "Введите пароль снова"}),
    )

    @final
    class Meta:
        model = User
        fields = ["username", "email", "password"]

    def clean_username(self):
        username = self.cleaned_data.get("username")
        if User.objects.filter(username=username).exists():
            self.add_error("username", "Пользователь с таким именем пользователя уже существует")
        return username

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if User.objects.filter(email=email).exists():
            self.add_error("email", "Пользователь с таким Email уже существует")
        return email

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_confirm = cleaned_data.get("password_confirm")
        if password != password_confirm:
            self.add_error("password_confirm", "Пароли не совпадают")
        return cleaned_data
