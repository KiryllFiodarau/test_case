from http import HTTPStatus
from django.test import TestCase
from django.test.client import Client
from decouple import config

from users.models import Users


class UsersTests(TestCase):
    def setUp(self):
        self.c = Client()
        self.data = {
            'first_name': 'test_post',
            'last_name': 'test_post',
            'mail': 'test_post@mail.ru',
        }
        self.user = Users(first_name='test', last_name='test', mail='test@mail.ru')
        self.user.save()

    def test_get_user_by_id(self):
        response = self.c.get("/api/users/%s" % self.user.pk)

        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(response.context['user'], self.user)

    def test_register_user(self):
        self.c.post("/%s" % config('UNIQUE_STR'), data=self.data)
        try:
            user = Users.objects.get(first_name=self.data['first_name'])
        except Users.DoesNotExist:
            user = None

        self.assertIsInstance(user, Users)
