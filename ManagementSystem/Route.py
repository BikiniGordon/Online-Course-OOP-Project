from fasthtml.common import *
from OnlineCourseSystem import *

app, rt = fast_app(live=True, debug=True)

payment_id = 1

def add_data():
    imeow = OnlineCourseManagement()
    imeow.add_student_list("1", "John", "Doe", "18", "testuser", "password", "test@example.com")
    imeow.add_teacher_list("2", "Name", "Surname", "69", "admin", "password", "test@example.com")
    teacher = imeow.get_person("2")
    
    # Programming Courses
    imeow.add_course_list("1", "Python Programming", "Learn Python programming from basics to advanced concepts", 100, "Programming", teacher)
    imeow.add_course_list("2", "Java Programming", "Master Java programming language and OOP principles", 150, "Programming", teacher)

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
    imeow.add_course_list("3", "Pet Care Basics", "Essential guide for taking care of your pets", 80, "Pet", teacher)

    
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
    imeow.add_course_list("4", "Basic Cooking Skills", "Learn fundamental cooking techniques and kitchen essentials", 120, "Cooking", teacher)
    
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
    account = imeow.get_account("1")
    Enrollment1 = Enrollment(account, course1, 0)
    imeow.add_enrollment_list(Enrollment1)
    Order1 = Order(account, Enrollment1)
    account.add_account_order(Order1)
    global faq_id_counter
    faq_id_counter = 1
    return imeow


test = add_data()

def navbar(account_id):
    return [
        Button(
            Img(
                src = "https://media-hosting.imagekit.io//3953e1bceac64d68/logo.png?Expires=1836319434&Key-Pair-Id=K2ZIVPTIP2VGHC&Signature=n-HMFmK8VEjrAPtl-5R8~TtBvrjN6E0yc1e-v65t~YQutAJML4vFpnGYNpnH2RODKn-eqCRbbq61eHc6QU~4gi~enp4il~UJENpLKl63z~EXrdIBVp3SHYXi5WzvcQNraMM1~0Xyt81zKJr4bkSS3zYYvn4dlIluX8fcFSIspDQpe6HRI8nqpWH9oiyytIbaBv6yrOrBID46Q2uFG6tt-UcCSAZ45ry0qBFgVV55LDlyn~lJOk8uFU4c-2zIzZWc05u0Fksq3sJL9Kt99GxzQMjjX89eEg3UKGb4B5wVQD58DCw0VWJGnVEc6loq5FjEeEWoBiRgXBDD1B0r-QPf9A__",
                alt = "Home",
                style = "max-width: 100%;"
            ),
            onclick=f"window.location.href='/{account_id}/main'", 
            type="submit",
            style=""" 
                max-width: 150px;
                margin: 1.5px 1px 0;  
                background-color: #F8F2EB; 
                color: #13171f;
                text-align: center; 
                border: 1px solid #F8F2EB;
                font-weight: bold;
                font-size: 18px;
                padding: 0px;
            """
        ),
        Button(
            "Explore",
            onclick=f"window.location.href='/{account_id}/search'", 
            type="submit",
            style=""" 
                max-width: 150px;
                margin: 1.5px 10px 0; 
                background-color: #F8F2EB; 
                color: #13171f;
                text-align: center; 
                border: 1px solid #F8F2EB;
                font-weight: bold;
                font-size: 18px;
            """
        ),
        Button(
            Img(
                src = "https://media-hosting.imagekit.io//c7195462cf184c14/cart.png?Expires=1836319434&Key-Pair-Id=K2ZIVPTIP2VGHC&Signature=oDP7U3q1OKXOOE6RCZZarw9fBMt~-K8ls4SDFL7tRXVBczZO27iUMJ97iLA-xfIQS7lgwBR4bP43neffAfBwLXIJU~fh4sepbGajjzc6CTD02OHLJdH7bpuUC04HOow7PgWUnVaGNQ6lIJH1~RYvagJ62x30yJzxPtvTJQUZ4BOSbzweDWqFV9NDFy~4PrN2OPBX9efaOvQbcQQMRNDrWp15e-gKe7BrA7oUETaX2FLxKwRh2~3iSVLDtjMn2sAvXsNd5Edl8S1FP8mMSUmCDPXFsSaaJdB9jZ-Qkosl25ixqLkDBrn34iUyeL4YPWObfJr6iI3mvvwDczUOY3KhBA__",
                alt = "Cart",
                style = "max-width: 50%;"
            ),
            onclick=f"window.location.href='/cart/{account_id}'", 
            type="submit",
            style=""" 
                max-width: 150px;
                margin: 1.5px 10px 0;  
                background-color: #F8F2EB; 
                color: #13171f;
                text-align: center; 
                border: 1px solid #F8F2EB;
                font-weight: bold;
                font-size: 18px;
            """
        ),
        Button(
            Img(
                src = "https://media-hosting.imagekit.io//ae90b28ac719454a/notif.png?Expires=1836319434&Key-Pair-Id=K2ZIVPTIP2VGHC&Signature=12AsucweImODEWeUG6KEW1IU3L9AXhwid8AntHYnBCGZBqUQafCakUCRg8t1Gto1x8iG-zNqEU7WXWSsmtoFCBP1VOhNzhuPiA-uWzc-7ekBN932u18QMttqWqBkDqOVAU9A6Nkmxorp1HDai-DArPP6QB~0SeIC0M3FIzZ-SeBfM0K52lnjGT42yYDVFezoHPW9kLgblxaaA4M~GkVEFXU9BET3BPdxcxx9crwWAav~YJRc04orrcOp13u~60FV6lMcDZSXtebrwYChebdlHMAOND6FEZag6RHXtfnEvT9vkn~7fV~iWkysFeuvWZADizPFjdmGwIG5XaMgIKTndQ__",
                alt = "Notification",
                style = "max-width: 50%;"
            ),
            onclick=f"window.location.href='/{account_id}/notification'", 
            type="submit",
            style=""" 
                max-width: 150px;
                margin: 0;  
                background-color: #F8F2EB; 
                color: #13171f;
                text-align: center;
                border: 1px solid #F8F2EB;
                font-weight: bold;
                font-size: 18px;
            """
        ),
        Button(
            "FAQ",
            onclick=f"window.location.href='/{account_id}/faq'", 
            type="submit",
            style=""" 
                max-width: 150px;x;
                margin: 1.5px 10px 0;  
                background-color: #F8F2EB;
                color: #13171f;
                text-align: center;
                border: 1px solid #F8F2EB;
                font-weight: bold;
                font-size: 18px;
            """
        ),
        Button(
            Img(
                src = "https://upload.wikimedia.org/wikipedia/en/thumb/9/96/Meme_Man_on_transparent_background.webp/316px-Meme_Man_on_transparent_background.webp.png",
                alt = "Profile",
                style = "max-width: 30%;"
            ),
            onclick=f"window.location.href='/{account_id}/viewprofile'", 
            type="submit",
            style=""" 
                max-width: 150px;
                margin: 1.5px 10px 0; 
                background-color: #F8F2EB; 
                color: #13171f;
                text-align: center; 
                border: 1px solid #F8F2EB;
                font-weight: bold;
                font-size: 18px;
            """
        ),
        Button(
            "Log out",
            onclick=f"window.location.href='/login'", 
            type="submit",
            style=""" 
                max-width: 150px;
                margin: 1.5px 10px 0; 
                background-color: #F8F2EB; 
                color: #13171f;
                text-align: center; 
                border: 1px solid #F8F2EB;
                font-weight: bold;
                font-size: 18px;
            """
        )
        
    ]

