from fasthtml.common import *
from OnlineCourseSystem import *

app, rt = fast_app()

payment_id = 1

def add_data():
    imeow = OnlineCourseManagement()
    
    imeow.add_course_list("1", "Python Programming", 100, "Programming")
    imeow.add_course_list("2", "Java Programming", 150, "Programming")

    chapter1_1 = Chapter("1")
    chapter1_1.add_lesson("1", "Variables and Data Types", "Lesson 1 content", "Understanding variables and basic data types", "Variables are containers for storing data values...")
    
    chapter2_1 = Chapter("2")
    chapter2_1.add_lesson("2", "Control Structures", "Lesson 2 content", "Learn about if statements and loops", "Control structures help you control the flow...")

    course1 = imeow.get_course("1")
    course1.add_chapter(chapter1_1)
    course1.add_chapter(chapter2_1)

    chapter1_2 = Chapter("1")
    chapter1_2.add_lesson("1", "Variables and Data Types", "Lesson 1 content", "Understanding variables and basic data types", "Variables are containers for storing data values...")
    chapter2_2 = Chapter("2")
    chapter2_2.add_lesson("2", "Control Structures", "Lesson 2 content", "Learn about if statements and loops", "Control structures help you control the flow...")
    chapter3_2 = Chapter("3")
    chapter3_2.add_lesson("3", "Functions", "Lesson 3 content", "Learn about functions", "Functions are a block of code which only runs when it is called...")

    course2 = imeow.get_course("2")
    course2.add_chapter(chapter1_2)
    course2.add_chapter(chapter2_2)
    course2.add_chapter(chapter3_2)
    
    # Add a test account
    imeow.add_account_list("1", "testuser", "password", "test@example.com")
    account = imeow.get_account("1")
    Enrollment1 = Enrollment(account, course1, 0)
    imeow.add_enrollment_list(Enrollment1)
    Order1 = Order("1", Enrollment1)
    account.add_account_order(Order1)
    imeow.add_student_list("Name", "Surname", "69", account)
    return imeow

test = add_data()

@rt('/{account_id}/course/{course_id}')
def get(account_id: str ,course_id: str):
    course = test.get_course(course_id)
    return Container(
        Grid(
            Card(
                P(course.get_course_category(), style='color: #5996B2;'),
                H3(course.get_course_name()),
                P("This course is about Python Programming"),
                Card(
                    H5("This course includes", style='text-align: center;'),
                    P("5 chapters"),
                    P("20 lessons"),
                    P("1 downloadable resource"),
                    P("Certificate of completion"),
                )
            ),
            Card(
                H1("This is an image."),
                H4("{}฿".format(course.get_course_price())),
                Button("Add to Cart", 
                      hx_post= "/" + account_id + "/addtocart/" + course_id,
                      hx_target="#cart-message")
            )
        ),
        Div(id="cart-message")  # Placeholder for popup message
    )

@rt('/{account_id}/addtocart/{course_id}')
def add_course_to_cart(account_id: str, course_id: str):
    result = test.add_to_cart(account_id, course_id)
    # If course is already in cart
    if result == "Course already in cart":
        return Container(
            Card(
                Grid(
                    Button("×", 
                          hx_post="/close-popup",
                          hx_target="#cart-message",
                          style="background: none; border: none; font-size: 20px; position: absolute; right: 10px; top: 5px;"),
                    P("This course is already added!", style="color: #dc3545;"),
                    Button("View Cart", 
                          onclick=f"window.location.href='/cart/{account_id}'",
                          style="background-color: #5996B2; color: white;"),
                    columns=1
                ),
                style="position: relative; padding: 20px;"
            ),
            style="position: fixed; bottom: 20px; right: 20px; z-index: 1000;",
            id="cart-message"
        )
    elif result == "Added item to cart":
        return Container(
            Card(
                Grid(
                    Button("×", 
                          hx_post="/close-popup",
                          hx_target="#cart-message",
                          style="background: none; border: none; font-size: 20px; position: absolute; right: 10px; top: 5px;"),
                    P("Course added to cart successfully!"),
                    Button("View Cart", 
                          onclick=f"window.location.href='/cart/{account_id}'",
                          style="background-color: #5996B2; color: white;"),
                    columns=1
                ),
                style="position: relative; padding: 20px;"
            ),
            style="position: fixed; bottom: 20px; right: 20px; z-index: 1000;",
            id="cart-message"
        )
    return result

@rt('/close-popup')
def post():
    return ""  # Returns empty string to clear the popup content

