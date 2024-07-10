import os
import sqlite3
from datetime import datetime, timedelta
from functools import wraps
import dotenv
import jwt
from flask import Flask, render_template, request, redirect, url_for, make_response, session
from mylib import database_worker, encrypt_password, check_password
from flask import flash
from flask_mail import Mail, Message

app = Flask(__name__)

app.secret_key = 'ejhvvfwfbjwnwsqwpqqrhphwqnqwdwefhw45678uh23r23313fg2u181gf211dd'
dotenv.load_dotenv()
token_key = os.getenv('TOKEN_ENCRYPTION_KEY')

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = 'tutorflix.webapp@gmail.com'
app.config['MAIL_PASSWORD'] = 'Octob@r27'
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
mail = Mail(app)


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


def create_database():
    db = database_worker("tutorflix.db")

    query_user = """Create table if not exists users(
    id INTEGER PRIMARY KEY,
    name TEXT,
    email TEXT,
    password TEXT,
    country TEXT,
    acc_type TEXT
    )
    """
    query_post = """ CREATE table if not exists posts(
      id INTEGER PRIMARY KEY,
      title VARCHAR(100),
      content TEXT,
      datetime TEXT,
      price flaot,
      grade TEXT,
      subject TEXT,
      user_id INTEGER,
     FOREIGN KEY (user_id) REFERENCES users(id) on delete cascade

      )"""
    query_reviews = """ CREATE table if not exists reviews(
          id INTEGER PRIMARY KEY,
          title VARCHAR(100),
          content TEXT,
          datetime TEXT,
          user_id INTEGER,
          post_id INTEGER,
          FOREIGN KEY (user_id) REFERENCES users(id) on delete cascade
          FOREIGN KEY (post_id) REFERENCES posts(id) on delete cascade

          )"""
    db.run_save(query_user)
    db.run_save(query_post)
    db.run_save(query_reviews)
    db.close()


def get_username(user_id):
    db = database_worker("tutorflix.db")
    user = db.search(f"SELECT name FROM users WHERE id={user_id}")
    db.close()
    if user:
        return user[0][0]  # Assuming username is the first column in the query result
    return "Unknown User"  # Default value if user is not found


def populate_db():  # add regsitration option
    users = []
    db = database_worker("tutorflix.db")
    for u in users:
        email, pwd = u
        query = f"""INSERT into users(email,password)values 
        ('{email}','{encrypt_password(pwd)}')
        """
        db.run_save(query)
    db.close()


@app.route('/', methods = ['GET', 'POST'])
@app.route('/index', methods = ['GET', 'POST'])
@token_required
def index():
    return render_template('index.html')


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
                token = jwt.encode({'user_id': id, 'exp': datetime.utcnow() + timedelta(minutes = 30)}, token_key,
                                   algorithm = 'HS256')
                session['token'] = token
                return response
        else:
            msg = "user does not exist"
    return render_template("login.html", message = msg)


@app.route('/register', methods = ['GET', 'POST'])
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
        c.execute("INSERT INTO users (email, password, country, name, type) VALUES (?, ?, ?, ? , ?)",
                  (email, hashed_password, country, name, type))
        conn.commit()
        conn.close()
        # Redirect user to login page
        return redirect(url_for("login"))
    return render_template('register.html')


@app.route('/my_profile')
def my_profile():
    user_id = session.get('user_id') or request.cookies.get('user.id')
    if not user_id:
        return redirect(url_for('login'))

    return redirect(url_for('profile', user_id = user_id))


