class OnlineCourseManagement:
    def __init__(self):
        self.__student_list = []
        self.__teacher_list = []
        self.__course_list = []
        self.__enrollment_list = []
        self.__faq_list = []

    def add_student_list(self, id, username, password, email):
        self.__student_list.append(Account(id, username, password, email))

    def add_teacher_list(self, student):
        pass

    def add_course_list(self, id, name, price, category):
        self.__course_list.append(Course(id, name, price, category))

    def add_enrollment_list(self, enrollment):
        pass
    
    def add_faq_list(self, faq_id, faq_question):
        self.__faq_list.append(FAQ(faq_id, faq_question))

    def get_faq_list(self):
        return self.__faq_list
        
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
        if account:
            return account.get_cart()
        return None

    def add_to_cart(self, account_id, course_id):
        account = self.get_account(account_id)
        course = self.get_course(course_id)
        if account is None or course is None:
            return "Failed to add course to cart"
        result = account.add_item_to_cart(course)
        if result == "Success":
            return "Added item to cart"
        elif result == "Course already in cart":
            return "Course already in cart"
        return "Failed to add course to cart"

    def create_noti(self, content):
        pass
    
    def search_course(self, keyword):
        for course in self.__course_list:
            if keyword in course.get_course_detail():
                return course
        return None

    def search_course_by_keyword(self, keyword):
        matching_courses = []
        for course in self.__course_list:
            if keyword.lower() in course.get_course_detail().lower():
                matching_courses.append(course)
        return matching_courses

    def search_course_by_category(self, category):
        matching_courses = []
        for course in self.__course_list:
            if course.get_course_category().lower() == category.lower():
                matching_courses.append(course)
        return matching_courses

    def search_course_by_keyword_and_category(self, keyword, category):
        matching_courses = []
        for course in self.__course_list:
            if keyword.lower() in course.get_course_detail().lower() and course.get_course_category().lower() == category.lower():
                matching_courses.append(course)
        return matching_courses

    def login(self, username, password):
        for account in self.__student_list + self.__teacher_list:
            if account.get_username() == username and account.get_password() == password:
                return account
        return None

class Course:
    def __init__(self, course_id, course_name, course_price, course_category):
        self.__course_id = course_id
        self.__course_name = course_name
        self.__course_price = course_price
        self.__course_category = course_category
        self.__chapter_list = []
    
    def check_course_id(self, course_id):
        if self.__course_id == course_id:
            return True
        return False
    
    def add_chapter(self, chapter):
        self.__chapter_list.append(chapter)

    def get_chapter(self, chapter_id):
        for chapter in self.__chapter_list:
            if chapter.get_chapter_id() == chapter_id:
                return chapter
        return None
    
    def get_chapter_list(self):
        return self.__chapter_list

    def add_course_description(self):
        pass
    
    def get_course_detail(self):
        return
    
    def get_course_id(self):
        return self.__course_id

    def get_course_name(self):
        return self.__course_name
    
    def get_course_price(self):
        return self.__course_price
    
    def get_course_category(self):
        return self.__course_category
    
class Chapter:
    def __init__(self, chapter_id):
        self.__chapter_id = chapter_id
        self.__lesson_list = []
    
    def get_chapter_id(self):
        return self.__chapter_id
    
    def add_lesson(self, lesson_id, lesson_name, lesson_content, lesson_description, lesson_material):
        return self.__lesson_list.append(Lesson(lesson_id, lesson_name, lesson_content, lesson_description, lesson_material))
    
    def get_lesson(self, lesson_id):
        for lesson in self.__lesson_list:
            if lesson.get_lesson_id() == lesson_id:
                return lesson
        return None
    
    def get_lesson_list(self):
        return self.__lesson_list

    def get_chapter_detail(self):
        pass
    
class Lesson:
    def __init__(self, lesson_id, lesson_name, lesson_content, lesson_description, lesson_material):
        self.__lesson_id = lesson_id
        self.__lesson_name = lesson_name
        self.__lesson_content = lesson_content 
        self.__lesson_description = lesson_description 
        self.__lesson_material = lesson_material
    
    def get_lesson_id(self):
        return self.__lesson_id
    
    def get_lesson_name(self):
        return self.__lesson_name
    
    def get_lesson_content(self):
        return self.__lesson_content
    
    def get_lesson_description(self):
        return self.__lesson_description

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

    def get_content(self):
        return self.__cart

    def add_item(self, course):
        # Check if course already exists in cart
        for cart_item in self.__cart:
            if cart_item.get_course_id() == course.get_course_id():
                return "Course already in cart"
        self.__cart.append(course)
        return "Success"

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
        self.__account_order = []

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
        if (self.__account_cart.add_item(course) == "Success"):
            return "Success"
        elif (self.__account_cart.add_item(course) == "Course already in cart"):
            return "Course already in cart"
        return "Failed to add course to cart"
        

    def get_username(self):
        return self.__account_name

    def get_password(self):
        return self.__account_password

    def set_account_order(self, order):
        self.__account_order = order
    
    def add_account_order(self, order):
        self.__account_order.append(order)

    def get_account_order(self):
        return self.__account_order
    
    def view_lesson(self, lesson_id):
        #ex: lesson_id = "CPE-01-01"
        course_id, chapter_id, lesson_id = lesson_id.split("-")
        for order in self.__account_order:
            enrollment = order.get_paid_enrollment()
            if enrollment.enroll_course().check_course_id(course_id):
                chapter = enrollment.enroll_course().get_chapter(chapter_id)
                if chapter:
                    lesson = chapter.get_lesson(lesson_id)
                    return lesson
        return None
    
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
    
    def enroll_course(self):
        return self.__course
    
    def update_progression(self):
        pass

class Order:
    def __init__(self, order_account: Account, paid_enrollment):
        self.__order_account = order_account
        self.__paid_enrollment = paid_enrollment

    def get_paid_enrollment(self):
        return self.__paid_enrollment
        

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

    def add_faq_answer(self, answer):
        self.__faq_answer = answer

    def get_faq_question(self):
        return self.__faq_question
    
    def get_faq_answer(self):
        return self.__faq_answer

