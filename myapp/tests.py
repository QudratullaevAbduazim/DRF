from django.test import TestCase
from .models import Products

class ProductModelTest(TestCase):

    def setUp(self):
        self.product = Products.objects.create(
            name="Test Product",
            description="Test description",
            price=100.00,
            stock=10
        )

    def test_product_creation(self):
        self.assertEqual(self.product.name, "Test Product")
        self.assertEqual(self.product.price, 100.00)
        self.assertEqual(self.product.stock, 10)