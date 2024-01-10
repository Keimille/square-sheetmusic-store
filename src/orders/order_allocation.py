from dataclasses import dataclass

class InvalidOrderItem(Exception):
    pass

@dataclass(frozen=True)
class OrderItem:
    sku: str
    qty: int 

@dataclass(frozen=True)
class Order:
    name: str
    email: str
    order_id: str
    items: list[OrderItem]
    file_name: str = None

    def allocate(self, item: 'OrderItem'):
        if item in self.items:
            return Order(self.name, self.email, self.order_id, self.items, f"{item.sku}.pdf")
        else:
            raise InvalidOrderItem("Item does not match order")
    
    def __repr__(self):
        return f"Order(name={self.name}, email={self.email}, order_id={self.order_id}, items={self.items}, file_name={self.file_name})"

#myOrderItem = OrderItem("string-quartet-1", 1)

# Creating an instance of Order
#myOrder = Order("John Doe", "fake_email@email.com", "order-123", "string-quartet-1", 1)

# Allocating the order item to the order
#print(myOrder.allocate(myOrderItem))

