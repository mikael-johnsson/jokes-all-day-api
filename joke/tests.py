from django.contrib.auth.models import User
from .models import Joke
from rest_framework import status
from rest_framework.test import APITestCase

class JokeListViewTests(APITestCase):
    """
    To test the JokeList view
    setUp creates the user
    Joke.objects.create creates a joke
    """
    def setUp(self):
        User.objects.create_user(username="adam", password="password")
    
    def test_can_list_jokes(self):
        adam = User.objects.get(username="adam")
        Joke.objects.create(author=adam, title="A test title")
        response = self.client.get('/jokes/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print(response.data)
        print(len(response.data))

    def test_logged_in_user_can_create_post(self):
        self.client.login(username="adam", password="password")
        response = self.client.post("/jokes/", {"title": "a title", "content": "this is content"})
        count = Joke.objects.count()
        self.assertEqual(count, 1)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    # Why doesnt this work?
    def test_user_not_logged_in_cant_create_post(self):
        response = self.client.post("/jokes/", {"title": "a title", "content": "this is content"})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

