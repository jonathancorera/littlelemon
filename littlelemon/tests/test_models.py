from django.test import TestCase
from decimal import Decimal
from restaurant.models import Menu



class MenuTest(TestCase):

    def test_create_item(self):
        item = Menu.objects.create(title="IceCream", price=Decimal('80'), inventory=100)
        self.assertEqual(str(item), "IceCream : 80")




