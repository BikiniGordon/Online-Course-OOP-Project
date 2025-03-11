from fasthtml.common import *
from OnlineCourseSystem import *

app, rt = fast_app(live=True, debug=True)

payment_id = 1

def add_data():
    imeow = OnlineCourseManagement()
    
    # Programming Courses
    imeow.add_course_list("1", "Python Programming", "Learn Python programming from basics to advanced concepts", 100, "Programming")
    imeow.add_course_list("2", "Java Programming", "Master Java programming language and OOP principles", 150, "Programming")

    chapter1_1 = Chapter("1")
    chapter1_1.add_lesson("1", "Variables and Data Types", "Lesson 1 content", "Understanding variables and basic data types", "Variables are containers for storing data values...")
    chapter1_1.add_lesson("2", "Operators", "Lesson 2 content", "Learn about operators", "Operators are used to perform operations on variables and values...")
    chapter1_1.add_lesson("3", "Strings", "Lesson 3 content", "Learn about strings", "Strings are used for storing text...")
    
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
    
    # Add Pet Care Course
    imeow.add_course_list("3", "Pet Care Basics", "Essential guide for taking care of your pets", 80, "Pet")

    
    chapter1_pet = Chapter("1")
    chapter1_pet.add_lesson("1", "Understanding Your Pet", "Pet Basics", 
                          "Learn about pet behavior and needs", 
                          "Understanding your pet's behavior is key to being a good pet owner...")
    chapter1_pet.add_lesson("2", "Pet Nutrition", "Nutrition Guide", 
                          "Learn about proper pet nutrition", 
                          "Proper nutrition is essential for your pet's health...")
    
    chapter2_pet = Chapter("2")
    chapter2_pet.add_lesson("1", "Basic Pet Care", "Daily Care Guide", 
                          "Learn daily pet care routines", 
                          "Daily care routines help keep your pet healthy and happy...")
    
    course3 = imeow.get_course("3")
    course3.add_chapter(chapter1_pet)
    course3.add_chapter(chapter2_pet)

    # Add Cooking Course
    imeow.add_course_list("4", "Basic Cooking Skills", "Learn fundamental cooking techniques and kitchen essentials", 120, "Cooking")
    
    chapter1_cooking = Chapter("1")
    chapter1_cooking.add_lesson("1", "Kitchen Basics", "Kitchen Introduction", 
                              "Learn kitchen tools and equipment", 
                              "Understanding your kitchen tools is the first step to becoming a good cook...")
    chapter1_cooking.add_lesson("2", "Knife Skills", "Basic Cutting Techniques", 
                              "Master basic cutting techniques", 
                              "Proper knife skills are essential for food preparation...")
    
    chapter2_cooking = Chapter("2")
    chapter2_cooking.add_lesson("1", "Basic Cooking Methods", "Cooking Techniques", 
                              "Learn fundamental cooking methods", 
                              "Understanding different cooking methods will improve your cooking skills...")
    
    course4 = imeow.get_course("4")
    course4.add_chapter(chapter1_cooking)
    course4.add_chapter(chapter2_cooking)
    
    # Add a test account
    imeow.add_account_list("1", "testuser", "password", "test@example.com")
    account = imeow.get_account("1")
    Enrollment1 = Enrollment(account, course1, 0)
    imeow.add_enrollment_list(Enrollment1)
    Order1 = Order(account, Enrollment1)
    account.add_account_order(Order1)
    
    for account in imeow.get_account_list():
        print(f"Account ID: {account.get_account_id()}, Username: {account.get_username()}, Password: {account.get_password()}")
        
    return imeow


test = add_data()


