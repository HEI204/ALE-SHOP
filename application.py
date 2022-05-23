import os
from cs50 import SQL
from flask import Flask, redirect, render_template, request, session, flash
from flask_session import Session
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash

from helper import login_required, hk_time_now, order_id_generator


# Configure web application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem" # set the location for session storage
Session(app)

# Configure the app to support file upload
app.config["UPLOAD_FOLDER"] = "static/images/"
app.config["MAX_CONTENT_LENGTH"] = 16*1024*1024

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///market.db")

@app.route("/")
def index():
    ''' Homepage for showing all product  '''

    # Query all product info
    market_info = db.execute("SELECT * FROM products WHERE stock > 0")
    # Query user cash for the current login user
    try:
        user_cash = db.execute("SELECT cash FROM users WHERE username = ?", session["username"])[0]["cash"]
    except:
        user_cash = 0

    return render_template("index.html", market_info=market_info, user_cash=user_cash)


@app.route("/add_to_cart")
@login_required
def add_to_cart():
    ''' Add product to the cart '''

    # If user click the 'add to cart' button
    if request.args.get("product"):

        product_name = request.args.get("product")

        # Query specific product info and user info when user clicked the button
        product_info = db.execute("SELECT * FROM products WHERE name = ?", product_name)[0]
        user_id = db.execute("SELECT * FROM users WHERE username = ?", session["username"])[0]["id"]

        # Add to the cart and pop the message for add sucessfully
        flash("You have added to your cart!", category='success')
        db.execute("INSERT INTO cart(user_id, product_id, price) VALUES(?, ?, ?)",
                   user_id, product_info["id"], product_info["price"])

        return redirect("/")


@app.route("/cart")
@login_required
def cart():
    ''' Cart infomation  '''

    # If user click the 'remove' button for specific item in the cart
    if request.args.get("remove_product_id"):
        # Remove the specific item in the cart
        db.execute("DELETE FROM cart WHERE id = ?", request.args.get("remove_product_id"))

    # Query the user information
    user_info = db.execute("SELECT * FROM users WHERE username = ?", session["username"])[0]
    user_cash = user_info["cash"]

    # Query all the items currently inside the cart
    cart_items = db.execute("SELECT cart.id, name, products.price FROM products JOIN cart ON cart.product_id = products.id WHERE cart.user_id = ?",
                 user_info["id"])

    # Sum up the total price for all items in the cart
    cart_total_price = 0
    for item in cart_items:
        cart_total_price += item["price"]

    return render_template("cart.html", user_cash=user_cash, cart_items=cart_items, cart_total_price=cart_total_price)

@app.route("/buy")
@login_required
def buy():
    ''' Purchase cart items '''

    # Query the user information
    user_info = db.execute("SELECT * FROM users WHERE username = ?", session["username"])[0]
    user_cash = user_info["cash"]

    # Query all the items currently inside the cart
    cart_items = db.execute("SELECT products.id, name, products.price, discount FROM products JOIN cart ON cart.product_id = products.id WHERE cart.user_id = ?",
                 user_info["id"])

    cart_total_price = 0
    for item in cart_items:
        cart_total_price += item["price"]
    new_user_cash = user_cash - cart_total_price
    if new_user_cash < 0:
        flash("You do not have enough cash to buy all product inside the cart", category='danger')
        return redirect("/cart")
    else:
        order_id = order_id_generator()
        db.execute("UPDATE users SET cash = ? WHERE username = ?", new_user_cash, session["username"])
        for item in cart_items:
            item_stock = db.execute("SELECT * FROM products WHERE id = ?", item["id"])[0]["stock"]
            db.execute("INSERT INTO transactions(order_id, product_id, user_id, price, timestamp) VALUES(?, ?, ?, ?, ?)",
                       order_id, item["id"], user_info["id"], item["price"], hk_time_now())
            db.execute("UPDATE products SET stock = ? WHERE id = ?", (item_stock-1), item["id"])


        db.execute("DELETE FROM cart WHERE user_id = ?", user_info["id"])
        flash("You have bought sucessfully!", category='success')

    return redirect("/")

@app.route("/single_product", methods=["GET", "POST"])
def single_product():
    ''' Single product information on seperate page'''

    # If user click 'more info' for specific product
    if request.method == "GET":
        temp = request.args.get("product")

        if not temp:
            product_name = ""
        else:
            product_name = temp;

        # Query the information for that product
        product_info = db.execute("SELECT * FROM products WHERE name = ?", product_name)[0]

        # Show the information for that product in new page
        return render_template("single_product.html", product_name=product_name, product_info=product_info)


