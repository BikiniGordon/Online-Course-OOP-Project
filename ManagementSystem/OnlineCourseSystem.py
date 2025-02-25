class OnlineCourseManagement:
    def __int__(self):
        self.__student_list = []
        self.__teacher_list = []
        self.__course_list = []
        self.__enrollment_list = []
        self.__faq_list = []

    def add_student_list(self, id, username, password, email):
        self.__student_list.append(Student(id, username, password, email, None, None, None))

    def add_teacher_list(self, student):
        pass

    def add_course_list(self, id, name, price):
        self.__course_list.append(Course(id, name, price))

    def add_enrollment_list(self, enrollment):
        pass
    
    def add_faq_list(self, faq):
        pass
        
    def get_course(self, course_id):
        for course in self.__course_list:
            if course.check_course_id(course_id):
                return course
            return None

    def get_account(self, account_id):
        for account in self.__student_list:
            if account.check_account_id(account_id):
                return account
            return None

    def get_account_cart(self, account_id):
        account = self.get_account(account_id)
        return account.get_cart()

    def add_to_cart(self, account_id, course_id):
        account = self.get_account(account_id)
        course = self.get_course(course_id)
        if account is None or course is None:
            return "Failed to add course to cart"
        if account.add_item_to_cart(course):
            return "Added item to cart"
        return "Failed to add course to cart"

    def create_noti(self, content):
        pass

class Course:
    def __init__(self, course_id, course_name, course_price):
        self.__course_id = course_id
        self.__course_name = course_name
        self.__course_price = course_price
    
    def check_course_id(self, course_id):
        if self.__course_id == course_id:
            return True
        return False
    
    def add_chapter(self, chapter_id):
        pass

    def add_course_description(self):
        pass
    
    def get_course_detail(self):
        pass

class Chapter:
    def __init__(self, chapter_id):
        self.__chapter_id = chapter_id
        self.__lesson_list = []
    
    def add_lesson(self, lesson_id, lesson_name, lesson_content, lesson_description, lesson_material):
        pass
    
    def get_chapter_detail(self):
        pass

class Lesson:
    def __init__(self, lesson_id, lesson_name, lesson_content, lesson_description, lesson_material):
        self.__lesson_id = lesson_id
        self.__lesson_name = lesson_name
        self.__lesson_content = lesson_content 
        self.__lesson_description = lesson_description 
        self.__lesson_material = lesson_material
    
    def add_lesson_name(self, lesson_name):
        pass

    def add_lesson_content(self, lesson_content):
        pass
    
    def add_lesson_description(self, lesson_description):
        pass
    
    def add_lesson_material(self, lesson_material):
        pass
    
class Cart:
    def __init__(self):
        self.__cart = []

    def add_item(self, course):
        self.__cart.append(course)
        return "Success"

    def remove_item(self, course):
        pass

    def checkout(self):
        pass

class Account:
    def __init__(self, account_id, account_username, account_password, account_email, account_payment_method, account_cart, account_order):
        self.__account_id = account_id
        self.__account_name = account_username
        self.__account_password = account_password
        self.__account_email = account_email
        self.__account_payment_method = None
        self.__account_cart = Cart()
        self.__account_order = None

    def login(self):
        pass

    def logout(self):
        pass
    
    def check_account_id(self, account_id):
        if self.__account_id == account_id:
            return True
        return False

    def get_cart(self):
        return self.__account_cart
    
    def add_item_to_cart(self, course):
        self.__account_cart.add_item(course)
        return "Success"
        

class Person:
    def __init__(self, name, surname, age, account: Account):
        self.__name = name
        self.__surname = surname
        self.__age = age
        self.__account = account
    
    def edit_profile(self):
        pass

    def view_profile(self):
        pass
        
class Student(Person):
    def __init__(self, name, surname, age, account: Account):
        super().__init__(name, surname, age, account)
        self.__enrollment_list = [] 

class Teacher(Person):
    def __init__(self, name, surname, age, account: Account):
        super().__init__(name, surname, age, account)
        self.__course_list = []

    def create_course(self, course):
        pass

    def edit_course(self, course):
        pass

    def remove_course(self, course):
        pass

class Enrollment:
    def __init__(self, student, course, progression):
        self.__student = student
        self.__course = course
        self.__progression = progression
        
    def update_progression(self):
        pass

class Order:
    def __init__(self, order_account: Account):
        self.__order_account = order_account
        self.__paid_enrollment = []

class PaymentMethod:
    def __init__(self, payment_id):
        self.__payment_id = payment_id

    def process_payment(self):
        pass

class CreditCard(PaymentMethod):
    def __init__(self, payment_id, card_number):
        super().__init__(payment_id)
        self.__card_number = card_number


class Notification:
    def __init__(self, notification_id, notification_content):
        self.__notification_id = notification_id
        self.__text = notification_content

    def delete_notification(self):
        pass

class FAQ:
    def __init__(self, faq_id, faq_question):
        self.__faq_id = faq_id
        self.__faq_question = faq_question
        self.__faq_answer = None

    def __add_answer(self, answer):
        pass

