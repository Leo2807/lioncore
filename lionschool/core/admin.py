from django.contrib import admin

from .models import Grade, Group, Pupil, Teacher, Warden, Course

for model in Grade, Group, Pupil, Teacher, Warden, Course:
    admin.site.register(model)
