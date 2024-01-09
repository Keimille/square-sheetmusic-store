import unittest
import sys

class DigitalOrderAutomation(unittest.TestCase):
    def test_get_digital_item_from_order():
        order = Order(name="John Doe", email="fake_email@email.com", order_id="order-123",sku="string-quartet-1", qty=1)
        digital_item = OrderItem('order-id', sku="string-quartet-1", qty=1)
        
        order.allocate(digital_item)
        
        assert order.file_name == "string-quartet-1.pdf"