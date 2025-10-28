from django.contrib import admin

from fefu_lab.models import Course, Student, User


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


admin.site.register(Course)
admin.site.register(User)
