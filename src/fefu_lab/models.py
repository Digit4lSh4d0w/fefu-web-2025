from typing import final, override

from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=100)
    enrollment_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name


class Course(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

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
