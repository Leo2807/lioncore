from django.test import TestCase

from .models import Grade, Group, Pupil, Warden, Teacher
from django.contrib.auth.models import User


class NamedOptionTest(TestCase):
    def correct_string_representation_factory(self, named_option_class):
        name = "{noc}y Mc{noc}face".format(noc=named_option_class)
        named_option = named_option_class(name=name)
        self.assertEqual(name, str(named_option))

    def test_correct_string_representation(self):
        for named_option_class in Grade, Group:
            self.correct_string_representation_factory(named_option_class)


class UserExtensionTest(TestCase):
    def correct_string_representation_factory(self, user_extension_class):
        username = "Yo momma {uec}".format(uec=user_extension_class)
        user = User.objects.create_user(username=username)
        user_extension = user_extension_class(user=user)
        self.assertEqual(username, str(user_extension))

    def test_correct_string_representation(self):
        for user_extension_class in Pupil, Warden, Teacher:
            self.correct_string_representation_factory(user_extension_class)
