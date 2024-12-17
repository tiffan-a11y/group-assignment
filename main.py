from abc import ABC, abstractmethod

class User:
    def __init__(self, user_id, user_name):
        self.user_id = user_id
        self.user_name = user_name

    def register_user(self):
        print(f"User '{self.user_name}' registered successfully.")

    def login(self):
        print(f"User '{self.user_name}' logged in successfully.")

    def logout(self):
        print(f"User '{self.user_name}' logged out.")

    def delete_account(self):
        print(f"User '{self.user_name}' account deleted.")


# Order Class (Abstract) 
class Order(ABC):
    def __init__(self, order_id, customer_name, restaurant_name, items, delivery_address):
        self.order_id = order_id
        self.customer_name = customer_name
        self.restaurant_name = restaurant_name
        self.items = items
        self.delivery_address = delivery_address
        self.order_status = "Pending"

    @abstractmethod
    def process_order(self):
        pass

# Payment Class (Inherits Order)
class Payment(Order):
    def __init__(self, order_id, customer_name, restaurant_name, items, delivery_address, payment_method):
        super().__init__(order_id, customer_name, restaurant_name, items, delivery_address)
        self.payment_method = payment_method
        self.payment_status = "Unpaid"

    def process_payment(self):
        print(f"Processing payment for order '{self.order_id}' via {self.payment_method}...")
        self.payment_status = "Paid"
        print(f"Payment status: {self.payment_status}")

    def process_order(self):
        if self.payment_status == "Paid":
            self.order_status = "Processed"
            print(f"Order '{self.order_id}' has been processed.")
        else:
            print(f"Order '{self.order_id}' cannot be processed until payment is completed.")


# Restaurant Class 
class Restaurant:
    def __init__(self, restaurant_name, restaurant_address):
        self.restaurant_name = restaurant_name
        self.restaurant_address = restaurant_address
        self.menu = []
        self.orders = []

    def add_order(self, order):
        self.orders.append(order)
        print(f"Order '{order.order_id}' added to '{self.restaurant_name}'.")

    def manage_orders(self):
        print(f"Orders for '{self.restaurant_name}':")
        for order in self.orders:
            print(f"- Order ID: {order.order_id}, Status: {order.order_status}")


# Menu Class 
class Menu:
    def __init__(self, items, description, price):
        self.items = items  # List of items
        self.description = description
        self.price = price

    def update_menu(self, new_items):
        self.items = new_items
        print("Menu updated successfully.")


# Customer Class (Inherits User) 
class Customer(User):
    def __init__(self, customer_id, customer_name, phone, address, payment_details):
        super().__init__(customer_id, customer_name)
        self.phone = phone
        self.address = address
        self.payment_details = payment_details
        self.cart = []

    def choose_restaurant(self, restaurant):
        print(f"Customer '{self.user_name}' chose restaurant '{restaurant.restaurant_name}'.")

    def browse_menu(self, menu):
        print(f"Menu: {menu.items}")

    def add_to_cart(self, item):
        self.cart.append(item)
        print(f"Item '{item}' added to cart.")

    def place_order(self, order):
        print(f"Order '{order.order_id}' placed by customer '{self.user_name}'.")

    def track_order(self, order):
        print(f"Order '{order.order_id}' status: {order.order_status}")


# Delivery_guy Class (Inherits User) 
class Delivery_guy(User):
    def __init__(self, name, transportation_details, location):
        super().__init__(None, name)
        self.transportation_details = transportation_details
        self.location = location

    def accept_order(self, order):
        print(f"Delivery guy '{self.user_name}' accepted order '{order.order_id}'.")

    def update_order_status(self, order, status):
        order.order_status = status
        print(f"Order '{order.order_id}' status updated to '{status}' by delivery guy '{self.user_name}'.")


# Ordering_system Class 
class Ordering_system:
    def __init__(self, customer, restaurant, order):
        self.customer = customer
        self.restaurant = restaurant
        self.order = order

    def create_order(self):
        print(f"Order '{self.order.order_id}' created by '{self.customer.user_name}' for restaurant '{self.restaurant.restaurant_name}'.")


# Testing the System
if __name__ == "__main__":
    # Initialize objects
    customer = Customer("C001","Franck", "00000", "Kneza Mihajla 17", "Cash")
    restaurant = Restaurant("Pizzeria Uomo", "Vladimira Gacinovica 25")
    menu = Menu(["Pizza", "Steak", "Pasta"], "Delicious food", 10.99)
    order = Payment("O001", "Franck", "Pizzeria Uomo", ["Pizza", "Steak"], "Kneza Mihajla 17", "Credit Card")
    delivery_guy = Delivery_guy("Sebastian", "Car", "Milana Blagojevica Spanca 12")

    # Customer actions
    customer.register_user()
    customer.login()
    customer.choose_restaurant(restaurant)
    customer.browse_menu(menu)
    customer.add_to_cart("Pizza")
    customer.add_to_cart("Steak")

    # Place and process order
    restaurant.add_order(order)
    customer.place_order(order)
    order.process_payment()
    order.process_order()

    # Manage orders
    restaurant.manage_orders()

    # Delivery guy updates
    delivery_guy.accept_order(order)
    delivery_guy.update_order_status(order, "Delivered")

    # Track order
    customer.track_order(order)

    # Logout
    customer.logout()