@app.route('/users')
@token_required
def users():
    # Checks if the user is authenticated by checking if the user.id cookie exists
    if request.cookies.get('user.id'):
        db = database_worker(
            "tutorflix.db")  # Creates a database worker object to perform SQL queries on the "social_net.db" database
        all_users = db.search("SELECT * FROM users where type='teacher'")  # Selects all users from the "users" table
        db.close()  # Closes the database connection
        country_full_names = {
            'AF': 'Afghanistan',
            'AX': 'Aland Islands',
            'AL': 'Albania',
            'DZ': 'Algeria',
            'AS': 'American Samoa',
            'AD': 'Andorra',
            'AO': 'Angola',
            'AI': 'Anguilla',
            'AQ': 'Antarctica',
            'AG': 'Antigua and Barbuda',
            'AR': 'Argentina',
            'AM': 'Armenia',
            'AW': 'Aruba',
            'AU': 'Australia',
            'AT': 'Austria',
            'AZ': 'Azerbaijan',
            'BS': 'Bahamas',
            'BH': 'Bahrain',
            'BD': 'Bangladesh',
            'BB': 'Barbados',
            'BY': 'Belarus',
            'BE': 'Belgium',
            'BZ': 'Belize',
            'BJ': 'Benin',
            'BM': 'Bermuda',
            'BT': 'Bhutan',
            'BO': 'Bolivia',
            'BQ': 'Bonaire, Sint Eustatius and Saba',
            'BA': 'Bosnia and Herzegovina',
            'BW': 'Botswana',
            'BV': 'Bouvet Island',
            'BR': 'Brazil',
            'IO': 'British Indian Ocean Territory',
            'BN': 'Brunei Darussalam',
            'BG': 'Bulgaria',
            'BF': 'Burkina Faso',
            'BI': 'Burundi',
            'KH': 'Cambodia',
            'CM': 'Cameroon',
            'CA': 'Canada',
            'CV': 'Cape Verde',
            'KY': 'Cayman Islands',
            'CF': 'Central African Republic',
            'TD': 'Chad',
            'CL': 'Chile',
            'CN': 'China',
            'CX': 'Christmas Island',
            'CC': 'Cocos (Keeling) Islands',
            'CO': 'Colombia',
            'KM': 'Comoros',
            'CG': 'Congo',
            'CD': 'Congo, Democratic Republic of the Congo',
            'CK': 'Cook Islands',
            'CR': 'Costa Rica',
            'CI': 'Cote D\'Ivoire',
            'HR': 'Croatia',
            'CU': 'Cuba',
            'CW': 'Curacao',
            'CY': 'Cyprus',
            'CZ': 'Czech Republic',
            'DK': 'Denmark',
            'DJ': 'Djibouti',
            'DM': 'Dominica',
            'DO': 'Dominican Republic',
            'EC': 'Ecuador',
            'EG': 'Egypt',
            'SV': 'El Salvador',
            'GQ': 'Equatorial Guinea',
            'ER': 'Eritrea',
            'EE': 'Estonia',
            'ET': 'Ethiopia',
            'FK': 'Falkland Islands (Malvinas)',
            'FO': 'Faroe Islands',
            'FJ': 'Fiji',
            'FI': 'Finland',
            'FR': 'France',
            'GF': 'French Guiana',
            'PF': 'French Polynesia',
            'TF': 'French Southern Territories',
            'GA': 'Gabon',
            'GM': 'Gambia',
            'GE': 'Georgia',
            'DE': 'Germany',
            'GH': 'Ghana',
            'GI': 'Gibraltar',
            'GR': 'Greece',
            'GL': 'Greenland',
            'GD': 'Grenada',
            'GP': 'Guadeloupe',
            'GU': 'Guam',
            'GT': 'Guatemala',
            'GG': 'Guernsey',
            'GN': 'Guinea',
            'GW': 'Guinea-Bissau',
            'GY': 'Guyana',
            'HT': 'Haiti',
            'HM': 'Heard Island and Mcdonald Islands',
            'VA': 'Holy See (Vatican City State)',
            'HN': 'Honduras',
            'HK': 'Hong Kong',
            'HU': 'Hungary',
            'IS': 'Iceland',
            'IN': 'India',
            'ID': 'Indonesia',
            'IR': 'Iran, Islamic Republic of',
            'IQ': 'Iraq',
            'IE': 'Ireland',
            'IM': 'Isle of Man',
            'IL': 'Israel',
            'IT': 'Italy',
            'JM': 'Jamaica',
            'JP': 'Japan',
            'JE': 'Jersey',
            'JO': 'Jordan',
            'KZ': 'Kazakhstan',
            'KE': 'Kenya',
            'KI': 'Kiribati',
            'KP': 'Korea, Democratic People\'s Republic of',
            'KR': 'Korea, Republic of',
            'XK': 'Kosovo',
            'KW': 'Kuwait',
            'KG': 'Kyrgyzstan',
            'LA': 'Lao People\'s Democratic Republic',
            'LV': 'Latvia',
            'LB': 'Lebanon',
            'LS': 'Lesotho',
            'LR': 'Liberia',
            'LY': 'Libyan Arab Jamahiriya',
            'LI': 'Liechtenstein',
            'LT': 'Lithuania',
            'LU': 'Luxembourg',
            'MO': 'Macao',
            'MK': 'Macedonia, the Former Yugoslav Republic of',
            'MG': 'Madagascar',
            'MW': 'Malawi',
            'MY': 'Malaysia',
            'MV': 'Maldives',
            'ML': 'Mali',
            'MT': 'Malta',
            'MH': 'Marshall Islands',
            'MQ': 'Martinique',
            'MR': 'Mauritania',
            'MU': 'Mauritius',
            'YT': 'Mayotte',
            'MX': 'Mexico',
            'FM': 'Micronesia, Federated States of',
            'MD': 'Moldova, Republic of',
            'MC': 'Monaco',
            'MN': 'Mongolia',
            'ME': 'Montenegro',
            'MS': 'Montserrat',
            'MA': 'Morocco',
            'MZ': 'Mozambique',
            'MM': 'Myanmar',
            'NA': 'Namibia',
            'NR': 'Nauru',
            'NP': 'Nepal',
            'NL': 'Netherlands',
            'AN': 'Netherlands Antilles',
            'NC': 'New Caledonia',
            'NZ': 'New Zealand',
            'NI': 'Nicaragua',
            'NE': 'Niger',
            'NG': 'Nigeria',
            'NU': 'Niue',
            'NF': 'Norfolk Island',
            'MP': 'Northern Mariana Islands',
            'NO': 'Norway',
            'OM': 'Oman',
            'PK': 'Pakistan',
            'PW': 'Palau',
            'PS': 'Palestinian Territory, Occupied',
            'PA': 'Panama',
            'PG': 'Papua New Guinea',
            'PY': 'Paraguay',
            'PE': 'Peru',
            'PH': 'Philippines',
            'PN': 'Pitcairn',
            'PL': 'Poland',
            'PT': 'Portugal',
            'PR': 'Puerto Rico',
            'QA': 'Qatar',
            'RE': 'Reunion',
            'RO': 'Romania',
            'RU': 'Russian Federation',
            'RW': 'Rwanda',
            'BL': 'Saint Barthelemy',
            'SH': 'Saint Helena',
            'KN': 'Saint Kitts and Nevis',
            'LC': 'Saint Lucia',
            'MF': 'Saint Martin',
            'PM': 'Saint Pierre and Miquelon',
            'VC': 'Saint Vincent and the Grenadines',
            'WS': 'Samoa',
            'SM': 'San Marino',
            'ST': 'Sao Tome and Principe',
            'SA': 'Saudi Arabia',
            'SN': 'Senegal',
            'RS': 'Serbia',
            'CS': 'Serbia and Montenegro',
            'SC': 'Seychelles',
            'SL': 'Sierra Leone',
            'SG': 'Singapore',
            'SX': 'Sint Maarten',
            'SK': 'Slovakia',
            'SI': 'Slovenia',
            'SB': 'Solomon Islands',
            'SO': 'Somalia',
            'ZA': 'South Africa',
            'GS': 'South Georgia and the South Sandwich Islands',
            'SS': 'South Sudan',
            'ES': 'Spain',
            'LK': 'Sri Lanka',
            'SD': 'Sudan',
            'SR': 'Suriname',
            'SJ': 'Svalbard and Jan Mayen',
            'SZ': 'Swaziland',
            'SE': 'Sweden',
            'CH': 'Switzerland',
            'SY': 'Syrian Arab Republic',
            'TW': 'Taiwan, Province of China',
            'TJ': 'Tajikistan',
            'TZ': 'Tanzania, United Republic of',
            'TH': 'Thailand',
            'TL': 'Timor-Leste',
            'TG': 'Togo',
            'TK': 'Tokelau',
            'TO': 'Tonga',
            'TT': 'Trinidad and Tobago',
            'TN': 'Tunisia',
            'TR': 'Turkey',
            'TM': 'Turkmenistan',
            'TC': 'Turks and Caicos Islands',
            'TV': 'Tuvalu',
            'UG': 'Uganda',
            'UA': 'Ukraine',
            'AE': 'United Arab Emirates',
            'GB': 'United Kingdom',
            'US': 'United States',
            'UM': 'United States Minor Outlying Islands',
            'UY': 'Uruguay',
            'UZ': 'Uzbekistan',
            'VU': 'Vanuatu',
            'VE': 'Venezuela',
            'VN': 'Viet Nam',
            'VG': 'Virgin Islands, British',
            'VI': 'Virgin Islands, U.s.',
            'WF': 'Wallis and Futuna',
            'EH': 'Western Sahara',
            'YE': 'Yemen',
            'ZM': 'Zambia',
            'ZW': 'Zimbabwe'
        }

        country = request.args.get('country')  # Gets the country chosen from the option bar (if any)
        search_query = request.args.get('search_query')
        # Filters the list of all_users to only include those that contain the search query (case insensitive)
        # if a search query is provided through the search bar filter
        if search_query:
            all_users = [user for user in all_users if search_query.lower() in user[1].lower()]
        return render_template("user.html", users = all_users, country = country,
                               country_full_names = country_full_names)
    else:
        return redirect("login")


