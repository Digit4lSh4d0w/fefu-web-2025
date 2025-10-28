from typing import final, override

from django.db import models
from django.urls import reverse


class AbstractUser(models.Model):
    """
    Класс абстрактного пользователя для определения конечных классов
    студента и преподавателя без повторения одних и тех же полей.
    """

    first_name = models.CharField(max_length=20, verbose_name="Имя")
    last_name = models.CharField(max_length=50, verbose_name="Фамилия")
    email = models.EmailField(max_length=50, unique=True, verbose_name="Email")
    birthday = models.DateField(null=True, blank=True, verbose_name="Дата рождения")
    is_active = models.BooleanField(default=True, verbose_name="Активен")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")

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

    def get_faculty_display_name(self):
        return self.FACULTY_CHOICES.get(self.faculty, "Неизвестно")


@final
class Teacher(AbstractUser):
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
        verbose_name = "Преподаватель"
        verbose_name_plural = "Преподаватели"
        db_table = "teachers"


@final
class Course(models.Model):
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
    is_active = models.BooleanField(default=True, verbose_name="Активен")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")

    @final
    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"
        ordering = ["title"]
        db_table = "courses"

    def __str__(self):
        return self.title


# Можно было использовать готовый класс из модуля Django.
@final
class User(models.Model):
    username = models.CharField(max_length=30)
    email = models.EmailField()
    # Я знаю, что пароли нужно солить и хэшировать,
    # например, с помощью pbkdf2 или argon2id.
    password = models.CharField(max_length=128)

    @override
    def __str__(self) -> str:
        return self.username
