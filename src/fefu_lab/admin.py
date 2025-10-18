from django.contrib import admin

from fefu_lab.models import Course, Student, User

admin.site.register(Student)
admin.site.register(Course)
admin.site.register(User)
