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
