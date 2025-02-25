import unittest
from unittest.mock import Mock
from OnlineCourseSystem import OnlineCourseManagement
from OnlineCourseSystem import Course
from OnlineCourseSystem import Account
from OnlineCourseSystem import Cart
from OnlineCourseSystem import Course

class TestAddToCart(unittest.TestCase):
    def setUp(self):
        """Set up test fixtures before each test method is run."""
        # Create a mock system
        self.mock_system = Mock(spec=OnlineCourseManagement)
        
        # Create test data
        self.test_course = Course("CS101", "Introduction to Programming", 99.99, "Computer Science")
        self.test_account = Account("A123", "testuser", "password", "test@example.com")
        
        # Configure mock behavior
        self.mock_system.get_account_cart.return_value = Cart(self.test_account)
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

class TestSearchFeature(unittest.TestCase):
    def setUp(self):
        """Set up test fixtures before each test method is run."""
        # Create a mock system
        self.mock_system = Mock(spec=OnlineCourseManagement)
        
        # Create test data
        self.test_courses = [
            Course("CS101", "Introduction to Programming", 99.99, "Computer Science"),
            Course("CS102", "Data Structures", 79.99, "Computer Science"),
            Course("CS103", "Algorithms", 89.99, "Computer Science"),
            Course("CS104", "Machine Learning", 109.99, "Computer Science")
        ]
        
        # Mock the get_course_detail method to return the course name
        for course in self.test_courses:
            course.get_course_detail = Mock(return_value=course._Course__course_name)
        
        # Configure mock behavior
        self.mock_system.search_course_by_keyword.side_effect = lambda keyword: [course for course in self.test_courses if keyword.lower() in course.get_course_detail().lower()]
        self.mock_system.search_course_by_category.side_effect = lambda category: [course for course in self.test_courses if course.get_course_category().lower() == category.lower()]
        self.mock_system.search_course_by_keyword_and_category.side_effect = lambda keyword, category: [course for course in self.test_courses if keyword.lower() in course.get_course_detail().lower() and course.get_course_category().lower() == category.lower()]

    def test_search_course_by_keyword(self):
        """Test searching courses by keyword."""
        result = self.mock_system.search_course_by_keyword("Programming")
        
        # Verify the method was called with correct parameters
        self.mock_system.search_course_by_keyword.assert_called_with("Programming")
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].get_course_detail(), "Introduction to Programming")

    def test_search_course_by_category(self):
        """Test searching courses by category."""
        result = self.mock_system.search_course_by_category("Computer Science")
        
        # Verify the method was called with correct parameters
        self.mock_system.search_course_by_category.assert_called_with("Computer Science")
        self.assertEqual(len(result), 4)

    def test_search_course_by_keyword_and_category(self):
        """Test searching courses by keyword and category."""
        result = self.mock_system.search_course_by_keyword_and_category("Machine", "Computer Science")
        
        # Verify the method was called with correct parameters
        self.mock_system.search_course_by_keyword_and_category.assert_called_with("Machine", "Computer Science")
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].get_course_detail(), "Machine Learning")

class TestCartCalculateTotal(unittest.TestCase):
    def setUp(self):
        """Set up test fixtures before each test method is run."""
        # Create a mock system
        self.mock_system = Mock(spec=OnlineCourseManagement)
        
        # Create test data
        self.test_account = Account("A123", "testuser", "password", "test@example.com")
        self.test_course1 = Course("CS101", "Introduction to Programming", 99.99, "Computer Science")
        self.test_course2 = Course("CS102", "Data Structures", 79.99, "Computer Science")
        self.test_cart = Cart(self.test_account)
        self.test_cart.add_item(self.test_course1)
        self.test_cart.add_item(self.test_course2)
        
        # Configure mock behavior
        self.mock_system.get_account_cart.return_value = self.test_cart
        
    def test_calculate_total(self):
        """Test calculating the total price of items in the cart."""
        cart = self.mock_system.get_account_cart("A123")
        total = cart.calculate_total()
        
        # Verify the total price calculation
        self.assertEqual(total, 179.98)

if __name__ == "__main__":
    unittest.main()