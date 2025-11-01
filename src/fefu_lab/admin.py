from django.contrib import admin

from fefu_lab.models import Course, Enrollment, Student, Teacher


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = [
        "last_name",
        "first_name",
        "email",
        "birthday",
        "faculty",
        "is_active",
    ]

    list_filter = [
        "faculty",
        "is_active",
    ]

    search_fields = [
        "first_name",
        "last_name",
        "email",
        "faculty",
    ]


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = [
        "last_name",
        "first_name",
        "email",
        "birthday",
        "is_active",
    ]

    list_filter = [
        "last_name",
        "first_name",
        "email",
        "is_active",
    ]

    search_fields = [
        "first_name",
        "last_name",
        "email",
    ]


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = [
        "title",
        "duration",
        "teacher",
        "is_active",
    ]

    list_filter = [
        "duration",
        "teacher",
        "is_active",
    ]

    search_fields = [
        "title",
        "duration",
        "teacher",
    ]


@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = [
        "course",
        "student",
        "is_active",
        "created_at",
    ]

    list_filter = [
        "course",
        "is_active",
        "student",
    ]

    search_fields = [
        "course",
        "student",
    ]