@app.route('/user/<user_id>', methods = ['GET', 'POST'])
@token_required
def profile(user_id: int):
    if not request.cookies.get('user.id'):
        return redirect(url_for('login'))
    else:
        db = database_worker("tutorflix.db")
        current_user_id = request.cookies.get('user.id')  # get the ID of the currently logged in user
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
            user = user[0]  # remember search returns a list (should be one user so...

        return render_template("profile.html", user = user, posts = posts, current_user_id = int(current_user_id))


def has_graded(post_id, user_id):
    db = database_worker("tutorflix.db")
    result = db.search(f"SELECT id FROM reviews WHERE post_id={post_id} AND user_id={user_id}")
    db.close()
    return bool(result)


@app.route('/rate_post/<int:post_id>', methods = ['POST'])
@token_required
def rate_post(post_id):
    current_user_id = int(request.cookies.get('user.id'))
    given_grade = int(request.form['rating'])

    # Ensure the user has not graded the post before
    if not has_graded(post_id, current_user_id):
        # Insert the rating into the reviews table
        db = database_worker("tutorflix.db")
        query = f"INSERT INTO reviews (given_grade, user_id, post_id) VALUES ({given_grade}, {current_user_id}, {post_id})"
        db.run_save(query)
        db.close()
        flash('Post rated successfully!', 'success')
    else:
        flash('You have already rated this post or you cannot rate your own post.', 'error')

    # Redirect to the same page with the same filters
    return redirect(url_for('posts', min_price = request.args.get('min_price'),
                            max_price = request.args.get('max_price'),
                            subject = request.args.get('subject'),
                            content_keywords = request.args.get('content_keywords')))