@rt('/{account_id}/main')
def main(account_id: str):
    account = test.get_account(account_id)
    enrolled_courses = account.view_enrolled_course()
    enrolled_course_card = []
    recommended_courses = []
    recommended_courses_based_on_interest = []
    
    all_courses = test.get_course_list()
    enrolled_ids = [course.get_course_id() for course in enrolled_courses]
    enrolled_categories = [course.get_course_category() for course in enrolled_courses]
    
    # Create cards for enrolled courses
    for course in enrolled_courses:
        course_id = course.get_course_id()
        enrolled_course_card.append(
            Card(
                H3(course.get_course_name()),
                P(course.get_course_category(), style='color: #5996B2;'),
                P(course.get_course_detail()),
                Button("Start Learning",
                    onclick=f"window.location.href='enrolled/{course_id}'"),
                style="min-width: 250px; margin: 10px;"
            )
        )
    
    # Create cards for recommended courses
    for course in all_courses:
        if course.get_course_id() not in enrolled_ids:
            if course.get_course_category() in enrolled_categories:
                recommended_courses_based_on_interest.append(
                    Card(
                        H3(course.get_course_name()),
                        P(course.get_course_category(), style='color: #5996B2;'),
                        P(course.get_course_detail()),
                        P(f"Price: {course.get_course_price()}฿"),
                        Button("View Course",
                            onclick=f"window.location.href='course/{course.get_course_id()}'"),
                        style="min-width: 250px; margin: 10px;"
                    )
                )
            else:
                recommended_courses.append(
                    Card(
                        H3(course.get_course_name()),
                        P(course.get_course_category(), style='color: #5996B2;'),
                        P(course.get_course_detail()),
                        P(f"Price: {course.get_course_price()}฿"),
                        Button("View Course",
                            onclick=f"window.location.href='course/{course.get_course_id()}'"),
                        style="min-width: 250px; margin: 10px;"
                    )
                )

    # Add other categories section
    other_categories = {}
    
    # Group courses by category
    for course in all_courses:
        if (course.get_course_id() not in enrolled_ids and 
            course.get_course_category() not in enrolled_categories):
            category = course.get_course_category()
            if category not in other_categories:
                other_categories[category] = []
            other_categories[category].append(
                Card(
                    H3(course.get_course_name()),
                    P(category, style='color: #5996B2;'),
                    P(course.get_course_detail()),
                    P(f"Price: {course.get_course_price()}฿"),
                    Button("View Course",
                           onclick=f"window.location.href='course/{course.get_course_id()}'"),
                    style="min-width: 250px; margin: 10px;"
                )
            )

    # Create category sections
    category_sections = []
    for category, courses in other_categories.items():
        if courses:
            category_sections.extend([
                H2(f"Explore {category} Courses", style="margin-top: 50px;"),
                Div(
                    Grid(
                        *courses,
                        columns=len(courses),
                        style="display: flex; overflow-x: auto;"
                    ),
                    style="margin: 20px 0;"
                )
            ])

    return Container(
        Titled("Welcome! {}".format(account.get_account_username()), 
               style="margin-top: 20px;"),
        
        # Enrolled Courses Section
        H2("My Enrolled Courses", style="margin-top: 50px;"),
        Div(
            Grid(
                *enrolled_course_card if enrolled_course_card else P("You haven't enrolled in any courses yet."),
                columns=len(enrolled_course_card) if enrolled_course_card else 1,
                style="display: flex; overflow-x: auto;"
            ),
            style="margin: 20px 0;"
        ),
        
        # Recommended Courses Section
        H2("Recommended Courses", style="margin-top: 50px;"),
        P("Based on your interests", style="color: #666;"),
        Div(
            Grid(
                *recommended_courses_based_on_interest if recommended_courses_based_on_interest else P("No recommendations available."),
                columns=len(recommended_courses_based_on_interest) if recommended_courses_based_on_interest else 1,
                style="display: flex; overflow-x: auto;"
            ),
            style="margin: 20px 0;"
        ),
        
        # Other Categories Sections
        *category_sections
    )

