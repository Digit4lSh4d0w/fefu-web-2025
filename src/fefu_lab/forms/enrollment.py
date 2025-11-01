from typing import final

from django import forms

from fefu_lab.models import Course, Enrollment, Student


@final
class StudentEnrollmentForm(forms.ModelForm):
    student = forms.ModelChoiceField(
        queryset=Student.objects.all(),
        label="Студент:",
        required=True,
        initial=Student.objects.all()[0],
        widget=forms.Select(
            attrs={
                "class": "form-input",
            },
        ),
    )

    course = forms.ModelChoiceField(
        queryset=Course.objects.all(),
        label="Курс:",
        required=True,
        initial=Course.objects.all()[0],
        widget=forms.Select(
            attrs={
                "class": "form-input",
            },
        ),
    )

    @final
    class Meta:
        model = Enrollment
        fields = [
            "student",
            "course",
        ]

    def __init__(self, *args, student: Student | None = None, **kwargs):
        super().__init__(*args, **kwargs)
        if student:
            self.fields["student"].initial = student
            self.fields["student"].queryset = Student.objects.filter(pk=student.pk)
            self.fields["student"].disabled = True
        else:
            self.fields["student"].initial = Student.objects.all()[0]
            self.fields["student"].queryset = Student.objects.all()
            self.fields["student"].disabled = False

    def clean(self):
        cleaned_data = super().clean()

        student = cleaned_data.get("student")
        course = cleaned_data.get("course")

        if student and course:
            if Enrollment.objects.filter(student=student, course=course, is_active=True).exists():
                self.add_error("course", "Студент уже зачислен на курс")

        return cleaned_data
