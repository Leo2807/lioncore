from django.contrib import admin

from .models import Grade, Group, Pupil, Teacher, Warden

for model in {Grade, Group, Pupil, Teacher,  Warden}:
    admin.site.register(model)