@app.route("/admin", methods=["GET", "POST"])
@login_required
def admin():
    ''' Admin dashboard for all product information in out market '''

    # User reached route via GET (as by clicking a link or via redirect)
    if request.method == "GET":
        # Only admin able to add new product
        if session["username"] != 'admin':
            flash("Sorry, you do not have permission to access admin page", category='danger')
            return redirect("/")

        # Show the market info for our shop to the admin
        market_info = db.execute("SELECT * FROM products")
        return render_template("admin.html", market_info=market_info)


@app.route("/add_cash", methods=["GET", "POST"])
@login_required
def add_cash():
    """ Add cash """

    user_cash = db.execute("SELECT * FROM users WHERE username = ?", session["username"])[0]["cash"]

    # User reached route via GET (as by clicking a link or via redirect)
    if request.method == "GET":
        return render_template("add_cash.html", user_cash=user_cash)

    # User reached route via POST (as by submitting a form via POST)
    # Validation for the amount of cash
    try:
        added_cash = float(request.form.get("added_cash"))
    except:
        flash("You should input a number for add cash", category='danger')
        return render_template("add_cash.html", user_cash=user_cash)

    if added_cash < 0:
        flash("You should input a positive number for add cash", category='danger')
        return render_template("add_cash.html", user_cash=user_cash)

    total_cash = float(user_cash) + float(added_cash)
    db.execute("UPDATE users SET cash = ? WHERE username = ?", total_cash, session["username"])

    return render_template("add_cash.html", user_cash=total_cash)


@app.route("/history", methods=["GET", "POST"])
@login_required
def history():
    """ User transaction record """
    user_info = db.execute("SELECT * FROM users WHERE username = ?", session["username"])[0]
    transaction_info = db.execute("SELECT SUM(products.price) as total_price, transactions.order_id, timestamp FROM transactions JOIN products ON transactions.product_id = products.id WHERE transactions.user_id = ? GROUP BY order_id ORDER BY timestamp DESC", user_info["id"])
    return render_template("history.html", transaction_info=transaction_info, user_cash=user_info["cash"])


@app.route("/order_info")
@login_required
def order_info():
    """ Show the product for the order"""

    user_cash = db.execute("SELECT * FROM users WHERE username = ?", session["username"])[0]["cash"]
    order_id = request.args.get("order_id")
    order_info = db.execute("SELECT products.name, products.price FROM products JOIN transactions ON products.id = transactions.product_id WHERE order_id = ?", order_id)
    return render_template("order_info.html", order_info=order_info, user_cash=user_cash, order_id=order_id)


@app.route("/add_product", methods=["GET", "POST"])
@login_required
def add_product():
    ''' Add product to the market '''

    # User reached route via GET (as by clicking a link or via redirect)
    if request.method == "GET":
        # Only admin able to add new product
        if session["username"] != 'admin':
            flash("Sorry, you do not have permission to access this page", category='danger')
            return redirect("/")

        return render_template("add_product.html")

    # User reached route via POST (as by submitting a form via POST)
    product_name =  request.form.get("product_name")
    product_description = request.form.get("description")

    # Validation for product information to add into the database
    try:
        product_price = float(request.form.get("product_price"))
    except ValueError:
        return flash("You should input the product price", category='danger')

    try:
        product_stocks = int(request.form.get("product_stocks"))
    except ValueError:
        flash("You should input the product stocks", category='danger')

    if not product_name:
        flash("You should input the product name", category='danger')
    elif product_price <= 0:
        flash("Product price should be a positive number", category='danger')
    elif not (product_discount >= 0 and product_discount <= 1):
        flash("Product discount should be between 0 and 1", category='danger')
    elif not product_description:
        flash("You should input the product description", category='danger')
    else:
        # Add the product info into the datbase
        exist = db.execute("SELECT name FROM products WHERE name = ? COLLATE NOCASE", product_name)

        # If the product already added in the database (Handle case insensitive case)
        if exist:
            flash("This product already added into the database", category='danger')
            return render_template("add_product.html")

        try:
            db.execute("INSERT INTO products(name, price, discount, stock, description) VALUES(?, ?, ?, ?, ?)",
                       product_name, product_price, product_discount, product_stocks, product_description)

        # If the product already added in the database
        except:
            flash("This product already added into the database", category='danger')
    return render_template("add_product.html")


