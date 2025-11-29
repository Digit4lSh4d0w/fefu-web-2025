from django.contrib import admin

from fefu_lab.models import Course, Enrollment, StudentProfile, TeacherProfile


@admin.register(StudentProfile)
class StudentAdmin(admin.ModelAdmin):
    list_display = [
        "user",
        "faculty",
        "is_active",
        "created_at",
        "updated_at",
        "deleted_at",
    ]

    list_filter = [
        "user",
        "faculty",
        "is_active",
    ]

    search_fields = [
        "user",
        "faculty",
    ]


@admin.register(TeacherProfile)
class TeacherAdmin(admin.ModelAdmin):
    list_display = [
        "user",
        "is_active",
        "created_at",
        "updated_at",
        "deleted_at",
    ]

    list_filter = [
        "user",
        "is_active",
    ]

    search_fields = [
        "user",
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
