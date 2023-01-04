from django.contrib.auth.models import User
from .models import Rating
from profiles.models import Profile
from rest_framework import status
from rest_framework.test import APITestCase


class RatingListViewTests(APITestCase):
    def setUp(self):
        User.objects.create_user(username='owner1', password='dacapotestapi')
        User.objects.create_user(username='owner2', password='dacapotestapi')

    def test_can_view_rating(self):
        owner1 = User.objects.get(username='owner1')
        owner2 = Profile.objects.get(id=2)

        Rating.objects.create(
           id=1, owner=owner1, profile=owner2, rating=3)
        response = self.client.get('/rating/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_logged_in_user_can_rate_users(self):
        owner1 = User.objects.get(username='owner1')
        owner2 = User.objects.get(username='owner2')

        self.client.login(username='owner1', password='dacapotestapi')
        response = self.client.post(
            '/rating/', {'owner': owner1,
                         'profile': 2,
                         'rating': 3})
        count = Rating.objects.count()

        self.assertEqual(count, 1)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_user_not_logged_in_cant_rate_user(self):
        owner1 = User.objects.get(username='owner1')
        owner2 = User.objects.get(username='owner2')

        response = self.client.post(
            '/rating/', {'owner': owner1,
                         'profile': 2,
                         'rating': 3})

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class RatingDetailViewTests(APITestCase):
    def setUp(self):
        User.objects.create_user(username='owner1', password='dacapotestapi')
        User.objects.create_user(username='owner2', password='dacapotestapi')

        owner1 = User.objects.get(username='owner1')
        owner2 = Profile.objects.get(id=2)

        Rating.objects.create(
            owner=owner1, profile=owner2, rating=3)

    def test_user_logged_in_can_delete_rating(self):
        owner1 = User.objects.get(username='owner1')

        self.client.login(username='owner1', password='dacapotestapi')
        response = self.client.delete('/rating/1')

        self.assertEqual(
            response.status_code, status.HTTP_301_MOVED_PERMANENTLY)

    def test_user_logged_in_can_update_rating(self):
        owner1 = User.objects.get(username='owner1')
        owner2 = Profile.objects.get(id=2)

        self.client.login(username='owner1', password='dacapotestapi')
        response = self.client.put(
            '/rating/1/', {'owner': owner1,
                           'profile': 2,
                           'rating': 5})
        put_rating = Rating.objects.filter(pk=1).first()

        self.assertEqual(put_rating.rating, 5)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
