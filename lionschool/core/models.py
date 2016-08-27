from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from django.utils.translation import pgettext_lazy


class UserExtension(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, models.CASCADE)

    def __str__(self):
        return self.user.__str__()

    class Meta:
        abstract = True


class Pupil(UserExtension):
    grade = models.ForeignKey('Grade', verbose_name=_("grade"), blank=True)
    group = models.ForeignKey('Group', verbose_name=_("group"), blank=True)
    wardens = models.ManyToManyField(
        'Warden', verbose_name=_("wardens"), blank=True
    )

    class Meta:
        verbose_name = _("pupil")
        verbose_name_plural = _("pupils")


class Teacher(UserExtension):
    diplomas = models.TextField(_("diplomas"), blank=True)

    class Meta:
        verbose_name = _("teacher")
        verbose_name_plural = _("teachers")


class Warden(UserExtension):

    class Meta:
        verbose_name = _("warden")
        verbose_name_plural = _("wardens")


class NamedOption(models.Model):
    name = models.CharField(_("name"), max_length=30, primary_key=True)

    def __str__(self):
        return str(self.name)

    class Meta:
        abstract = True


class Grade(NamedOption):
    class Meta:
        verbose_name = _("grade")
        verbose_name_plural = _("grades")


class Group(NamedOption):
    class_teacher = models.ManyToManyField(
        Teacher, verbose_name=_("class teacher"), blank=True
    )

    class Meta:
        verbose_name = pgettext_lazy("group", "synonym: class")
        verbose_name_plural = pgettext_lazy("groups", "synonym: classes")


class Course(models.Model):
    name = models.CharField(_("name"), max_length=150)

    teachers = models.ManyToManyField(
        Teacher, verbose_name=_("teachers"), blank=True
    )

    groups = models.ManyToManyField(
        Group,
        verbose_name=pgettext_lazy("groups", "synonym: classes"),
        blank=True
    )

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = _("course")
        verbose_name_plural = _("courses")