@rt('/')
def root():
    return Redirect('/login')

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
        enrollment = next((order.get_paid_enrollment() for order in account.get_account_order() 
                         if order.get_paid_enrollment().enroll_course().get_course_id() == course_id), None)
        progress = enrollment.get_progress() if enrollment else 0
        
        enrolled_course_card.append(
            Card(
                H3(course.get_course_name()),
                P(course.get_course_category(), style='color: #5996B2;'),
                P(course.get_course_detail()),
                P(f"Progress: {progress}%", 
                      style="color: #28a745; text-align: left;"),
                Button("Start Learning",
                    onclick=f"window.location.href='enrolled/{course_id}'",
                    style="""
                            background-color: #8D8883;
                            border-radius: 30px;
                            border: 1px solid #8D8883;
                            """
                            ),
                        style="""
                        min-width: 250px; 
                        margin: 10px;
                        border-radius: 30px;
                        """
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
                            onclick=f"window.location.href='course/{course.get_course_id()}'",
                            style="""
                            background-color: #8D8883;
                            border-radius: 30px;
                            border: 1px solid #8D8883;
                            """
                            ),
                        style="""
                        min-width: 250px; 
                        margin: 10px;
                        border-radius: 30px;
                        """
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
                            onclick=f"window.location.href='course/{course.get_course_id()}'",
                            style="""
                            background-color: #8D8883;
                            border-radius: 30px;
                            border: 1px solid #8D8883;
                            """
                            ),
                        style="""
                        min-width: 250px; 
                        margin: 10px;
                        border-radius: 30px;
                        """
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
                           onclick=f"window.location.href='course/{course.get_course_id()}'",
                    style="""
                            background-color: #8D8883;
                            border-radius: 30px;
                            border: 1px solid #8D8883;
                            """
                            ),
                        style="""
                        min-width: 250px; 
                        margin: 10px;
                        border-radius: 30px;
                        """
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
        Container(*navbar(account_id),
                  style="""
                display: flex;
                justify-content: center; 
                align-items: center;
                margin-bottom: 30px;
                background-color: #F8F2EB;
                border: 1px solid #f8f2eb;
                padding: 0px;          
                border-radius: 8px;    
                box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);  
            """),
        Titled("Welcome! {}".format(account.get_username()), 
               style="margin-top: 20px; text-align: center;"),
        
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
def view_course(account_id: str, course_id: str):
    course = test.get_course(course_id)
    chapter_num = len(course.get_chapter_list())
    lesson_num = sum([len(chapter.get_lesson_list()) for chapter in course.get_chapter_list()])
    creator_info = None
    if hasattr(course, 'get_creator') and course.get_creator():
        creator = course.get_creator()
        name, surname, age, desc = creator.view_profile()
        creator_info = Card(
            H5("Course Creator", style="color: #5C482C;"),
            P(f"{name} {surname}", style="font-weight: bold;"),
            P(desc if desc else "No description available"),
            style="margin-top: 15px; padding: 15px; border-top: 1px solid #eee; border-radius: 20px; background-color: #fff;"
        )
    
    return Container(
        Container(*navbar(account_id),
            style="""
                display: flex;
                justify-content: center; 
                align-items: center;
                margin-bottom: 30px;
                background-color: #F8F2Eb;
                border: 1px solid #f8f2eb;
                padding: 2px;         
                border-radius: 8px;    
                box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);  
            """
        ),
        Grid(
            Card(
                P(course.get_course_category(), style='color: #5996B2;'),
                H3(course.get_course_name(), style='color: #5C482C;'),
                P(course.get_course_detail()),
                Card(
                    H5("This course includes", style='text-align: center; color: #5C482C;'),
                    P("{} chapters".format(chapter_num)),
                    P("{} lessons".format(lesson_num)),
                    P("1 downloadable resource"),
                    P("Certificate of completion"),
                    style="margin-top: 20px; padding: 15px; border-top: 1px solid #eee; border-radius: 20px; background-color: #FFF;"
                ),
                creator_info if creator_info else None,
                style="background-color: #Fff; border-radius: 20px; padding: 15px;"
            ),
            Card(
                Img(
                    src="https://www.westminster.ac.uk/sites/default/public-files/styles/panel_image_1_2_768px_/public/general-images/epq-meme.jpg?itok=5b7ZyKpI",
                    alt="Course Image",
                    style="""
                        max-width: 100%;
                        height: auto;
                        border-radius: 8px;
                        margin-bottom: 20px;
                        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
                    """
                ),
                H4("{}฿".format(course.get_course_price()), style='color: #5C482C;'),
                Button(
                    "Add to Cart", 
                    hx_post=f"/{account_id}/addtocart/{course_id}",
                    hx_target="#cart-message",
                    style="""
                    background-color: #8D8883; 
                    color: white; 
                    border-radius: 30px;
                    border: 1px solid #8D8883;
                    """
                ),
                Div(id="cart-message"),
                style="""
                background-color: #fff; 
                border-radius: 20px;
                padding: 15px;
                """
            ),
            columns=2,
            style="gap: 20px; padding: 20px;"
        )
    )

