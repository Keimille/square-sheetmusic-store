import unittest
import pathlib
import sys

from src.orders.order_allocation import Order, OrderItem, InvalidOrderItem

class TestOrder(unittest.TestCase):
    def setUp(self):
        self.order_items = [OrderItem("string-quartet-1", 1), OrderItem("piano-quintet", 1)]
        self.order = Order("John Doe", "fake_email@email.com", "order-123", self.order_items)

    def test_allocate(self):
        self.order = self.order.allocate(self.order_items[0])
        self.assertEqual(self.order.file_name, "string-quartet-1.pdf")

    def test_allocate_multiple_items(self):
        self.order = self.order.allocate(self.order_items[0])
        self.assertEqual(self.order.file_name, "string-quartet-1.pdf")
        self.order = self.order.allocate(self.order_items[1])
        self.assertEqual(self.order.file_name, "piano-quintet.pdf")

    def test_allocate_invalid_item(self):
        invalid_item = [OrderItem("invalid-sku", 1)]
        with self.assertRaises(InvalidOrderItem):
            self.order.allocate(invalid_item)

if __name__ == '__main__':
    unittest.main()