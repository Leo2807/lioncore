from django.test import TestCase

from .models import Grade, Group, Pupil, Warden, Teacher
from django.contrib.auth.models import User


class GradeTest(TestCase):
    def test_correct_string_representation(self):
        name = "Grady McGradeface"
        grade = Grade(name=name)
        self.assertEqual(name, str(grade))


class GroupTest(TestCase):
    def test_correct_string_representation(self):
        name = "Groupy McGroupface"
        group = Group(name=name)
        self.assertEqual(name, str(group))


class UserExtension(TestCase):
    def correct_string_representation_factory(self, user_extension_class):
        username = "Yo momma {uec}".format(uec=user_extension_class)
        user = User.objects.create_user(username=username)
        user_extension = user_extension_class(user=user)
        self.assertEqual(username, user_extension.__str__())

    def test_correct_string_representation(self):
        for user_extension_class in {Pupil, Warden, Teacher}:
            self.correct_string_representation_factory(user_extension_class)