@app.route('/posts')
@token_required
def posts():
    # Checks if the user is authenticated by checking if the user.id cookie exists
    if request.cookies.get('user.id'):
        db = database_worker("tutorflix.db")
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
        return render_template("posts.html", posts = all_posts, get_username = get_username)
    else:
        return redirect("login")


@app.route('/delete_post/<int:post_id>', methods = ['POST'])
@token_required
def delete_post(post_id):
    current_user_id = int(request.cookies.get('user.id'))

    # Check if the user owns the post before deleting
    db = database_worker("tutorflix.db")
    post_owner_id = db.search(f"SELECT user_id FROM posts WHERE id={post_id}")
    db.close()

    if post_owner_id and post_owner_id[0][0] == current_user_id:
        # User owns the post, proceed with deletion
        db = database_worker("tutorflix.db")
        query = f"DELETE FROM posts WHERE id={post_id}"
        db.run_save(query)
        db.close()
        flash('Post deleted successfully!', 'success')
    else:
        flash('You do not have permission to delete this post.', 'error')

    # Redirect to the user's profile page
    return redirect(url_for('profile', user_id = current_user_id))


@app.route('/leaderboard')
@token_required
def leaderboard():
    # Fetch the average grades for all tutors from the reviews table
    db = database_worker("tutorflix.db")
    query = """
        SELECT p.user_id, AVG(r.given_grade) as avg_grade
        FROM reviews r
        JOIN posts p ON r.post_id = p.id
        GROUP BY p.user_id
        ORDER BY avg_grade DESC
        LIMIT 3
    """
    top_tutors = db.search(query)
    db.close()

    # Define medal emojis
    medals = ['🥇', '🥈', '🥉']
    # Render the leaderboard template with the top tutors and medals
    return render_template("leaderboard.html", top_tutors = top_tutors, medals = medals, get_username = get_username)


