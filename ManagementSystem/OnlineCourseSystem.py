class OnlineCourseManagement:
    def __int__(self):
        self.__student_list = []
        self.__course_list = []
    
    def get_course(self):
        pass

    def get_account_cart(self):
        pass

    def add_item(self, course):
        pass

class Course:
    def __init__(self, course_id, course_name, course_price):
        self.__course_id = course_id
        self.__course_name = course_name
        self.__course_price = course_price
    
    def check_course_id(self, course_id):
        pass

class Cart:
    def __init__(self):
        self.__cart = []

    def add_item(self, course):
        pass

class Account:
    def __init__(self, account_id, account_name):
        self.__account_id = account_id
        self.__account_name = account_name
        self.__account_cart = None

    def check_account_id(self, account_id):
        pass

    def add_item_to_cart(self, course):
        pass


