from typing import final

from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class CustomAbstractModel(models.Model):
    """Абстрактная модель.

    Класс, содержащий часто используемые поля и методы.
    """

    is_active = models.BooleanField(default=True, verbose_name="Активен")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")
    deleted_at = models.DateTimeField(
        null=True, blank=True, verbose_name="Дата удаления"
    )

    class Meta:
        abstract = True

    @property
    def is_active_display(self):
        if self.is_active:
            return "Да"
        return "Нет"


class CustomAbstractUser(CustomAbstractModel):
    """Абстрактный пользователь.

    Класс абстрактного пользователя для определения конечных классов
    студента и преподавателя без повторения одних и тех же полей.
    """

    user = models.OneToOneField(
        User, on_delete=models.CASCADE, verbose_name="Пользователь"
    )
    birthday = models.DateField(null=True, blank=True, verbose_name="Дата рождения")

    class Meta:
        abstract = True

    @property
    def first_name_display(self) -> str:
        return self.user.first_name

    @property
    def last_name_display(self) -> str:
        return self.user.last_name

    @property
    def full_name_display(self):
        return f"{self.last_name_display} {self.first_name_display}"

    def __str__(self):
        return self.full_name_display


@final
class StudentProfile(CustomAbstractUser):
    FACULTY_CHOICES = {
        "CS": "Кибербезопасность",
        "SE": "Программная инженерия",
        "IT": "Информационные технологии",
        "DS": "Наука о данных",
        "WEB": "Веб-технологии",
    }

    faculty = models.CharField(
        max_length=4,
        choices=FACULTY_CHOICES,
        default="CS",
        verbose_name="Факультет",
    )

    @final
    class Meta:
        verbose_name = "Студент"
        verbose_name_plural = "Студенты"
        db_table = "students"

    def get_absolute_url(self):
        return reverse("student_detail", kwargs={"pk": self.pk})

    def faculty_display(self):
        return self.FACULTY_CHOICES.get(self.faculty, "Неизвестно")


@final
class TeacherProfile(CustomAbstractUser):
    @final
    class Meta:
        verbose_name = "Преподаватель"
        verbose_name_plural = "Преподаватели"
        db_table = "teachers"


@final
class Course(CustomAbstractModel):
    title = models.CharField(max_length=200, unique=True, verbose_name="Название")
    slug = models.SlugField(
        max_length=200, unique=True, verbose_name="Машиночитаемое название"
    )
    description = models.CharField(max_length=1500, verbose_name="Описание")
    duration = models.PositiveIntegerField(
        verbose_name="Продолжительность курса (в минутах)"
    )
    teacher = models.ForeignKey(
        TeacherProfile,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        verbose_name="Преподаватель",
    )

    @final
    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"
        ordering = ["title"]
        db_table = "courses"

    def __str__(self):
        return self.title

    @property
    def teacher_display(self):
        if self.teacher:
            return str(self.teacher)
        return "Преподаватель не назначен"


@final
class Enrollment(CustomAbstractModel):
    student = models.ForeignKey(
        StudentProfile,
        on_delete=models.CASCADE,
        verbose_name="Студент",
    )
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        verbose_name="Курс",
    )

    @final
    class Meta:
        verbose_name = "Зачисление"
        verbose_name_plural = "Зачисления"
        ordering = ["course", "is_active", "student"]
        db_table = "enrollments"

    def __str__(self):
        return str(self.course)


def get_user_role(user):
    """Возвращает роль пользователя по активному профилю."""
    try:
        if user.studentprofile.is_active:
            return "student"
    except Exception:
        pass

    try:
        if user.teacherprofile.is_active:
            return "teacher"
    except Exception:
        pass

    return None


def get_user_profile(user):
    """Возвращает активный профиль пользователя по роли."""
    role = get_user_role(user)
    if role == "student":
        return user.studentprofile
    elif role == "teacher":
        return user.teacherprofile
    return None
