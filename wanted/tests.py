from django.contrib.auth.models import User
from .models import Wanted
from rest_framework import status
from rest_framework.test import APITestCase


class WantedListViewTests(APITestCase):
    def setUp(self):
        User.objects.create_user(username='test', password='dacapotestapi')

    def test_can_view_wanted(self):
        test = User.objects.get(username='test')
        Wanted.objects.create(owner=test, title='an instrument')
        response = self.client.get('/wanted/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_logged_in_user_can_create_wanted(self):
        self.client.login(username='test', password='dacapotestapi')
        response = self.client.post(
            '/wanted/', {'title': 'an instrument'})
        count = Wanted.objects.count()

        self.assertEqual(count, 1)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_user_not_logged_in_cant_create_wanted(self):
        response = self.client.post('/wanted/',
                                    {'title': 'an instrument'})

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class WantedDetailViewTests(APITestCase):
    def setUp(self):
        owner1 = User.objects.create_user(
            username='owner1', password='newpassword')
        owner2 = User.objects.create_user(
            username='owner2', password='newpassword')

        Wanted.objects.create(
            owner=owner1, title='an instrument', description='owner1 item'
        )

        Wanted.objects.create(
            owner=owner2, title='another instrument', description='owner2 item'
        )

    def test_can_get_wanted_using_valid_id(self):
        response = self.client.get('/wanted/1/')

        self.assertEqual(response.data['title'], 'an instrument')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_cant_get_wanted_using_invalid_id(self):
        response = self.client.get('/wanted/903/')

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_user_can_update_own_wanted(self):
        self.client.login(username='owner1', password='newpassword')
        response = self.client.put(
            '/wanted/1/', {'title': 'a brand new item'})
        wanted = Wanted.objects.filter(pk=1).first()

        self.assertEqual(wanted.title, 'a brand new item')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_cant_update_foreign_wanted(self):
        self.client.login(username='owner1', password='newpassword')
        response = self.client.put(
            '/wanted/2/', {'title': 'forbidden action'})

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