def get_professor_email(user_id, professor_id):
    db = database_worker("tutorflix.db")
    user, professor = db.search(f"SELECT email FROM users WHERE id = {user_id}"), db.search(
        f"SELECT email FROM users WHERE id = {professor_id}")
    db.close()

    if (user and professor):
        return (user[0][0], professor[0][0])  # Assuming email is the first (and only) column in the query result
    else:
        return None  # Return None if the user with the specified ID is not found


@app.route('/email_professor/<int:user_id>/<int:professor_id>', methods = ['GET', 'POST'])
@token_required
def email_professor(user_id, professor_id):
    if request.method == 'POST' and 'email_professor' in request.form:
        print("Received email_professor POST request")
        user_email, professor_email = get_professor_email(user_id, professor_id)
        if professor_email and user_email:
            msg = Message(f"Hey you have a new request for a class from :{user_email}",
                          sender = "tutorflix.webapp@gmail.com", recipients = [f'{professor_email}'])
            msg.body = "Hello, this is a test"
            try:
                print(msg)
                mail.send(msg)
                print("Email sent successfully")
                return 'Sent email'
            except Exception as e:
                print(f"Error sending email: {str(e)}")
                return redirect('index.html')
        else:
            print("Professor email not found")
            return 'Professor email not found'
    else:
        print("Invalid request")
        return 'Invalid request'


@app.route('/logout')
def logout():
    response = make_response(redirect('login'))
    response.set_cookie("user_id", "", expires = 0)

    return response


@app.route('/delete_profile')
@token_required
def delete_profile():
    if not request.cookies.get('user.id'):
        return redirect(url_for('login'))
    else:
        db = database_worker("tutorflix.db")
        current_user_id = request.cookies.get('user.id')  # get the ID of the currently logged in user
        query = f"Delete from users where id={current_user_id}"
        db.run_save(query = query)
        return redirect('login')


# print("creating database")
# create_database()
# print("populating the users table")
# populate_db()
if __name__ == '__main__':
    app.run(debug = True)
