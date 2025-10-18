from django import forms


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
