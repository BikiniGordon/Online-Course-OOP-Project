class OnlineCourseManagement:
    def __int__(self):
        self.__student_list = []
        self.__teacher_list = []
        self.__course_list = []
        self.__enrollment_list = []
        self.__faq_list = []

    def add_student_list(self, username, password, email):
        pass

    def add_teacher_list(self, student):
        pass

    def add_course_list(self, course):
        pass

    def add_enrollment_list(self, enrollment):
        pass
    
    def add_faq_list(self, faq):
        pass
        
    def get_course(self, course_id):
        pass

    def get_account(self, account_id):
        pass

    def get_account_cart(self, account_id):
        pass

    def add_to_cart(self, course):
        pass

    def create_noti(self, content):
        pass

class Course:
    def __init__(self, course_id, course_name, course_price):
        self.__course_id = course_id
        self.__course_name = course_name
        self.__course_price = course_price
    
    def check_course_id(self, course_id):
        pass
    
    def add_chapter(self, chapter_id):
        pass

    def add_course_description(self):
        pass
    
    def get_course_detail(self):
        pass

    def get_course_price(self):
        return self.__course_price

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
    def __init__(self, account):
        self.__account = account
        self.__cart = []

    def add_item(self, course):
        self.__cart.append(course)

    def remove_item(self, course):
        self.__cart.pop(course)

    def calculate_total(self):
        total_price = 0
        for course_item in self.__cart:
            total_price += course_item.get_course_price()
        return total_price

    def create_enrollment(self):
        paid_enrollment = []
        for course_item in self.__cart:
            enroll = Enrollment(self.__account, course_item, 0)
            paid_enrollment.append(enroll)
        return paid_enrollment

class Account:
    def __init__(self, account_id, account_username, account_password, account_email):
        self.__account_id = account_id
        self.__account_name = account_username
        self.__account_password = account_password
        self.__account_email = account_email
        self.__account_cart = Cart(self)
        self.__account_payment_method = None
        self.__account_order = None

    def login(self):
        pass

    def logout(self):
        pass
    
    def check_account_id(self, account_id):
        pass

    def add_item_to_cart(self, course):
        pass

    def set_account_order(self, order):
        self.__account_order = order

    def get_account_order(self):
        return self.__account_order

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
    def __init__(self, order_account: Account, paid_enrollment):
        self.__order_account = order_account
        self.__paid_enrollment = paid_enrollment
        

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

