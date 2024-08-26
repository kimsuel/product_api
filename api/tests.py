from django.test import TestCase
from rest_framework import status

from api.models import Product


class ProductTestCase(TestCase):
    def setUp(self):
        self.product_1 = Product.objects.create(name='샴푸', price=10000, quantity=500)
        self.product_2 = Product.objects.create(name='가방', price=20000, quantity=200)
        self.product_3 = Product.objects.create(name='책상', price=155000, quantity=50)

    def test_product_list(self):
        response = self.client.get('/api/products')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response_data = response.json()
        self.assertEqual(len(response_data), Product.objects.count())

    def test_product_retrieve(self):
        response = self.client.get(f'/api/products/{self.product_1.id}')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response_data = response.json()
        self.assertEqual(response_data['name'], self.product_1.name)

    def test_product_create(self):
        response = self.client.post(f'/api/products', data={
            'name': '곰돌이 인형',
            'price': 5000,
            'quantity': 5000
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        response_data = response.json()
        self.assertEqual(response_data['name'], '곰돌이 인형')

    def test_product_update(self):
        response = self.client.patch(f'/api/products/{self.product_1.id}',
                                   data={'price': 15000, 'quantity': 300},
                                   content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response_data = response.json()
        self.assertEqual(response_data['price'], 15000)

    def test_product_delete(self):
        response = self.client.delete(f'/api/products/{self.product_1.id}')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        self.assertEqual(Product.objects.count(), 2)