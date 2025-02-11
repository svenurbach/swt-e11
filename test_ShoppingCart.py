import unittest
from ShoppingCart import ShoppingCart


class ShoppingCartTest(unittest.TestCase):

    def setUp(self):
        self.cart = ShoppingCart()

    def tearDown(self):
        print(self.cart.items)

    def test_empty_cart_has_zero_total(self):
        self.assertEqual(self.cart.get_total(), 0)

    def test_add_item_increases_total(self):
        self.cart.add_item('Monitor', 500)
        self.assertEqual(self.cart.get_total(), 500)

    def test_add_multiple_items_sums_total(self):
        self.cart.add_item('Maus',20)
        self.cart.add_item('Tastatur', 40)
        self.cart.add_item('HDMI-Kabel', 10)
        self.assertEqual(self.cart.get_total(), 70)

    def test_get_quantity_of_items(self):
        self.cart.add_item('Laptop', 5)
        self.cart.add_item('Laptop', 2000)
        self.assertEqual(self.cart.get_quantity('Laptop'), 2)

    def test_remove_item(self):
        self.cart.add_item('Laptop', 2000)
        self.cart.add_item('Maus', 20)
        self.cart.remove_item('Laptop')
        self.assertEqual(self.cart.get_quantity('Laptop'), 0)

    def test_add_item_with_negative_price(self):
        self.assertRaises(ValueError, self.cart.add_item, 'Banane', -2)


if __name__ == '__main__':
    unittest.main()