@rt('/{account_id}/course/{course_id}')
def view_course(account_id: str ,course_id: str):
    course = test.get_course(course_id)
    chapter_num = len(course.get_chapter_list())
    lesson_num = sum([len(chapter.get_lesson_list()) for chapter in course.get_chapter_list()])
    return Container(
        Grid(
            Card(
                P(course.get_course_category(), style='color: #5996B2;'),
                H3(course.get_course_name()),
                P(course.get_course_detail()),
                Card(
                    H5("This course includes", style='text-align: center;'),
                    P("{} chapters".format(chapter_num)),
                    P("{} lessons".format(lesson_num)),
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
def close_popup():
    return ""  # Returns empty string to clear the popup content

@rt('/cart/{account_id}')
def view_cart(account_id: str):
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
              onclick=f"window.location.href='/{account_id}/main'", # Redirect to main page [not available at the moment]
        )

@rt('/{account_id}/enrolled/{course_id}')
def view_enrolled_course(account_id: str, course_id: str):
    course = test.get_enrolled_course(account_id, course_id)
    if course:
        return Container(
            Grid(
                Div(
                    Div(
                        P("Select a lesson to view content", 
                            style="text-align: center; color: #666;"),
                        id="lesson-content",
                        cls="main-content"
                    ),
                    H3(f"Course: {course.get_course_name()}", 
                        style="margin-top: 20px;")
                ),
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
                                    cls="lesson-box", style = "margin-bottom: 20px;"
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
    return H1("Course not found", style="color: #dc3545;")

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
    
@rt('/login', methods=['GET'])
def get_login():
    return Container(
        H1("Login", style="text-align: center; margin-bottom: 20px;"),
        Form(
            Div(
                Label("Username", 
                    Input(
                        type="text", 
                        id="username",
                        name="username",
                        required=True,
                        placeholder="Enter your username",
                        style="width: 100%;"
                    )
                ),
                Label("Password", 
                    Input(
                        type="password", 
                        id="password",
                        name="password",
                        required=True,
                        placeholder="Enter your password",
                        style="width: 100%;"
                    )
                ),
                style="max-width: 300px;"
            ),
            
            Button(
                "Login", 
                type="submit",
                style=""" 
                    max-width: 200px;
                    margin: 20px auto 0;
                    display: block;
                    background-color: #007bff; 
                    color: white;
                """
            ),
            
            method="post",
            action="/login",
            style="padding: 20px;"
        ),
        style="""
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
        """
    )

@rt('/login', methods=['POST'])
def post_login(username: str, password: str):
    account = test.login(username, password)
    if account:
        account_id = account.get_account_id()
        return Redirect(f"/{account_id}/main")
    else:
        return Container(
            H1("Login Failed", style="text-align: center; color: red;"),
            P("Invalid username or password."),
            A("Go back", href="/login", style="display: block; text-align: center; margin-top: 20px;")
        )

@rt('/{account_id}/search', methods=['GET'])
def get_search(account_id: str):
    results = test.search_courses("")
    
    return Titled("Search Online Courses",
        Form(
            Input(id="search", placeholder="Search courses...", hx_get="/searchresult", target_id="results", hx_trigger="keyup delay:500ms change"),
            style="margin-bottom: 20px;"
        ),
        Div(
            *[
                A(
                    Card(H3(c.get_course_name()), P(c.get_course_detail()), P(f"Category: {c.get_course_category()}"), H6(f"{c.get_course_price()}฿", style="color: #FFFF00"), style="cursor: pointer;"),
                    href=f"/{account_id}/course/{c.get_course_id()}",
                    style="text-decoration: none; color: inherit;"
                )
                for c in results
            ],
            id="results",
            style="margin-top: 20px;"
        )
    )

@rt('/{account_id}/searchresult', methods=['GET'])
def get_search_result(search: str, account_id: str):
    results = test.search_courses(search)
    
    return Div(
        *[
            A(
                Card(H3(c.get_course_name()), P(c.get_course_detail()), P(f"Category: {c.get_course_category()}"), H6(f"{c.get_course_price()}฿", style="color: #FFFF00"), style="cursor: pointer;"),
                href=f"/{account_id}/course/{c.get_course_id()}",
                style="text-decoration: none; color: inherit;"
            )
            for c in results
        ] if results else [P("No courses found.")],
        style="margin-top: 10px;"
    )

serve(port=5005)
