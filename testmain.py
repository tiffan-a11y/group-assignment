import unittest
from main import Ordering_system, Restaurant, Order, Payment, Customer, Delivery_guy, Menu

class TestOrderingSystem(unittest.TestCase):

    def setUp(self):
        # Initialize objects
        self.customer = Customer("C001", "Franck", "00000", "Kneza Mihajla 17", "Cash")
        self.restaurant = Restaurant("Pizzeria Uomo", "Vladimira Gacinovica 25")
        self.menu = Menu(["Pizza", "Steak", "Pasta"], "Delicious food", 10.99)
        self.order = Payment("O001", "Franck", "Pizzeria Uomo", ["Pizza", "Steak"], "Kneza Mihajla 17", "Credit Card")
        self.delivery_guy = Delivery_guy("Sebastian", "Car", "Milana Blagojevica Spanca 12")
        self.ordering_system = Ordering_system(self.customer, self.restaurant, self.order)

    def test_order_creation(self):
        self.assertEqual(self.order.customer_name, "Franck")
        self.assertEqual(self.order.restaurant_name, "Pizzeria Uomo")
        self.assertEqual(self.order.items, ["Pizza", "Steak"])
        self.assertEqual(self.order.delivery_address, "Kneza Mihajla 17")
        self.assertEqual(self.order.order_status, "Pending")

    def test_customer_registration_and_login(self):
        self.customer.register_user()
        self.customer.login()
        self.assertEqual(self.customer.user_name, "Franck")
        self.assertEqual(self.customer.phone, "00000")

    def test_manage_orders(self):
        self.restaurant.add_order(self.order)
        self.restaurant.manage_orders()
        self.assertIn(self.order, self.restaurant.orders)

    def test_order_payment_processing(self):
        self.order.process_payment()
        self.assertEqual(self.order.payment_status, "Paid")

    def test_order_processing(self):
        self.order.process_payment()  # First, process the payment
        self.order.process_order()
        self.assertEqual(self.order.order_status, "Processed")

    def test_delivery_guy_accepts_and_updates_order(self):
        self.delivery_guy.accept_order(self.order)
        self.assertEqual(self.order.order_status, "Pending")  # Status should still be pending before updating

        self.delivery_guy.update_order_status(self.order, "Delivered")
        self.assertEqual(self.order.order_status, "Delivered")

    def test_customer_tracking_order(self):
        self.delivery_guy.update_order_status(self.order, "Delivered")
        self.customer.track_order(self.order)
        self.assertEqual(self.order.order_status, "Delivered")  # Assuming the status was updated to "Delivered"

    def test_create_order_in_ordering_system(self):
        self.ordering_system.create_order()
        # Check that the correct order has been created for the customer and restaurant
        self.assertEqual(self.order.customer_name, "Franck")
        self.assertEqual(self.order.restaurant_name, "Pizzeria Uomo")
        self.assertEqual(self.order.order_id, "O001")

if __name__ == "__main__":
    unittest.main()
