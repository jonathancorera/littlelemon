from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework import status


from restaurant.models import Menu
from restaurant.serializers import MenuSerializer


class MenuViewTest(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        self.pizza = Menu.objects.create(title='Pizza', price=12.99, inventory=10)
        self.burger = Menu.objects.create(title='Burger', price=8.99, inventory=5)
        self.pasta = Menu.objects.create(title='Pasta', price=15.99, inventory=7)

    def loginAsTestUser(self) -> None:
        self.client.login(username='testuser', password='Password123?')

    def test_getall(self):
        self.loginAsTestUser()
        response = self.client.get('restaurant/menu')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        menu = Menu.objects.all()
        serializer = MenuSerializer(menu, many=True)
        self.assertEqual(response.data, serializer.data)