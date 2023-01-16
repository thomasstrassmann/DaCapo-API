from django.contrib.auth.models import User
from .models import Instrument
from rest_framework import status
from rest_framework.test import APITestCase


class InstrumentListViewTests(APITestCase):
    def setUp(self):
        User.objects.create_user(username='test', password='dacapotestapi')

    def test_can_view_instruments(self):
        test = User.objects.get(username='test')
        Instrument.objects.create(owner=test, title='an instrument')
        response = self.client.get('/instruments/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_logged_in_user_can_create_instrument(self):
        self.client.login(username='test', password='dacapotestapi')
        response = self.client.post(
            '/instruments/', {'title': 'an instrument',
                              'brand': 'test brand'})
        count = Instrument.objects.count()

        self.assertEqual(count, 1)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_user_not_logged_in_cant_create_instrument(self):
        response = self.client.post('/instruments/',
                                    {'title': 'an instrument'})

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class InstrumentDetailViewTests(APITestCase):
    def setUp(self):
        owner1 = User.objects.create_user(
            username='owner1', password='newpassword')
        owner2 = User.objects.create_user(
            username='owner2', password='newpassword')

        Instrument.objects.create(
            owner=owner1, title='an instrument', description='owner1 item'
        )

        Instrument.objects.create(
            owner=owner2, title='another instrument', description='owner2 item'
        )

    def test_can_get_item_using_valid_id(self):
        response = self.client.get('/instruments/1/')

        self.assertEqual(response.data['title'], 'an instrument')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_cant_get_item_using_invalid_id(self):
        response = self.client.get('/instrument/1024/')

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_user_can_update_own_item(self):
        self.client.login(username='owner1', password='newpassword')
        response = self.client.put(
            '/instruments/1/', {'title': 'a brand new instrument',
                                'brand': 'test brand'})
        instrument = Instrument.objects.filter(pk=1).first()

        self.assertEqual(instrument.title, 'a brand new instrument')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_cant_update_foreign_item(self):
        self.client.login(username='owner1', password='newpassword')
        response = self.client.put(
            '/instruments/2/', {'title': 'forbidden action'})

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
