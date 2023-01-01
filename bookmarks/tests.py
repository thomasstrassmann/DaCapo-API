from django.contrib.auth.models import User
from .models import Bookmark
from instruments.models import Instrument
from rest_framework import status
from rest_framework.test import APITestCase


class BookmarkListViewTests(APITestCase):
    def setUp(self):
        User.objects.create_user(username='test', password='dacapotestapi')
        User.objects.create_user(username='creator', password='dacapotestapi')

    def test_can_view_bookmarks(self):
        test = User.objects.get(username='test')
        Instrument.objects.create(owner=test, title='an instrument')
        bookmarked_instrument = Instrument.objects.get(title="an instrument")
        Bookmark.objects.create(owner=test, instrument=bookmarked_instrument)
        response = self.client.get('/bookmarks/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_logged_in_user_can_create_bookmark(self):
        self.client.login(username='test', password='dacapotestapi')
        creator = User.objects.get(username='creator')
        Instrument.objects.create(owner=creator, title='an instrument')
        response = self.client.post(
            '/bookmarks/', {'instrument': 1})
        count = Bookmark.objects.count()

        self.assertEqual(count, 1)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_user_not_logged_in_cant_create_bookmark(self):
        response = self.client.post('/bookmarks/',
                                    {'title': 'an instrument'})

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_user_logged_in_can_delete_bookmark(self):
        test = User.objects.get(username='test')
        creator = User.objects.get(username='creator')
        Instrument.objects.create(owner=creator, title='an instrument')

        self.client.login(username='test', password='dacapotestapi')
        self.client.post('/bookmarks/', {'title': 'an instrument'})
        response = self.client.delete('/bookmarks/1')

        self.assertEqual(
            response.status_code, status.HTTP_301_MOVED_PERMANENTLY)
