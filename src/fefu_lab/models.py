from typing import final, override

from django.db import models
from django.urls import reverse


class AbstractModel(models.Model):
    """Абстрактная модель.

    Класс, содержащий часто используемые поля и методы.
    """

    is_active = models.BooleanField(default=True, verbose_name="Активен")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")

    class Meta:
        abstract = True

    @property
    def is_active_display(self):
        if self.is_active:
            return "Да"
        return "Нет"


class AbstractUser(AbstractModel):
    """Абстрактный пользователь.

    Класс абстрактного пользователя для определения конечных классов
    студента и преподавателя без повторения одних и тех же полей.
    """

    first_name = models.CharField(max_length=20, verbose_name="Имя")
    last_name = models.CharField(max_length=50, verbose_name="Фамилия")
    email = models.EmailField(max_length=50, unique=True, verbose_name="Email")
    birthday = models.DateField(null=True, blank=True, verbose_name="Дата рождения")

    class Meta:
        abstract = True
        ordering = ["last_name", "first_name"]

    def __str__(self):
        return f"{self.last_name} {self.first_name}"

    @property
    def full_name(self):
        return str(self)


@final
class Student(AbstractUser):
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
class Teacher(AbstractUser):
    @final
    class Meta:
        verbose_name = "Преподаватель"
        verbose_name_plural = "Преподаватели"
        db_table = "teachers"


@final
class Course(AbstractModel):
    title = models.CharField(max_length=200, unique=True, verbose_name="Название")
    slug = models.SlugField(max_length=200, unique=True, verbose_name="Машиночитаемое название")
    description = models.CharField(max_length=1500, verbose_name="Описание")
    duration = models.PositiveIntegerField(verbose_name="Продолжительность курса (в минутах)")
    teacher = models.ForeignKey(
        Teacher,
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
class Enrollment(AbstractModel):
    student = models.ForeignKey(
        Student,
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