@app.route("/update_product_info", methods=["GET", "POST"])
@login_required
def update_product_info():
    ''' Update product information for the product in the market currently '''

    # User reached route via GET (as by clicking a link or via redirect)
    if request.method == "GET":
        # Only admin able to update product info
        if session["username"] != 'admin':
            flash("Sorry, you do not have permission to access this page", category='danger')
            return redirect("/")

        current_product = db.execute("SELECT * FROM products")

        temp = request.args.get("selected_product_name")
        if not temp:
            update_product_name = ""
        else:
            update_product_name = temp

        return render_template("update_product_info.html",current_product=current_product, update_product_name=update_product_name)

    # User reached route via POST (as by submitting a form via POST)
    selected_product_name = request.form.get("product")
    new_product_description = request.form.get("new_description")

    # Validation for update product info
    try:
        new_product_price = float(request.form.get("new_product_price"))
    except ValueError:
        return flash("You should input the product price", category='danger')

    try:
        new_product_stocks = int(request.form.get("new_product_stocks"))
    except ValueError:
        return flash("You should input the product stocks", category='danger')

    if not selected_product_name:
        flash("Please select the product name that you would like to update", category='danger')
    elif new_product_price <= 0:
        flash("Product price should be a positive number", category='danger')
    elif not (new_product_discount >= 0 and new_product_discount <= 1):
        flash("Product discount should be between 0 and 1", category='danger')
    elif not new_product_description:
        flash("You should input the product description", category='danger')
    else:
        # Update the product info
        db.execute("UPDATE products SET price = ?, discount = ?, stock = ?, description = ? WHERE name = ?",
                   new_product_price, new_product_discount, new_product_stocks, new_product_description, selected_product_name)

    return redirect("/admin")


@app.route("/register", methods=["GET", "POST"])
def register():
    ''' User register page '''

    # User reached route via GET (as by clicking a link or via redirect)
    if request.method == "GET":
        return render_template("register.html")

    # User reached route via POST (as by submitting a form via POST)
    username = request.form.get("username")
    password = request.form.get("password")
    confirm_password = request.form.get("confirmation")
    email = request.form.get("email_address")

    # Hash the password
    hashed_password = generate_password_hash(password)

    # Username and Password Validation
    if not username:
        flash("You should input your username for create account", category='danger')
    elif not password:
        flash("You should input your password for create account", category='danger')
    elif not confirm_password:
        flash("You should input your password again for confirmation", category='danger')
    elif len(password) < 6:
        flash("Your password should be at least 6 character long", category='danger')
    elif not email:
        flash("You should input your email address for create account", category='danger')
    elif password != confirm_password:
        flash("Your password does not match")
    else:
        # Insert username and hashed password into the database
        try:
            db.execute("INSERT INTO users(username, hash, email_address) VALUES(?, ?, ?)",
                       username, hashed_password, email)
            flash("You have registerd your account sucessfully", category='success')
            return render_template("login.html")

        # If the username already exist in the database
        except:
            flash("This username has been registered by other", category='danger')
    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    ''' Login '''

    # Forget any user_id
    session.clear()

    # User reached route via GET (as by clicking a link or via redirect)
    if request.method == "GET":
        return render_template("login.html")

    # User reached route via POST (as by submitting a form via POST)
    username = request.form.get("username")
    password = request.form.get("password")

    # Ensure username and password was entered
    if not username:
        flash("You should input your username for login", category='danger')
        return render_template("login.html")
    elif not password:
        flash("You should input your password for login", category='danger')
        return render_template("login.html")

    # Query the username in the database
    rows = db.execute("SELECT * FROM users WHERE username = ?", username)

    if len(rows) != 1 or not check_password_hash(rows[0]["hash"], password):
        flash("Invalid username and/or password", category='danger')
        return render_template("login.html")

    # Remember which user has logged in
    session["username"] = rows[0]["username"]

    if username == "admin":
        return redirect("/admin")
    # Redirect user to home page
    return redirect("/")


@app.route("/logout")
def logout():
    ''' Logout '''

    # Forget any user_id
    session.clear()

    # Redirect user to home page
    return redirect("/")
