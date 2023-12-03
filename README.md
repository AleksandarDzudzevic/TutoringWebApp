# CS_IA_Aleks TutorFlix web application
![](https://github.com/AleksandarDzudzevic/CS_IA_Aleks/blob/main/Screenshot%202023-09-02%20at%2014.18.57.png)
Fig.1 shows the picture created for TutorFlix using Dream AI[^1] generated on the prompt "Art representing Tutoring services, presenting a tutor and a student".

## 1. [Criteria A: Planning](#criteria-a-planning)

1.1. [Definition of the problem](#problem-definition)

1.2. [Rationale for a proposed solution](#rationale-for-proposed-solution)

1.3. [Design Statement](#design-statement)

1.4. [Success Criteria](#success-criteria)
## 2. [Criteria B: Design](#criteria-b-design)

2.1[System Diagram](#system-diagram)

2.2. [Wireframe Diagram](#wireframe-diagram)

2.3. [ER Diagram](#er-diagram)

2.4. [UML Diagram](#uml-diagram)

2.5. [Flow Diagram](#flow-diagram)

2.6. [Test plan](#test-plan)

2.7. [Record of tasks](#record-of-tasks)

## 3. [Criteria C: Development](#criteria-c-development)

3.1.[Tools and techniques used](#tools-and-techniques-used)

3.2. [Sources](#sources)

3.3[Development](#development)

## 4. [Criteria D: Functionality](#criteria-d-functionality)
 
4.1 [SNS Video](#video-showcase)

## 5. [Criteria E: Evaluation](#criteria-e-evaluation)

5.1 [Table of Evaluation](#evaluation-table)

## 6. [Appendix](#Appendix)
# Criteria A: Planning


## Problem Definition
As a student, I often struggled with not having a place to find the right tutor. Just like many, I ended up going with the tutors recommended by friends or relatives, which usually turned out to be better at selling their services than actually teaching and that bothered me. I also struggled with finding ones that lived close to me. I got contacted by my client, a teacher, who saw a similar issue and explained that in the past he tried using online selling platforms such as eBay or Craigslist to post his advertisement for tutoring services, but was unsuccessful as the students who wanted to find him couldn't due to many other tutors teaching the same subject. To change this, my client requested a tutoring platform where students can find tutors that are well-ranked not well-advertised, live close to them, and are within their price range so that tutoring services can finally be level that they are supposed to. 

## Rationale for Proposed Solution
To revolutionize tutoring services and allow the best-ranked tutors to get the most exposure, instead of the ones with the best advertising, I have decided to develop a web application for my client that will serve as an inclusive platform that will connect highly ranked tutors and students seeking their help, allowing the most optimal learning experience.

## Design Statement
I will design an innovative web application that will make connecting tutors and students easier. The development will be done using the software Flask framework in Python, CSS, and HTML. It will take around 10 weeks to develop and will be evaluated according to the success criteria stated below by the client.

### Why Web Application?
Web applications are more adequate when developing a platform that offers services like the one I am making because it allows easier access to many different tutors across multiple devices without the need for downloading and installing an application. With a constant addition of new tutors across different subjects, the web application doesn't ask for constant updates. Students who are looking for a tutor can access the website through a web browser on their desktop or mobile devices. This increases the potential user number and makes it easier for users to share their experience with tutors with others, allowing high-quality tutors to jump out from the rest. Lastly, web applications can be maintained easily. They can be optimized for search engines, making it easier for new users to discover and join this platform both as tutors and as students, depending on their needs.

### Why Python?
Python contains many versatile features, which make it a better choice compared to other languages, for example, PHP[^2]. Python's Flask framework is ideal for developing a website for a tutoring platform due to its lightweight and flexible nature [^3]. It offers a range of libraries and extensions, making it easier to implement complex features when compared to its competitors such as PHP or ruby [^4]. This is essential when creating a complex web application such as a tutoring platform. Additionally, Python has an active community of developers making it easy to expand its features in the future with their help.

### Why SQL?
To store the vast amounts of data needed for an online tutoring platform, a reliable and efficient database is essential. While non-SQL databases can be an option, SQL databases offer several advantages that make them better suited for this purpose. The main advantage of SQL databases is their ability to handle large amounts of data efficiently, thanks to their relational structure[^5]. This makes it easier to manage and query the data of students and tutors. This feature also ensures that data is consistent and accurate, as it is subject to strong data integrity constraints[^6]. 

## Success Criteria
1) The tutoring platform will have a secure register system, unique for student and tutor accounts with access to different features on the platform.
>[ I often struggled with not having a place to find the right tutor/I usually just got their phone number as a contact]
2) The tutoring platform will contain useful filter options such as search by tutor name and country and for posts subject, word search, and price range.
>[I also struggled with finding ones that lived close to me, and as I usually just got their phone number as a contact, I wasn't aware of who they were and how much they charged]
3) The tutoring platform will allow tutor accounts to upload multiple tutoring posts for different subjects and topics that they offer to teach, all on one account.
>[in the past he tried using online selling platforms such as eBay or Craigslist to post his advertisement for tutoring services, but was unsuccessful]
4) The tutoring platform will have a grading system for tutors where students can rate their experience with the tutor.
> Students who wanted to find him couldn't due to many other tutors teaching the same subject.
5) The tutoring platform will allow students to see all posts by a specific tutor or reviews made by a specific student.
>[was unsuccessful as the students that tried to find him couldn't due to many other tutors teaching the same subject.]
6) The tutoring platform will have leaderboards for tutors with the most reviews and best grades, and be constantly updated to ensure that good and reliable tutors gain the most exposure.
>[ (Tutors) usually turned out to be better at selling their services than actually teaching]

Criteria A was established with the help of the data gathered through a questionnaire. (referred to in the [appendix](#appendix))

# Criteria B: Design
## System Diagram
![](https://github.com/AleksandarDzudzevic/CS_IA_Aleks/blob/main/IA%20System%20DiagramVersionLast.png)
Fig.2 shows the system diagram of the online tutoring platform which visually represents the interconnected components, modules, and their interactions, providing a comprehensive overview of the application's architecture and helping in understanding the overall structure of Tutorflix.
## Wireframe Diagram
![](https://github.com/AleksandarDzudzevic/CS_IA_Aleks/blob/main/Wireframe%20IA.png)
Fig.3 Shows the wireframe diagram of the web application for the Tutorflix platform. All of the main pages are connected through the navigation bar (indicated as "NAVIGATION BAR"), which was part of the base template used for the Citio website, and within that indicated with red color are the features available to both account types (students and tutors). A token is required to move around the website, and it can only be received when a user passes login successfully, which is why that is the starting location when accessing the web application. 
## ER Diagram 
![](https://github.com/AleksandarDzudzevic/CS_IA_Aleks/blob/main/ER%20DIAGRAM_IA_Final.png)
Fig.4 Shows the ER diagram of the online tutoring platform, which represents the database structure of the web application and its interconnectivity and relationships between users, posts, and review classes. 
## UML Diagram
![](https://github.com/AleksandarDzudzevic/CS_IA_Aleks/blob/main/UML_IA.png)
Fig.5 shows the class used for manipulating the database, used for the website application during the process of sending and receiving query requests, allowing communication between databases and features of the web application.
## Flow Diagram
![](https://github.com/AleksandarDzudzevic/CS_IA_Aleks/blob/main/FC_1_User%20list%20flow%20diagram%20-%20Flowchart.png)
Fig.6 shows a Flow diagram that visually represents the registration process for the Tutorflix web application, showcasing the required information from the users, which is gathered through the represented input boxes and is then queried and stored in the user database once the registration has been successful.
![](https://github.com/AleksandarDzudzevic/CS_IA_Aleks/blob/main/FC_2-fthe%20profile%20feature%20-%20Flowchart.png)
Fig.7 shows a Flow diagram that visually represents the feature of viewing a specific profile and showcases the process of presenting a specific profile with all its posts through queries that get such information from the Posts database allowing the representation of the desired profile only if the user has a valid and active token (if they are logged in). In case one is viewing their own profile they have the option to upload a new post of their own.
![](https://github.com/AleksandarDzudzevic/CS_IA_Aleks/blob/main/User%20list%20feature%20flow%20diagram%20-%20Flowchart%20(1).png)
Fig.8 shows a Flow diagram that visually represents the filtering feature for the tutor list of the Tutorflix web application, which allows users to efficiently use Tutorflix in order to find tutors that match their needs, either location-wise, financially, subject-wise or all of the mentioned by using iterations to checks all the registered users that fit such criterium.


## Test plan
|Test Number|Description|Test Type| Target|Procedure|Expected Outcome|
|-----------|-----------|--------|-----------|-----------------|----|
|1|Account registration system|Unit testing|Have a fully functional registration system that checks if the proper values are input in the email and password fields|(1) Run app.py (2) Click the register button on the login screen (3) Input a username: TesterSNS, email: testersns@gmail.com, password:abc123! following the password policy, account type: Student and Country: England that will be used for this tester account(4) After filling in all the fields create an account (5) Try to log in with the new account to see if it exists now| After following the procedure, a user should be able to login using the credentials of the newly created account|
|2|Tutor list inspecting from a student account type|Unit testing| Be able to access the tutor list and see all the available tutors and their tutoring posts for different subjects.|(1)Run Project_4.py(2)Login using adequate credentials for the tester account created in test no.1. (3)Choose the "see all tutors" option from the navigation bar.(4)Check if the redirected page shows a table containing the id, username, and country for each tutor| The student is able to access the tutor list from the main menu and will be able to see all the tutorflix tutors| 
|3|Accesing a specific user's profile from the user list|Integration testing| Access a specific user's profile  by choosing it from the user list|(1)Run Project_4.py(2)Login using adequate credentials for the tester account created in the test no.1. (3)Choose the "see all users" option from the navigation bar. (4) Choose a desired user and click on their nickname to get redirected to his profile. (5) Check if his profile and posts  (if there are any) are displayed successfully| A user can choose to view a specific creator profile that he is interested in.|
|4|Finding a specific user through filter options in the user table|Integration testing|Find a user through username search or by choosing a specific city of interest |(1)Run Project_4.py(2)Login using adequate credentials for the tester account created int test no.1. (3)Choose the "see all users" option from the navigation bar. (4) Choose a city and see if only users from that city appear in the user table. (5) Now type a certain username or a part of it and see if only adequate users appear | Both filter functions work and are properly integrated with the user table database and main menu|
|5|Code practices around HTML and Python, regarding usage of loops and their nesting  |Code Review| Replace repeating functions and features using better coding practices by using loops, and make the code more efficient by nesting loops.|(1) Review Project_4.py python code and HTML code to see any repetitive parts. (2) Create an algorithm that would replace the repetitive part using loops and nesting them if necessary. (3) Replace the old repetitive code and connect new algorithm and HTML code to the main SNS code | The code now uses loops for the profile accessing and for the learn about city feature.| 
|6| Commenting on complex code practices |Code Review| Adding comments that would explain the usage of more complex programming tools and algorithms to help future potential developers| (1) Review the python Project_4.py code and focus on the more complex algorithms and routes that have unique features (2) Add a comment explaining their usage and function in the code| The code is easier to understand and is more open for future co-development|


Fig.9 shows the test plan containing tests performed on the Tutorflix web application.

## Record of Tasks
| Task No | Planned Action                                              | Planned Outcome                                                                                                 | Time estimate | Target completion date | Criterion |
|---------|-------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------|---------------|------------------------|-----------|
|1|Write problem definition (Planning)|Have a clear problem that states the issue, its consequences, and a clear approach and solution that is being proposed| 20 min |8.7.2023 |A | 
|2|First client meeting: success criteria and required information (Planning)|Have a first client meeting and get the client to state the success criteria and basic information needed to establish a design statement and rationale for the solution that will be proposed to the client | 30 min|10.7.2023 |A |
|3|Write the first version of the rationale for the proposed solution and design statement (Planning)|Write down the rationale and design statement that will be presented to the client |35 min |10.7.2023 |A |
|4| Rewrite rationale for the proposed solution (Planning| Rewrite design statement so that it better explains methodology and tools that will be used for this web application development| 15 min | 11.7.2023| A|
|5| Design first version of the System diagram (Design)| Have the system diagram of the web application finsihed|20 min | 13.7.2023| B| 
|6| Add table of content (Planning)	 | Add table of content at the top of the file that will allow easier inspection of the project| 15 min|13.7.2023 | A|
|7| Construct the first version of database structures needed for the web application (Design)| Have the sketch of the databases for the initial idea of how the web application will be structured| 30 min| 14.7.2023|B|
|8|Design first version of the ER diagram (Design)| Design the first version of the diagram representing the Data structure of the web application| 25 min|20.7.2023 | B|
|9| Create databases and start with the program development (Development)|Start coding the web application and create databases  |45 min | 21.7.2023|C |
|10| Design the web applications logo and its color panel with the help of the client (see in [appendix](#appendix)) (Design)|Design the logo that would be used on the client's web application and the colors that will dictate the template|30 min|23.7.2023|B |
|11|Create the first version of the wireframe diagram of the web application (Design)| Have a clear visual representation of the web application's structure and interconnectivity between its features|23.7.2023||
|12| Create the first version of the login and registration system (Developing) |Create a functional login/registration system |1 h|30.7.2023 |C|
|13| Design second version of the System diagram (Design)| Have the system diagram showcase both client and server device|20 min | 15.8.2023| B| 
|14|Connect login/registration to the database (Developing)|Established connection now add/checks newly registered/ already existing accounts to/with the data database|20 min| 23.8.2023|C|
|15| Redo Login and Register UI to match the general template used for the web application (Developing)| Make the registration system UI fit better into the web app style. | 20 min| 1.9.2023 | C|
|16| Add password policy and create an interactive response to the user's input for the password. (Developing) |Make a password policy and add an emoji reaction showing if the user followed the policy. | 25 min|16.9.2023 | C|
|17| Add JWT token in order to improve web app security and only allow feature access to logged-in users (Developing)| Only registered users can access the application features| 30 min | 21.9.2023| C|
|18| Create the UML diagram for the web application (Design) |Create the UML diagram for the class used for manipulating databases for the web application | 20 min|26.9.2023 | B|
|19| Update the wireframe diagram so that it shows the new design of the web application (Design)|Have the wireframe diagram show an accurate version of the web application|20 min |28.9.2023 | B |
|20|  Perform 2 unit tests explained in the test plan section (Testing)  | Perform tests of the registration system and the tutor list feature  |  15 min | 6.10.2023  |  B   |
|21| Test accessing the tutors list from the main menu page (Testing) | Update the test plan with integration test relating to allowing registered students to access the table containing tutors of tutorflix| 15 min  |   6.10.2023 | B    |
|22| Test accessing a specific tutor from the user list feature. (Testing) | Update the test plan with an integration test relating to the feature that checks a specific tutor account from the tutor list  |  15 min |  8.10.2023  |  B   |
|23| Add the tutor list feature and the filtering options for it (Developing)|Have a tutor list feature that can be filtered by country or name of the tutor | 40 min|30.10.2023 | C|
|24| Add the view-specific tutor or student account option (Developing)| Be able to see a specific account by clicking a hyperlink attached to the account's name in the list of accounts|35 min |2.11.2023 | C|
|25| Create a flow diagram for the registration system (Design)| Have a visual presentation of the registration algorithm that was used for the web application|20 min |3.11.2023 |B |
|26| Create a flow diagram for the user account viewing feature (Design)| Have a visual presentation of the algorithm that was used for the account viewing feature of the web application|25 min |3.11.2023 |B |
|27| Create a flow diagram for the tutor list filtering feature (Design)| Have a visual presentation of the algorithm that was used for the tutor list filtering feature of the web application|30 min |3.11.2023 |B |
|28| Run code review for potential loops and loop nesting and see if any complex algorithms used need a comment to help future co-developers (Testing)| More efficient code of higher quality and better coding practices that would make co-development easier  | 25 min  |3.11.2023|B|
|29| Update descriptions of the diagrams and make the visual representation more understandable (Design)| Make the design of the diagrams easier to interpret| 20 min| 24.11.2023|B|

Fig.10 shows the record of tasks throughout the development of the Tutorflix web application.
# Criteria C: Development
## Tools and techniques used
1. Manipulating SQLite Database
2. Variables
3. For loops
4. If statements
5. Functions
6. Password Hashing
7. Nesting loops
8. HTML template usage
9. JWT session token usage
10. Cookie usage
11. CSS web design 
12. Using Flask library in Python
## Sources
1. “Beautiful CSS Buttons Examples - CSS Scan.” 92 Beautiful CSS Buttons Examples - CSS Scan, https://getcssscan.com/css-buttons-examples. 
2. “Flask HTTP Methods, Handle GET &amp; Post Requests.” GeeksforGeeks, GeeksforGeeks, 2 Feb. 2023, https://www.geeksforgeeks.org/flask-http-methods-handle-get-post-requests/. 
3. “Cirrus CSS.” Cirrus, https://www.cirrus-ui.com/buttons/basics. 
4. Auth0. “JSON Web Tokens.” Auth0 Docs, https://auth0.com/docs/secure/tokens/json-web-tokens. 
5. “How to - Search Bar.” How To Create a Search Bar, https://www.w3schools.com/howto/howto_css_searchbar.asp. 
## Development

## Success Criteria 1: The tutoring platform will have a secure register system, unique for student and tutor accounts with access to different features on the platform.
### Password encryption
```.py
from passlib.context import CryptContext

pwd_config = CryptContext(schemes = ["pbkdf2_sha256"],
                          default = "pbkdf2_sha256",
                          pbkdf2_sha256__default_rounds = 30000
                          )
```
Fig.11 Shows the encryption function used for securing users' data

Fig. 11 shows the process and encryption method used for password hashing for the Tutorflix website. To prevent any serious harm in the case of data leaking, if the same password is used in multiple places, an intruder can use that and the email for other web services, hurting the user in the process.
```.py
# This function receives an unsafe password and returns the hashed password
def encrypt_password(user_passowrd):
    return pwd_config.encrypt(user_passowrd)

```
Fig. 12 shows the method which calls the previously mentioned process of encryption.
In order to fulfill the client's request for the website, safe and secure data storing is necessary and it allows privacy of the user to stay at a desired level.

### Regsitration System
```.py
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        country = request.form['country']
        name = request.form['username']
        type = request.form['account-type']
        # Generate hashed password
        hashed_password = encrypt_password(password)
        # Insert user data into database
        conn = sqlite3.connect('tutorflix.db')
        c = conn.cursor()
        c.execute("INSERT INTO users (email, password, country, name, type) VALUES (?, ?, ?, ? , ?)", (email, hashed_password, country,name,type))
        conn.commit()
        conn.close()
        # Redirect user to login page
        return redirect(url_for("login"))
    return render_template('register.html')

```
Fig. 13 shows the registration function for the social network website Citio. 

in Fig.13 
When developing the registration system shown in Fig.13 using generalization I was able to recognize a way to solve one of the criteria requirements by including an option bar in the registration where a user would input the country and the account type (student/tutor) which would later be used in the filtering options. This helped with solving the problem of seeing irrelevant content creators who are not located in the same country. Then I implemented abstraction I used sqlite3.connect instead of the databse_wroker method I used in other cases in order to not have to modify that method jsut because of this specific case.

### Login System
```.py
@app.route('/login', methods = ['GET', 'POST'])
def login():
    msg = ''
    if request.method == 'POST':
        email = request.form['email']
        passwd = request.form['passwd']

        db = database_worker("tutorflix.db")
        user = db.search(f"SELECT id, email, password from users where email ='{email}'")
        if user:
            print("passed")
            user = user[0]  # cause search returns a list
            id, email_db, hashed = user
            if check_password(hashed_password = hashed, user_password = passwd):
                response = make_response(render_template('index.html'))
                response.set_cookie('user.id', f"{id}")
                token = jwt.encode({'user_id': id, 'exp': datetime.utcnow() + timedelta(minutes = 30)}, token_key,algorithm = 'HS256')
                session['token'] = token
                return response
        else:
            msg = "user does not exist"
    return render_template("login.html", message = msg)

```
Fig.14 shows the Login system feature of the website

Fig. 14 we see the login function of the Tutorflix web application. After getting the credentials that a user inputted I developed an algorithm that searches through the user database, looking for an account with a matching email address. The policy for the email address is to have the symbol "@" and characters before and after it. If there is such a user, the algorithm would then check if the encryption of the password they inputted matches the one in the database that was stored upon registration of the account. If it does, login is successful and a user is given a session token that lasts 30 minutes after which they would need to login again. 

```.py
def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        # Check if a token is present in the user's session
        if 'token' not in session:
            print("no token")
            # If no token is present, redirect the user to the login page
            return redirect(url_for('login'))
        try:
            # Attempt to decode the token using the secret key
            print("decoding the token")
            print(session['token'])
            data = jwt.decode(session['token'], token_key, algorithms = ['HS256'])
            print(data)

        except:
            print("wrong token")
            # If the token is invalid, redirect the user to the login page
            return redirect(url_for('login'))

        # If the token is valid, call the decorated function with the original arguments and keyword arguments
        return f(*args, **kwargs)

    # Return the decorated function
    return decorated
```
Fig.15 shows the JWT session token feature of the Tutorflix Web application.

Fig.15 shows the function used for the creation of the session tokens. This important implementation was inspired by using computational thinking and decomposing the problem of website safety. Even after implementing cookies, one could still redirect to a page without signing in beforehand. This is why I generalized the algorithm for creating JWT session tokens [^9] which in turn allowed me to set a requirement that a user is logged in before accessing any features of the website. This improved the security of the website and solved the previously decomposed problem of safety that the website had.

In order to successfully develop this I needed to have the following things in my algorithm: The wraps function from functools module is used to preserve the original function's metadata (data containing information about certain data, in this case about the function). After that the decorated function checks if a token is present in the user's session. If a token is present, the function attempts to decode it using the 'jwt.decode' function. If the token is invalid, the user is redirected to the login page. If the token is valid, the decorated function is called with the original arguments and keyword arguments using the 'f' function. For this, args is used to pass a variable number of non-keyword arguments to the decorated function and kwargs is used to pass a variable number of keyword arguments to the decorated function. 

## Success Criteria 2: The tutoring platform will contain useful filter options such as search by tutor name and country and for posts subject, word search, and price range.
```.py
country = request.args.get('country')# Gets the country chosen from the option bar (if any)
        search_query = request.args.get('search_query')
        # Filters the list of all_users to only include those that contain the search query (case insensitive)
        # if a search query is provided through the search bar filter
        if search_query:
            all_users = [user for user in all_users if search_query.lower() in user[1].lower()]
        return render_template("user.html", users = all_users, country = country)
```
Fig.16 shows the filter options for the tutors using country filtering and name search filtering.

```.py
    min_price = request.args.get('min_price')
        max_price = request.args.get('max_price')
        subject = request.args.get('subject')
        content_keywords = request.args.get('content_keywords')

        # Construct the SQL query based on the provided parameters
        query = "SELECT * FROM posts WHERE 1=1"  # Start with a true condition to append filters

        if min_price:
            query += f" AND price >= {min_price}"
        if max_price:
            query += f" AND price <= {max_price}"
        if subject:
            query += f" AND subject = '{subject}'"
        if content_keywords:
            query += f" AND content LIKE '%{content_keywords}%'"

        # Execute the query and fetch results as dictionaries
        all_posts = db.search(query)
        db.close()

        # Now all_posts will contain dictionaries, and you can access their elements using keys
        return render_template("posts.html", posts=all_posts, get_username=get_username)
```
Fig.17 shows the filter options for the posts using subject, price and key word filtering.

## Success Criteria 3: The tutoring platform will allow tutor accounts to upload/delete multiple tutoring posts for different subjects and topics that they offer to teach, all on one account.

```.py
   if request.method == 'POST':
            if request.method == 'POST':
                title = request.form['title']
                content = request.form['content']
                price = request.form['price']
                subject = request.form['subject']
                now = datetime.now()
                today = now.strftime("%d/%m/%Y")

                if len(title) > 0 and len(content) > 0 and len(price) > 0 and len(subject) > 0 and str(
                        user_id) == current_user_id:
                    new_post = f"INSERT INTO posts (title, content, price, subject, user_id, datetime) VALUES ('{title}', '{content}', '{price}', '{subject}', '{user_id}', '{today}')"
                    db.run_save(query = new_post)
                    return redirect(url_for('profile', user_id = user_id))
        users, posts = None, None
        user = db.search(f"SELECT * from users where id={user_id}")
        if user:
            posts = db.search(f"select * from posts where user_id={user_id}")
            user = user[0]  

        return render_template("profile.html", user = user, posts = posts, current_user_id=int(current_user_id))
```
Fig. 18 shows the code developed in order to allow posting tutoring advertisements on the Tutorflix website. The algorithm I developed uses if statements to gather the post's title,content, subject, price, time of posting, and checks if the information is being provided by the user currently signed in. If that is the case a new post will be inserted and the page will be refreshed, now showing the newly posted article. I developed this algorithm using patern recognition from the login page where a similar type was used where after a certain validation a query was used which inserted data input into the database.



# Criteria D: Functionality
## Video showcase

# Criteria E: Evaluation
## Evaluation table
|Criteria number| Criteria| Final product| Criteria success|
|---------------|----------|-------------------------------|--------------|

## Client interview

## Recommendation


# Appendix
![](https://github.com/AleksandarDzudzevic/CS_IA_Aleks/blob/main/client_interview_1st.png)

### The first client consultation was done remotely on July 10th, 2023 13:15 pm, during which success criteria were established.

[^1]: Dream AI prompt: "Art representing Tutoring services, presenting a tutor and a student". 6 July 2023 https://dream.ai/create
[^2]: Sengar, Ritesh. “Python vs PHP: Which Is Better for Web Development?” Hackernoon, 7 Jan. 2021, hackernoon.com/python-vs-php-which-is-better-for-web-development-cj1236mj. 
[^3]: "Welcome to Flask." Flask Documentation, 15 Jan. 2023, flask.palletsprojects.com/en/2.1.x/. 
[^4]: Grinberg, Miguel. Flask Web Development: Developing Web Applications with Python. 2nd ed., O'Reilly Media, Inc., 2018. 
[^5]: “What Is a Database?” Oracle, https://www.oracle.com/database/what-is-database/. 
[^6]: "What is SQL?" W3Schools, W3Schools, https://www.w3schools.com/sql/
[^7]: https://www.smashingmagazine.com/2010/01/color-theory-for-designers-part-1-the-meaning-of-color/
[^8]: 4. Auth0. “JSON Web Tokens.” Auth0 Docs, https://auth0.com/docs/secure/tokens/json-web-tokens. 
[^9]: 4. Auth0. “JSON Web Tokens.” Auth0 Docs, https://auth0.com/docs/secure/tokens/json-web-tokens. 

