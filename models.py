from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

class Pupil(User):
    grade = models.ForeignKey('Grade', verbose_name=_("grade"))
    group = models.ForeignKey('Group', verbose_name=_("group"))
    wardens = models.ManyToManyField('Warden', verbose_name=_("wardens"))

class Teacher(User):
    diplomas = models.TextField(_("diplomas"))

class Warden(User):
    pass

class NamedOption(models.Model):
    name = models.CharField(_("name"), max_length=30, primary_key=True)

    class Meta:
        abstract = True

class Grade(NamedOption):
    class Meta:
        verbose_name = _("grade")
        verbose_name_plural = _("grades")

class Group(NamedOption):
    class_teacher = models.ManyToManyField(Teacher, verbose_name=_("class teacher"))
    class Meta:
        verbose_name = _("group")
        verbose_name_plural = _("groups")
