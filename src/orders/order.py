from dataclasses import dataclass

class InvalidOrderItem(Exception):
    pass

@dataclass(frozen=True)
class Order:
    name: str
    email: str
    order_id: str
    sku: str
    qty: int
    file_name: str = None

    def allocate(self, item: 'OrderItem'):
        if self.sku == item.sku and self.qty == item.qty:
            return Order(self.name, self.email, self.order_id, self.sku, self.qty, f"{self.sku}.pdf")
        else:
            raise InvalidOrderItem("Item does not match order")
    
    def __repr__(self):
        return f"Order(name={self.name}, email={self.email}, order_id={self.order_id}, sku={self.sku}, qty={self.qty}, file_name={self.file_name})"

@dataclass(frozen=True)
class OrderItem:
    sku: str
    qty: int        

myOrderItem = OrderItem("string-quartet-1", 1)

# Creating an instance of Order
myOrder = Order("John Doe", "fake_email@email.com", "order-123", "string-quartet-1", 1)

# Allocating the order item to the order
myOrder.allocate(myOrderItem)

print(myOrder)