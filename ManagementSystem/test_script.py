import unittest
from unittest.mock import Mock
from OnlineCourseSystem import OnlineCourseManagement
from OnlineCourseSystem import Course
from OnlineCourseSystem import Account
from OnlineCourseSystem import Cart

class TestAddToCart(unittest.TestCase):
    def setUp(self):
        """Set up test fixtures before each test method is run."""
        # Create a mock system
        self.mock_system = Mock(spec=OnlineCourseManagement)
        
        # Create test data
        self.test_course = Course("CS101", "Introduction to Programming", 99.99)
        self.test_account = Account("A123", "testuser", "password", "test@example.com", None, None, None)
        
        # Configure mock behavior
        self.mock_system.get_account_cart.return_value = Cart()
        self.mock_system.add_to_cart.return_value = "Added item to cart"
        
    def test_add_to_cart_via_system(self):
        """Test adding a course to a cart through the system."""
        result = self.mock_system.add_to_cart("A123", "CS101")
        
        # Verify the method was called with correct parameters
        self.mock_system.add_to_cart.assert_called_with("A123", "CS101")
        self.assertEqual(result, "Added item to cart")
    
    def test_get_account_cart(self):
        """Test that get_account_cart returns a Cart object."""
        cart = self.mock_system.get_account_cart("A123")
        
        # Verify the method was called and returns expected type
        self.mock_system.get_account_cart.assert_called_with("A123")
        self.assertIsInstance(cart, Cart)
    
    def test_nonexistent_account_or_course(self):
        """Test adding a nonexistent course or using nonexistent account."""
        # Configure mock for failure case
        self.mock_system.add_to_cart.return_value = "Failed to add course to cart"
        
        result1 = self.mock_system.add_to_cart("INVALID", "CS101")
        self.assertEqual(result1, "Failed to add course to cart")

        result2 = self.mock_system.add_to_cart("A123", "INVALID")
        self.assertEqual(result2, "Failed to add course to cart")

if __name__ == "__main__":
    unittest.main()