@rt('/{account_id}/addtocart/{course_id}')
def add_course_to_cart(account_id: str, course_id: str):
    result = test.add_to_cart(account_id, course_id)
    if result == "Already enrolled in course":
        return Container(
            Card(
                Grid(
                    Button("×", 
                          hx_post="/close-popup",
                          hx_target="#cart-message",
                          style="""
                            background-color: #8D8883;
                            border-radius: 30px;
                            border: 1px solid #8D8883;
                            """),
                    P("You are already enrolled in this course!", style="color: #dc3545;"),
                    Button("View Course", 
                          onclick=f"window.location.href='/{account_id}/enrolled/{course_id}'",
                          style="""
                            background-color: #8D8883;
                            border-radius: 30px;
                            border: 1px solid #8D8883;
                            """),
                    columns=1
                ),
                style="position: relative; padding: 20px; border-radius: 30px"
            ),
            style="position: fixed; bottom: 20px; right: 20px; z-index: 1000; border-radius: 30px",
            id="cart-message"
        )
    elif result == "Course already in cart":
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
                          style="""
                            background-color: #8D8883;
                            border-radius: 30px;
                            border: 1px solid #8D8883;
                            """),
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
                          style="background: none; border-radius: 30px; font-size: 20px; position: absolute; right: 10px; top: 5px;"),
                    P("Course added to cart successfully!"),
                    Button("View Cart", 
                          onclick=f"window.location.href='/cart/{account_id}'",
                           style="""
                            background-color: #8D8883;
                            border-radius: 30px;
                            border: 1px solid #8D8883;
                            """),
                    columns=1
                ),
                style="position: relative; padding: 20px; border-radius: 30px"
            ),
            style="position: fixed; bottom: 20px; right: 20px; z-index: 1000; border-radius: 30px",
            id="cart-message"
        )
    return result

@rt('/close-popup')
def close_popup():
    return ""  # Returns empty string to clear the popup content

@rt('/cart/{account_id}')
def view_cart(account_id: str):
    cart = test.get_account_cart(account_id)
    cart_items = []
    for course in cart.get_content():
        cart_items.append(
            Card(
                Grid(
                    Div(
                        H3(course.get_course_name()),
                        P(f"{course.get_course_price()}฿")
                    ),
                    Button(
                        "Remove",
                        hx_post=f"/{account_id}/remove_from_cart/{course.get_course_id()}",
                        hx_target="#cart-container",  # Updated target
                         style="""
                            background-color: #8D8883;
                            border-radius: 30px;
                            border: 1px solid #8D8883;
                            """
                    ),
                    columns=2,
                    style="align-items: center; border-radius: 30px"
                ),
                style="margin-bottom: 10px; border-radius: 30px"
            )
        )
    
    total = cart.calculate_total()
    
    return Container(
        Container(*navbar(account_id),
            style="""
                display: flex;
                justify-content: center; 
                align-items: center;
                margin-bottom: 30px;
                background-color: #F8F2EB;
                border: 1px solid #f8f2eb;
                padding: 0px;          
                border-radius: 8px;    
                box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);  
            """
        ),
        Titled("Shopping Cart", style="margin-top: 20px; text-align: center; border-radius: 30px"),
        Div(
            H1("Your Cart"),
            Div(
                *cart_items,
                id="cart-items"
            ),
            P(f"Total: {total}฿", id="cart-total"),
            Button("Checkout with Credit card", 
                  onclick=f"window.location.href='/{account_id}/checkout/credit_card'",
                   style="""
                            background-color: #8D8883;
                            border-radius: 30px;
                            border: 1px solid #8D8883;
                            margin-right: 10px;
                            """),
            Button("Checkout by other ways", 
                  onclick=f"window.location.href='/{account_id}/checkout/others'",
                   style="""
                            background-color: #8D8883;
                            border-radius: 30px;
                            border: 1px solid #8D8883;
                            margin-right: 10px;
                            """),
            Button("Continue Shopping", 
                  onclick=f"window.location.href='/{account_id}/course/1'",
                   style="""
                            background-color: #fff;
                            color: #8D8883;
                            border-radius: 30px;
                            border: 1px solid #8D8883;
                            """),
            id="cart-container"
        )
    )

@rt('/{account_id}/remove_from_cart/{course_id}')
def remove_from_cart(account_id: str, course_id: str):
    result = test.remove_from_cart(account_id, course_id)
    cart = test.get_account_cart(account_id)
    cart_items = []
    for course in cart.get_content():
        cart_items.append(
            Card(
                Grid(
                    Div(
                        H3(course.get_course_name()),
                        P(f"{course.get_course_price()}฿")
                    ),
                    Button(
                        "Remove",
                        hx_post=f"/{account_id}/remove_from_cart/{course.get_course_id()}",
                        hx_target="#cart-container",
                         style="""
                            background-color: #ff6e6e;
                            color: #8D8883;
                            border-radius: 30px;
                            border: 1px solid #8D8883;
                            """
                    ),
                    columns=2,
                    style="align-items: center;"
                ),
                style="margin-bottom: 10px;"
            )
        )
    
    total = cart.calculate_total()
    
    return Div(
        H1("Your Cart"),
        Div(
            *cart_items if cart_items else [P("Your cart is empty.")],
            id="cart-items"
        ),
        P(f"Total: {total}฿", id="cart-total"),
        Button("Checkout with Credit card", 
              onclick=f"window.location.href='/{account_id}/checkout/credit_card'",
              style="""
                            background-color: #8d8883;
                            color: white;
                            border-radius: 30px;
                            border: 1px solid #8D8883;
                            """),
        Button("Checkout by other ways", 
              onclick=f"window.location.href='/{account_id}/checkout/others'",
               style="""
                            background-color: #8d8883;
                            color: white;
                            border-radius: 30px;
                            border: 1px solid #8D8883;
                            """),
        Button("Continue Shopping", 
              onclick=f"window.location.href='/{account_id}/course/1'",
               style="""
                            background-color: #fff;
                            color: #8D8883;
                            border-radius: 30px;
                            border: 1px solid #8D8883;
                            """),
        id="cart-container"
    )

@rt('/{account_id}/checkout/others')
def via_others(account_id: str):
    return Container(
        Container(*navbar(account_id),
                  style="""
                display: flex;
                justify-content: center; 
                align-items: center;
                margin-bottom: 30px;
                background-color: #F8F2EB;
                border: 1px solid #f8f2eb;
                padding: 0px;         
                border-radius: 8px;    
                box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);  
            """),
        H1("We don't have such thing, please pay with credit card. [I beg you]"),
        Form(
            Button("Back to Cart", style="""
                            background-color: #fff;
                            color: #8D8883;
                            border-radius: 30px;
                            border: 1px solid #8D8883;
                            """),
            method="/get",
            action=f"/cart/{account_id}"
        )
    )
    