@rt('/cart/{account_id}')
def get(account_id: str):
    account = test.get_account(account_id)
    cart = account.get_cart()
    cart_items = []
    for course in cart.get_content():
        cart_items.append(
            Card(
                H3(course.get_course_name()),
                P(f"{course.get_course_price()}฿")
            )
        )
    
    # Return a complete new page
    return Titled("Shopping Cart",  # This creates a new page with proper title
        Container(
            H1("Your Cart"),
            *cart_items,
            P(f"Total: {cart.calculate_total()}฿"),
            Button("Checkout with Credit card", 
                  onclick=f"window.location.href='/{account_id}/checkout/credit_card'",
                  style="background-color: #28a745; color: white;"),
            Button("Checkout by other ways", 
                  onclick=f"window.location.href='/{account_id}/checkout/others'",
                  style="background-color: #28a745; color: white;"),
            Button("Continue Shopping", 
                  onclick=f"window.location.href='/{account_id}/course/1'",
                  style="background-color: #5996B2; color: white;")
        )
    )

@rt('/{account_id}/checkout/others')
def others(account_id: str):
    return Container(
        H1("We don't have such thing, please pay with credit card. [I beg you]"),
        Form(
            Button("Back to Cart"),
            method="/get",
            action=f"/cart/{account_id}"
        )
    )

@rt('/{account_id}/checkout/credit_card')
def credit_card(account_id: str):
    return Container(
        H1("Credit Card Payment"),
        Form(
            Label("Card number:", id="card_number"),
            Input(placeholder = "Example: 1234 5678 1234 [If you paid once, you don't need to be worry, type anything.]",type="text", name="card_number"),
            Button("Pay"),
            method="post",
            action=f"/{account_id}/pay"
        )
    )

@rt('/{account_id}/pay')
def pay(account_id: str, card_number: str):
    global payment_id
    account = test.get_account(account_id)
    student = test.get_student(account_id)
    cart = account.get_cart()
    if account.get_account_payment_method() == None:
        card = CreditCard(payment_id, card_number)
        account.set_account_payment_method(card)
    else:
        card = account.get_account_payment_method()
    card.pay(cart.calculate_total())
    payment_id += 1
    for item in cart.get_content():
        enroll = Enrollment(student, item, 0)
        order_item = Order(account, enroll)
        account.add_account_order(order_item)
    cart.clear_item()
    
    return Container(
        H1(f"Payment Successful! Your course(s) will be available in your account. Balance: {card.get_balance()}"),
        Button("Back to main"), 
              onclick=f"window.location.href='/cart/{account_id}'", # Redirect to main page [not available at the moment]
        )

@rt('/{account_id}/enrolled/{course_id}')
def get(account_id: str, course_id: str):
    course = test.get_enrolled_course(account_id, course_id)
    return Container(
        Grid(
            # Left side - Lesson content
            Div(
                Div(
                    P("Select a lesson to view content", 
                        style="text-align: center; color: #666;"),
                    id="lesson-content",
                    cls="main-content"
                ),
                # Course name moved to bottom
                H3(f"Course: {course.get_course_name()}", 
                    style="margin-top: 20px;")
            ),
            # Right side - Navigation
            Div(
                H2("Course Navigation"),
                *[
                    Card(
                        H3(f"Chapter {chapter.get_chapter_id()}"),
                        *[
                            Div(
                                H4(f"Lesson {lesson.get_lesson_id()}: {lesson.get_lesson_name()}"),
                                P(lesson.get_lesson_description()),
                                Button(
                                    "View Lesson",
                                    hx_get=f"/{account_id}/lesson/{course_id}-{chapter.get_chapter_id()}-{lesson.get_lesson_id()}",
                                    hx_target="#lesson-content",
                                    hx_swap="innerHTML"
                                ),
                                cls="lesson-box"
                            ) for lesson in chapter.get_lesson_list()
                        ],
                        cls="chapter-box"
                    ) for chapter in course.get_chapter_list()
                ],
                cls="sidebar"
            ),
            columns=2
        )
    )

# Add this new route to handle lesson content display
@rt('/{account_id}/lesson/{lesson_id}')
def view_lesson(account_id: str, lesson_id: str):
    account = test.get_account(account_id)
    lesson = account.view_lesson(lesson_id)
    
    if lesson:
        return Container(
            H2(lesson.get_lesson_name()),
            Card(
                P(lesson.get_lesson_content()),
                style="margin-bottom: 20px;"
            )
        )
    return P("Lesson not found", style="color: #dc3545;")

def get_style():
    return """
    <style>
        body {
            font-family: Noto Sans, sans-serif;
            margin: 0;
            padding: 0;
        }
    """    

serve()

