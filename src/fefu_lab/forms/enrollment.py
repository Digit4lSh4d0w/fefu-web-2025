from typing import final

from django import forms

from fefu_lab.models import Course, Enrollment, StudentProfile


@final
class StudentEnrollmentForm(forms.ModelForm):
    student = forms.ModelChoiceField(
        queryset=StudentProfile.objects.all(),
        label="Студент:",
        required=True,
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

    def __init__(
        self,
        *args,
        student: StudentProfile | None = None,
        course: Course | None = None,
        **kwargs,
    ):
        super().__init__(*args, **kwargs)

        if student:
            self.fields["student"].initial = student
            self.fields["student"].queryset = StudentProfile.objects.filter(
                pk=student.pk
            )
            self.fields["student"].disabled = True
        else:
            self.fields["student"].initial = StudentProfile.objects.first()
            self.fields["student"].queryset = StudentProfile.objects.all()
            self.fields["student"].disabled = False

        if course:
            self.fields["course"].initial = course
            self.fields["course"].queryset = Course.objects.filter(pk=course.pk)
            self.fields["course"].disabled = True
        else:
            self.fields["course"].initial = Course.objects.first()
            self.fields["course"].queryset = Course.objects.all()
            self.fields["course"].disabled = False

    def clean(self):
        cleaned_data = super().clean()

        student = cleaned_data.get("student")
        course = cleaned_data.get("course")

        if (
            student
            and course
            and Enrollment.objects.filter(
                student=student, course=course, is_active=True
            ).exists()
        ):
            self.add_error("course", "Студент уже зачислен на курс")

        return cleaned_data