@rt('/{account_id}/checkout/credit_card')
def via_credit_card(account_id: str):
    payment_method = test.get_account(account_id).get_account_payment_method()
    if (payment_method):
        return Container(
            Container(*navbar(account_id),
            style="""
                display: flex;
                justify-content: center; 
                align-items: center;
                margin-bottom: 30px;
                background-color: #F8F2EB;
                border: 1px solid #f8f2eb;
                padding: 0px;        
                border-radius: 8px;    
                box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);  
            """
        ),
            H1("Credit Card Payment"),
            Form(
                Button("Pay with saved card",  style="""
                            background-color: #fff;
                            color: #8D8883;
                            border-radius: 30px;
                            border: 1px solid #8D8883;
                            """),
                method="post",
                action=f"/{account_id}/pay"
            )
        )
    return Container(
        Container(*navbar(account_id),
            style="""
                display: flex;
                justify-content: center; 
                align-items: center;
                margin-bottom: 30px;
                background-color: #F8F2EB;
                border: 1px solid #f8f2eb;
                padding: 0px;     
                border-radius: 8px;    
                box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);  
            """
        ),
        H1("Credit Card Payment"),
        Form(
            Label("Card number:", id="card_number", style="border-radius: 30px;"),
            Input(placeholder = "Example: 1234 5678 1234 [If you paid once, you don't need to be worry, type anything.]",type="text", name="card_number", style="border-radius: 30px;"),
            Button("Pay",  style="""
                            background-color: #8d8883;
                            color: white;
                            border-radius: 30px;
                            border: 1px solid #8D8883;
                            """),
            method="post",
            action=f"/{account_id}/pay"
        )
    )

@rt('/{account_id}/pay')
def pay(account_id: str, card_number: str = None):
    global payment_id
    account = test.get_account(account_id)
    student = test.get_person(account_id)
    cart = account.get_cart()
    if account.get_account_payment_method() == None:
        card = test.create_card(payment_id, card_number)
        account.set_account_payment_method(card)
    else:
        card = account.get_account_payment_method()
    card.pay(cart.calculate_total())
    payment_id += 1
    for item in cart.get_content():
        enroll = test.create_enrollment(student, item, 0)
        order_item = test.create_order(account, enroll)
        account.add_account_order(order_item)
        test.create_noti(account, f"Successfully enrolled to {item.get_course_name()}.")
    cart.clear_item()
    
    return Container(
        Container(*navbar(account_id),
            style="""
                display: flex;
                justify-content: center; 
                align-items: center;
                margin-bottom: 30px;
                background-color: #F8F2EB;
                border: 1px solid #f8f2eb;
                padding: 0px;      
                border-radius: 8px;    
                box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);  
            """
        ),
        H1(f"Payment Successful! Your course(s) will be available in your account. Balance: {card.get_balance()}"),
        Button("Back to main", style="""
                            background-color: #8d8883;
                            color: white;
                            border-radius: 30px;
                            border: 1px solid #8D8883;
                            """), 
              onclick=f"window.location.href='/{account_id}/main'",
        )

@rt('/{account_id}/enrolled/{course_id}')
def view_enrolled_course(account_id: str, course_id: str):
    course = test.get_enrolled_course(account_id, course_id)
    if course:
        return Container(
            Container(*navbar(account_id),
            style="""
                display: flex;
                justify-content: center; 
                align-items: center;
                margin-bottom: 30px;
                background-color: #F8F2EB;
                border: 1px solid #f8f2eb;
                padding: 0px;       
                border-radius: 8px;    
                box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);  
            """
        ),
            Div(
                Button(
                    "← Back", 
                    onclick=f"window.location.href='/{account_id}/main'",
                    style="""
                            background-color: #8d8883;
                            color: white;
                            border-radius: 30px;
                            border: 1px solid #8D8883;
                            """
                ),
                style="""
                    margin-bottom: 40px;
                """
            ),
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
                                        hx_swap="innerHTML",
                                        style="""
                            background-color: #8d8883;
                            color: white;
                            border-radius: 30px;
                            border: 1px solid #8D8883;
                            """
                                    ),
                                    cls="lesson-box", style = "margin-bottom: 20px; "
                                ) for lesson in chapter.get_lesson_list()
                            ],
                            cls="chapter-box",
                            style="""
                            border-radius: 30px;
                            """
                        ) for chapter in course.get_chapter_list()
                    ],
                    cls="sidebar"
                ),
                columns=2
            ),
            style="padding: 20px;"
        )
    return H1("Course not found", style="color: #dc3545;")

@rt('/{account_id}/lesson/{lesson_id}')
def view_lesson(account_id: str, lesson_id: str):
    account = test.get_account(account_id)
    try:
        course_id, chapter_id, lesson_num = lesson_id.split('-')
        lesson = account.view_lesson(lesson_id)
        
        if lesson:
            enrollment = next((order.get_paid_enrollment() for order in account.get_account_order() 
                            if order.get_paid_enrollment().enroll_course().get_course_id() == course_id), None)
            
            if enrollment:
                course = enrollment.enroll_course()
                total_lessons = sum(len(chapter.get_lesson_list()) for chapter in course.get_chapter_list())
                current_progress = enrollment.get_progress()
                
                if not enrollment.is_lesson_completed(lesson_id):
                    progress_per_lesson = 100 / total_lessons
                    completed_lessons = len(enrollment.get_completed_lessons()) + 1  # Include current lesson
                    new_progress = round((completed_lessons * progress_per_lesson))
                    new_progress = 100 if completed_lessons == total_lessons else new_progress
                    
                    enrollment.set_progress(new_progress)
                    enrollment.mark_lesson_complete(lesson_id)

                else:
                    new_progress = current_progress
            
            return Container(
                H2(lesson.get_lesson_name()),
                Card(
                    P(lesson.get_lesson_content()),
                    style="margin-bottom: 20px; border-radius: 20px; padding: 20px;"
                ),
                Div(
                    P(f"Progress: {new_progress}%", 
                      style="color: #28a745; text-align: left;")
                    ),
                    id="completion-status"
                )
        return P("Lesson not found", style="color: #dc3545;")
    except ValueError:
        return P("Invalid lesson ID format", style="color: #dc3545;")
    
