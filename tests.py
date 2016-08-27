from django.test import TestCase

from .models import Grade, Group


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
