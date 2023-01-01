from django.contrib.auth.models import User
from .models import Follower
from rest_framework import status
from rest_framework.test import APITestCase


class FollowerListViewTests(APITestCase):
    def setUp(self):
        User.objects.create_user(username='follower', password='dacapotestapi')
        User.objects.create_user(username='followed', password='dacapotestapi')

    def test_can_view_followers(self):
        following_user = User.objects.get(username='follower')
        followed_user = User.objects.get(username='followed')

        Follower.objects.create(owner=following_user,
                                followed_user=followed_user)
        response = self.client.get('/followers/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_logged_in_user_can_follow_users(self):
        following_user = User.objects.get(username='follower')
        followed_user = User.objects.get(username='followed')

        self.client.login(username='follower', password='dacapotestapi')
        response = self.client.post(
            '/followers/', {'owner': following_user.id,
                            'followed_user': followed_user.id})
        count = Follower.objects.count()

        self.assertEqual(count, 1)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_user_not_logged_in_cant_follow_user(self):
        following_user = User.objects.get(username='follower')
        followed_user = User.objects.get(username='followed')
        response = self.client.post(
            '/followers/', {'owner': following_user.id,
                            'followed_user': followed_user.id})

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class FollowerDetailViewTests(APITestCase):
    def setUp(self):
        User.objects.create_user(username='follower', password='dacapotestapi')
        User.objects.create_user(username='followed', password='dacapotestapi')

    def test_user_logged_in_can_unfollow_user(self):
        following_user = User.objects.get(username='follower')
        followed_user = User.objects.get(username='followed')

        self.client.login(username='follower', password='dacapotestapi')
        self.client.post(
            '/followers/', {'owner': following_user.id,
                            'followed_user': followed_user.id})
        response = self.client.delete('/followers/1')

        self.assertEqual(
            response.status_code, status.HTTP_301_MOVED_PERMANENTLY)
