from django.test import TestCase


class TestCheckoutViews(TestCase):

    def test_get_checkout_with_empty_bag(self):

        response = self.client.get('/checkout')
        self.assertTrue(response, '/products')