@rt('/login', methods=['GET'])
def get_login():
    return Container(
        Grid(
            # Left side - Image
            Container(
                Img(
                    src = "https://media-hosting.imagekit.io//28ea30b4fb964332/Let%E2%80%99s%20continue%20your%20learning%20journey!.png?Expires=1836407268&Key-Pair-Id=K2ZIVPTIP2VGHC&Signature=q~-dCTzJcwr4HbDbvynAg7O8ADzbo8fhgnKq56YasNbE1ekdMt-QoRsizYZEz6yhU9mydD07WQWYzxVbTbvmeb5g4WzPOHxnJ6vI9ObYBYSTKE-JYrmIAuRQG9yp4M8b-4~v9d1d4F8~BvxwKQ5WsE-idpBTZBM052F3rlPBdqwxl7vdjtsgaOWouvyly6ni-UhAi~WdTi4LHfKsf1UZuONgVDezFnoXDmahtiuNdsHtjhsmiiMLtFsB52R-8uytl5np7kfkxfm2fOFqihEbJZDyxsvgrmfW5aJRGbA1ntxTVJjAWWKlpiy2dMgprShSXywyJp~or91Gelw~MaqGCg__",
                    alt="Learning Journey",
                    style="""
                        width: auto;
                        height: 450px;
                        object-fit: cover;
                    """
                ),
                style="""
                    background-color: #FFFFFF;
                    height: 100vh;
                    width: 100%;
                    display: flex;
                    align-items: center;
                    justify-content: center;
                """
            ),
            
            # Right side - Login Form
            Container(
                Container(
                    Img(
                        src="https://media-hosting.imagekit.io//3953e1bceac64d68/logo.png?Expires=1836319434&Key-Pair-Id=K2ZIVPTIP2VGHC&Signature=n-HMFmK8VEjrAPtl-5R8~TtBvrjN6E0yc1e-v65t~YQutAJML4vFpnGYNpnH2RODKn-eqCRbbq61eHc6QU~4gi~enp4il~UJENpLKl63z~EXrdIBVp3SHYXi5WzvcQNraMM1~0Xyt81zKJr4bkSS3zYYvn4dlIluX8fcFSIspDQpe6HRI8nqpWH9oiyytIbaBv6yrOrBID46Q2uFG6tt-UcCSAZ45ry0qBFgVV55LDlyn~lJOk8uFU4c-2zIzZWc05u0Fksq3sJL9Kt99GxzQMjjX89eEg3UKGb4B5wVQD58DCw0VWJGnVEc6loq5FjEeEWoBiRgXBDD1B0r-QPf9A__",
                        alt="Logo",
                        style="max-width: 100px; margin-bottom: 30px;"
                    ),
                    H1("Login", 
                        style="text-align: center; margin-bottom: 40px; color: #5C482C;"
                    ),
                    Form(
                        Div(
                            Label("Username", 
                                Input(
                                    type="text", 
                                    id="username",
                                    name="username",
                                    required=True,
                                    placeholder="Enter your username",
                                    style="""
                                    width: 100%;
                                    border-radius: 30px;
                                    """
                                    
                                )
                            ),
                            Label("Password", 
                                Input(
                                    type="password", 
                                    id="password",
                                    name="password",
                                    required=True,
                                    placeholder="Enter your password",
                                    style="""
                                    width: 100%;
                                    border-radius: 30px;
                                    """
                                )
                            ),
                            style="""
                            max-width: 300px;
                            item-align: center;
                            margin: 0 auto;
                            """
                        ),
                        Button(
                            "Login", 
                            type="submit",
                            style=""" 
                                width: 200px;
                                margin: 40px auto 0;
                                display: block;
                                background-color: #8D8883; 
                                color: white;
                                padding: 10px 0;
                                border: none;
                                border-radius: 30px;
                            """
                        ),
                        method="post",
                        action="/login",
                        style="width: 100%;"
                    ),
                    style="""
                        width: 100%;
                        min-width: 400px;
                        margin: 0 auto;
                        text-align: center;
                    """
                ),
                style="""
                    background-color: #F8F2EB;
                    height: 100vh;
                    display: flex;
                    align-items: center;
                    justify-content: center;
                    padding: 20px;
                """
            ),
            columns=2,
            style="margin: 0; padding: 0; width: 100vw; height: 100vh;"
        ),
        style="margin: 0; padding: 0; max-width: 100vw; height: 100vh; overflow: hidden;"
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

    return Container(
        Container(*navbar(account_id),
            style="""
                display: flex;
                justify-content: center; 
                align-items: center;
                margin-bottom: 30px;
                background-color: #F8F2EB;
                border: 1px solid #f8f2eb;
                padding: 0px;        
                border-radius: 8px;    
                box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);  
            """
        ),
        Titled("Search Online Courses", style="text-align: center;"),
        Form(
            Input(id="search", placeholder="Search courses...", hx_get=f"/{account_id}/searchresult", target_id="results", hx_trigger="keyup delay:500ms change", style="width: 100%; border-radius: 30px;"),
            style="""
            margin-bottom: 20px;
            text-align: center;
            """
        ),
        Div(
            *[
                A(
                    Card(H3(c.get_course_name()), P(c.get_course_detail()), P(f"Category: {c.get_course_category()}"), H6(f"{c.get_course_price()}฿", style="color: #000000"), style="cursor: pointer; border-radius: 30px;"),
                    href=("/" + account_id + f"/course/{c.get_course_id()}"),
                    style="""
                    text-decoration: none; 
                    color: inherit;
                    border-radius: 30px;
                    """
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
                Card(H3(c.get_course_name()), P(c.get_course_detail()), P(f"Category: {c.get_course_category()}"), H6(f"{c.get_course_price()}฿", style="color: #000000"), style="cursor: pointer; border-radius: 30px;"),
                href=("/" + account_id + f"/course/{c.get_course_id()}"),
                style="text-decoration: none; color: inherit;"
            )
            for c in results
        ] if results else [P("No courses found.")],
        style="margin-top: 10px;"
    ) 

@rt('/{account_id}/editprofile', methods=['GET'])
def get_editprofile(account_id: str):
    return Container(
        Container(*navbar(account_id),
            style="""
                display: flex;
                justify-content: center; 
                align-items: center;
                margin-bottom: 30px;
                background-color: #F8F2EB;
                border: 1px solid #f8f2eb;
                padding: 0px;        
                border-radius: 8px;    
                box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);  
            """
        ),
        H1("Edit Profile", style="text-align: center; margin-bottom: 20px;"),
        Form(
            Div(
                Label("Username", 
                    Input(
                        type="text", 
                        id="username",
                        name="username",
                        required=True,
                        placeholder="Enter your new Username",
                        style="width: 100%; border-radius: 30px;"
                    )
                ),
                Label("New Password", 
                    Input(
                        type="text", 
                        id="password",
                        name="password",
                        required=True,
                        placeholder="Enter your new Password",
                        style="width: 100%; border-radius: 30px;"
                    )
                ),
                Label("Confirm Password", 
                    Input(
                        type="text", 
                        id="confirm_password",
                        name="confirm_password",
                        required=True,
                        placeholder="Confirm your Password",
                        style="width: 100%; border-radius: 30px;"
                    )
                ),
                Label("Name", 
                    Input(
                        type="text", 
                        id="name",
                        name="name",
                        required=True,
                        placeholder="Enter your new Name",
                        style="width: 100%; border-radius: 30px;"
                    )
                ),
                Label("Surname", 
                    Input(
                        type="surname", 
                        id="surname",
                        name="surname",
                        required=True,
                        placeholder="Enter your new Surname",
                        style="width: 100%; border-radius: 30px;"
                    )
                ),
                Label("Description", 
                    Input(
                        type="description", 
                        id="description",
                        name="description",
                        required=True,
                        placeholder="Enter your new Description",
                        style="width: 100%; border-radius: 30px;"
                    )
                ),
                style="max-width: 300px;"

            ),
            
            Button(
                "Submit", 
                type="submit",
                style=""" 
                    max-width: 200px;
                    margin: 20px auto 0;
                    display: block;
                    background-color: #8d8883;
                    border-radius: 30px;
                    border: 1px solid #8d8883;
                    color: white;
                """
            ),
            
            method="post",
            action="editprofile",
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
@rt('/{account_id}/editprofile', methods=['POST'])
def post_editprofile(account_id: str, username: str, password: str, confirm_password: str, name: str, surname: str, description: str):  # Note: category is now a list
    account = test.edit_profile(account_id, username, password, confirm_password, name, surname, description)
    if account:
        return Container(
            Container(*navbar(account_id),
            style="""
                display: flex;
                justify-content: center; 
                align-items: center;
                margin-bottom: 30px;
                background-color: #F8F2EB;
                border: 1px solid #f8f2eb;
                padding: 0px;         
                border-radius: 8px;    
                box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);  
            """
        ),
            H1("Edit Profile Successfully", style="text-align: center; color: green;"),
            A("Go back", href=f"/{account_id}/viewprofile", style="display: block; text-align: center; margin-top: 20px;")
        )
    else: 
        return Container(
            Container(*navbar(account_id),
            style="""
                display: flex;
                justify-content: center; 
                align-items: center;
                margin-bottom: 30px;
                background-color: #F8F2EB;
                border: 1px solid #f8f2eb;
                padding: 0px;    
                border-radius: 8px;    
                box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);  
            """
        ),
            H1("Edit Profile Failed", style="text-align: center; color: red;"),
            A("Go back", href=f"/{account_id}/editprofile", style="display: block; text-align: center; margin-top: 20px;")
        )


@rt('/{account_id}/addnewcourse', methods=['GET'])
def get_addnewcourse(account_id: str):
    return Container(
        Container(*navbar(account_id),
            style="""
                display: flex;
                justify-content: center; 
                align-items: center;
                margin-bottom: 30px;
                background-color: #F8F2EB;
                border: 1px solid #f8f2eb;
                padding: 0px;         
                border-radius: 8px;    
                box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);  
            """
        ),
        H1("Add Course", style="text-align: center; margin-bottom: 20px;"),
        Form(
            Grid(
                # Left side - Course Details
                Card(
                    H2("Course Details", style="color: #5C482C; margin-bottom: 20px;"),
                    Div(
                        Label("Course Name", 
                            Input(type="text", id="name", name="name", required=True,
                                placeholder="Enter your course name", style="width: 100%; border-radius: 30px;")
                        ),
                        Label("Course Detail", 
                            Input(type="text", id="detail", name="detail", required=True,
                                placeholder="Enter your course detail", style="width: 100%; border-radius: 30px;")
                        ),
                        Label("Course Price", 
                            Input(type="text", id="price", name="price", required=True,
                                placeholder="Enter your Course Price", style="width: 100%; border-radius: 30px;",
                                pattern="[0-9]{2,}")
                        ),
                        Label("Course ID", 
                            Input(type="text", id="course_id", name="course_id", required=True,
                                placeholder="Enter your Course ID", style="width: 100%; border-radius: 30px;")
                        ),
                        Div(
                            "Course Category",
                            Div(
                                Label(Input(type="radio", id="category_programming", name="category", 
                                          value="Programming", required=True), "Programming"),
                                Label(Input(type="radio", id="category_pet", name="category",
                                          value="Pet", required=True), "Pet"),
                                Label(Input(type="radio", id="category_cooking", name="category",
                                          value="Cooking", required=True), "Cooking"),
                                style="margin-top: 10px;"
                            ),
                            style="margin-top: 20px;"
                        ),
                        style="width: 100%;"
                    ),
                    style="background-color: #fff; padding: 20px; border-radius: 15px;"
                ),

                # Right side - Chapters and Lessons
                Card(
                    H2("Course Content", style="color: #5C482C; margin-bottom: 20px;"),
                    Div(
                        # Chapter 1
                        H3("Chapter 1", style="color: #5C482C;"),
                        Label("Chapter 1 Lesson 1 Name",
                            Input(type="text", name="ch1_l1_name", required=True,
                                 placeholder="Enter lesson name", style="width: 100%; border-radius: 30px;")
                        ),
                        Label("Chapter 1 Lesson 1 Content",
                            Textarea(name="ch1_l1_content", required=True,
                                    placeholder="Enter lesson content", style="width: 100%; border-radius: 15px;")
                        ),
                        Label("Chapter 1 Lesson 2 Name",
                            Input(type="text", name="ch1_l2_name", required=True,
                                 placeholder="Enter lesson name", style="width: 100%; border-radius: 30px;")
                        ),
                        Label("Chapter 1 Lesson 2 Content",
                            Textarea(name="ch1_l2_content", required=True,
                                    placeholder="Enter lesson content", style="width: 100%; border-radius: 15px;")
                        ),

                        # Chapter 2
                        H3("Chapter 2", style="color: #5C482C; margin-top: 20px;"),
                        Label("Chapter 2 Lesson 1 Name",
                            Input(type="text", name="ch2_l1_name", required=True,
                                 placeholder="Enter lesson name", style="width: 100%; border-radius: 30px;")
                        ),
                        Label("Chapter 2 Lesson 1 Content",
                            Textarea(name="ch2_l1_content", required=True,
                                    placeholder="Enter lesson content", style="width: 100%; border-radius: 15px;")
                        ),
                        Label("Chapter 2 Lesson 2 Name",
                            Input(type="text", name="ch2_l2_name", required=True,
                                 placeholder="Enter lesson name", style="width: 100%; border-radius: 30px;")
                        ),
                        Label("Chapter 2 Lesson 2 Content",
                            Textarea(name="ch2_l2_content", required=True,
                                    placeholder="Enter lesson content", style="width: 100%; border-radius: 15px;")
                        ),
                        style="width: 100%;"
                    ),
                    style="background-color: #fff; padding: 20px; border-radius: 15px;"
                ),
                columns=2,
                style="gap: 20px; width: 100%; max-width: 1200px;"
            ),
            Button("Submit", type="submit",
                style="""
                    max-width: 200px; 
                    margin: 20px auto 0; 
                    display: block; 
                    background-color: #8D8883; 
                    color: white; 
                    border-radius: 30px;
                    border: 1px solid #8D8883;
                """),
            method="post",
            action=f"/{account_id}/addnewcourse",
            style="padding: 20px; width: 100%;"
        ),
        style="""
            display: flex; 
            flex-direction: column; 
            align-items: center; 
            min-height: 100vh;
            padding: 20px;
        """
    )

@rt('/{account_id}/addnewcourse', methods=['POST'])
def post_addnewcourse(account_id: str, course_id: str, name: str, detail: str, 
                     price: int, category: List[str],
                     ch1_l1_name: str, ch1_l1_content: str,
                     ch1_l2_name: str, ch1_l2_content: str,
                     ch2_l1_name: str, ch2_l1_content: str,
                     ch2_l2_name: str, ch2_l2_content: str):
    try:
        teacher = None
        for t in test.get_teacher_list():
            if t.get_account().check_account_id(account_id):
                teacher = t
                break
        
        if not teacher:
            return Container(
                H1("Add Course Failed", style="text-align: center; color: red;"),
                P("Only teachers can add courses."),
                A("Go back", href=f"/{account_id}/main")
            )
            
        category_str = category[0] if category else ""
        test.add_course_list(course_id, name, detail, price, category_str, teacher)
        new_course = test.get_course(course_id)
        
        if new_course:
            # Add Chapter 1
            chapter1 = new_course.create_chapter("1")
            chapter1.add_lesson("1", ch1_l1_name, ch1_l1_content, "", "")
            chapter1.add_lesson("2", ch1_l2_name, ch1_l2_content, "", "")
            new_course.add_chapter(chapter1)

            # Add Chapter 2
            chapter2 = new_course.create_chapter("2")
            chapter2.add_lesson("1", ch2_l1_name, ch2_l1_content, "", "")
            chapter2.add_lesson("2", ch2_l2_name, ch2_l2_content, "", "")
            new_course.add_chapter(chapter2)

            return Container(
               Container(*navbar(account_id),
            style="""
                display: flex;
                justify-content: center; 
                align-items: center;
                margin-bottom: 30px;
                background-color: #F8F2EB;
                border: 1px solid #f8f2eb;
                padding: 0px;         
                border-radius: 8px;    
                box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);  
            """
        ),
                H1("Add Course Successfully", style="text-align: center; color: green;"),
                P("Course has been added successfully.")
            )
        else:
            return Container(
                Container(*navbar(account_id),
            style="""
                display: flex;
                justify-content: center; 
                align-items: center;
                margin-bottom: 30px;
                background-color: #F8F2EB;
                border: 1px solid #f8f2eb;
                padding: 0px;         
                border-radius: 8px;    
                box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);  
            """
        ),
                H1("Add Course Failed", style="text-align: center; color: red;"),
                A("Go back", href=f"/{account_id}/addnewcourse",
                  style="display: block; text-align: center; margin-top: 20px;")
            )
    except Exception as e:
        return Container(
            H1("Add Course Failed", style="text-align: center; color: red;"),
            P(f"Error: {str(e)}"),
            A("Go back", href=f"/{account_id}/addnewcourse")
        )
        
@rt('/{account_id}/viewprofile', methods=['GET'])
def viewprofile(account_id: str):
    account_obj = test.get_account(account_id)
    is_teacher = False
    
    for teacher in test.get_teacher_list():
        if teacher.get_account().check_account_id(account_id):
            is_teacher = True
            results = teacher
            break
    else:
        results = test.get_person(account_id)
    
    name, surname, age, desc = results.view_profile()
    
    buttons = [
        Button(
            "Edit Profile",
            onclick=f"window.location.href='/{account_id}/editprofile'", 
            type="submit",
            style=""" 
                max-width: 200px;
                margin: 20px auto 0;
                display: block;
                background-color: #8d8883; 
                border-radius: 30px;
                border: 1px solid #8d8883;
                color: white;
            """
        )
    ]
    if is_teacher:
        buttons.append(
            Button(
                "Create Course",
                onclick=f"window.location.href='/{account_id}/addnewcourse'", 
                type="submit",
                style=""" 
                    max-width: 200px;
                    margin: 20px auto 0;
                    display: block;
                    background-color: #fff; 
                    border-radius: 30px;
                    border: 1px solid #8d8883;
                    color: #13171f;
                """
            )
        )
    
    return Container(
        Container(*navbar(account_id),
            style="""
                display: flex;
                justify-content: center; 
                align-items: center;
                margin-bottom: 30px;
                background-color: #F8F2EB;
                border: 1px solid #f8f2eb;
                padding: 0px;
                border-radius: 8px;    
                box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);  
            """
        ),
        H1("View Profile", style="text-align: center; align-items: Top; margin-bottom: 20px;"),
        Container(
            H4(f"Name: {name}"),
            H4(f"Surname: {surname}"),
            H4(f"Age: {age}"),
            H4(f"Description: {desc}"),
            H4(f"Role: {'Teacher' if is_teacher else 'Student'}", style="color: #5996B2;"),
            style="""
                display: flex;
                flex-direction: column;
                justify-content: center;
                align-items: center;
                min-height: 45vh;
            """
        ),
        *buttons
    )
    
    
@rt("/{account_id}/faq")
def faq(account_id: str):
    faq_items = [
        Container(
            H3(f"{faq.get_faq_question()}?"),
            Label(f"Answer: {faq.get_faq_answer()}", style="border-redius: 30px;"),
            Form(
                Button("Add/Change answer", type = "add_answer", 
                       style = """
                        background-color: #8d8883; 
                        border-radius: 30px;
                        border: 1px solid #8d8883;"""),
                method = "post",
                action = f"/{account_id}/add_faq_answer/{faq.get_faq_id()}"
            ),
            style = "border: 30px #8d8883; padding: 10px; margin-bottom: 10px; border-radius: 30px; border: 1px solid #8d8883;"
        ) for faq in test.get_faq_list()
    ]
    return Container(
        Container(*navbar(account_id),
            style="""
                display: flex;
                justify-content: center; 
                align-items: center;
                margin-bottom: 30px;
                background-color: #F8F2EB;
                border: 1px solid #f8f2eb;
                padding: 0px;         
                border-radius: 8px;    
                box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);  
            """
        ),
        *faq_items,
        Form(
            Button("Contact us", type="routing", 
                   style = """
                        background-color: #8d8883; 
                        border-radius: 30px;
                        border: 1px solid #8d8883;"""),
            method = "post",
            action = f"/{account_id}/support",
        )
    )
    
    
@rt("/{account_id}/add_faq_answer/{faq_id}")
def add_answer(account_id: str, faq_id:int):
    for faq in test.get_faq_list():
        if faq.get_faq_id() == faq_id:
            return Container(
                Container(*navbar(account_id),
            style="""
                display: flex;
                justify-content: center; 
                align-items: center;
                margin-bottom: 30px;
                background-color: #F8F2EB;
                border: 1px solid #f8f2eb;
                padding: 0px;         
                border-radius: 8px;    
                box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);  
            """
        ),
                H1("Add answer"),
                Form(
                    H3(f"{faq.get_faq_question()}?"),
                    Label(f"Answer: {faq.get_faq_answer()}"),
                    Input(type="text", name="faq_ans", id="faq_ans", placeholder="Enter answer", required=True, pattern="[A-Za-z ]{2,}", style="border-radius: 30px;"),
                    Button("Done", type="submit", style = """
                        background-color: #8d8883; 
                        border-radius: 30px;
                        border: 1px solid #8d8883;"""),
                    method="post",
                    action=f"/{account_id}/faq_answered/{faq.get_faq_id()}"
                )
            )
            

@rt("/{account_id}/faq_answered/{faq_id}")
def append_answer(account_id: str, faq_id:int, faq_ans:str):
    for faq in test.get_faq_list():
        if faq.get_faq_id() == faq_id:
            faq.add_faq_answer(faq_ans)
    return Container(
        Container(*navbar(account_id),
            style="""
                display: flex;
                justify-content: center; 
                align-items: center;
                margin-bottom: 30px;
                background-color: #F8F2EB;
                border: 1px solid #f8f2eb;
                padding: 0px;         
                border-radius: 8px;    
                box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);  
            """
        ),
        H1("Answer added"),
        Form(
            Button("Back to FAQ", type = "home", style = """
                        background-color: #8d8883; 
                        border-radius: 30px;
                        border: 1px solid #8d8883;"""),
            method = "/get",
            action = f"/{account_id}/faq"
        )
    )
     

@rt("/{account_id}/support")
def support(account_id: str):
    return Container(
        Container(*navbar(account_id),
            style="""
                display: flex;
                justify-content: center; 
                align-items: center;
                margin-bottom: 30px;
                background-color: #F8F2EB;
                border: 1px solid #f8f2eb;
                padding: 0px;         
                border-radius: 8px;    
                box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);  
            """
        ),
        H1("Support"),
        Form(
            Label("Customer support", Input(type = "text", id = "faq_question", placeholder = "Enter your question", required = True, pattern = "[A-Za-z ]{2,}", style = "border-radius: 30px;")),
            Button("Submit question", type = "submit", style = """
                        background-color: #8d8883; 
                        border-radius: 30px;
                        border: 1px solid #8d8883;"""),
            method = "post",
            action = f"/{account_id}/submit_support"
        
        )
    )
    

@rt("/{account_id}/submit_support")
def submit_support(account_id: str, faq_question:str):
    global faq_id_counter
    for faq in test.get_faq_list():
        if faq_question == faq.get_faq_question():
            if faq.get_faq_answer() is not None:
                return Container(
                    Container(*navbar(account_id),
                    H1("There is already an answer to this question."),
                    Form(
                        Button("Back to FAQ", type = "home"),
                        method = "/get",
                        action = f"/{account_id}/faq"
                    )
                    )
                )
            return Container(
                Container(*navbar(account_id),
            style="""
                display: flex;
                justify-content: center; 
                align-items: center;
                margin-bottom: 30px;
                background-color: #F8F2EB;
                border: 1px solid #f8f2eb;
                padding: 0px;         
                border-radius: 8px;    
                box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);  
            """
        ),
                H1("There is this question already in the FAQ."),
                Form(
                    Button("Back to FAQ", type = "home",style = """
                        background-color: #8d8883; 
                        border-radius: 30px;
                        border: 1px solid #8d8883;"""),
                    method = "/get",
                    action = f"/{account_id}/faq"
                )
            )
            
    test.add_faq_list(faq_id_counter, faq_question)
    faq_id_counter += 1
    return Container(
        Container(*navbar(account_id),
            style="""
                display: flex;
                justify-content: center; 
                align-items: center;
                margin-bottom: 30px;
                background-color: #F8F2EB;
                border: 1px solid #f8f2eb;
                padding: 0px;         
                border-radius: 8px;    
                box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);  
            """
        ),
        H1("Thank you for contacting us"),
        Form(
            Button("Back to FAQ", type = "home",style = """
                        background-color: #8d8883; 
                        border-radius: 30px;
                        border: 1px solid #8d8883;"""),
            method = "/get",
            action = f"/{account_id}/faq"
        )
    )
    

@rt('/{account_id}/notification')
def notification(account_id: str):
    account = test.get_account(account_id)
    acc_noti = account.get_account_noti()
    noti = acc_noti.get_notification()
    noti = [
        Container(
            H3(f"{notification}"),
            style = "border: 1px #8d8883; padding: 10px; margin-bottom: 10px;"
        ) for notification in noti
    ]
    return Container(
        Container(*navbar(account_id),
            style="""
                display: flex;
                justify-content: center; 
                align-items: center;
                margin-bottom: 30px;
                background-color: #F8F2EB;
                border: 1px solid #f8f2eb;
                padding: 0px;
                border-radius: 8px;    
                box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);  
            """
        ),
        H1("Notification", style="margin-top: 20px; text-align: center;"),
        *noti,
        Form(
            Button("Back to main", type = "home",style = """
                        background-color: #8d8883; 
                        border-radius: 30px;
                        border: 1px solid #8d8883;"""),
            method = "/get",
            action = f"/{account_id}/main",
            style= "margin-bottom: 10px;"
        ),
        Form(
            Button("Clear notification", type = "clear_notification",style = """
                        background-color: #8d8883; 
                        border-radius: 30px;
                        border: 1px solid #8d8883;"""),
            method = "/get",
            action = f"/{account_id}/clear_notification"
        )
    )
    

@rt('/{account_id}/clear_notification')
def clear_notification(account_id: str):
    account = test.get_account(account_id)
    acc_noti = account.get_account_noti()
    acc_noti.delete_notification()
    return Container(
        Container(*navbar(account_id),
            style="""
                display: flex;
                justify-content: center; 
                align-items: center;
                margin-bottom: 30px;
                background-color: #F8F2EB;
                border: 1px solid #f8f2eb;
                padding: 0px;         
                border-radius: 8px;    
                box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);  
            """
        ),

        H1("Notifications cleared"),
        Form(
            Button("Back to main", type = "home",style = """
                        background-color: #8d8883; 
                        border-radius: 30px;
                        border: 1px solid #8d8883;
                        margin: 0 0 0 10px;
                   """),
            method = "/get",
            action = f"/{account_id}/main",
        ),
    ),

serve()