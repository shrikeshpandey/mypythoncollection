from flask import Flask, render_template, request, flash, redirect, url_for, session, escape
from controller.user_controller import user_controller
from controller.book_controller import book_controller
from controller.rented_books_controller import rented_books_controller
import platform, sys

app = Flask(__name__)
app.secret_key = 'examplekey'
app.config['HOST'] = 'localhost'
app.config['USER'] = 'invated'
app.config['PASSWORD'] = 'invated'

# Index Route
@app.route('/')
def home():
    return render_template("home.html")

# Creating a session
@app.route('/start_sesion',methods=['POST'])
def start_sesion():
        if request.method == 'POST':
                name=request.form['txtName']
                password=request.form['txtPass']
                resultado = user_controller.start_session(name, password)
                if resultado != None:
                        
                        session['usuario']=resultado['usuario']
                        session['clave']=resultado['clave']
                        session['fecha']=resultado['fecha']
                        flash("User "+ resultado['usuario'] +" Correct, we'll start session just now")
                        return redirect(url_for('.user'))
                        
                else:
                        flash("User or Password Incorrect")
                        return redirect(url_for('signin'))
# Delete Session
@app.route('/logout')
def logout():
        session.pop('usuario')
        session.pop('clave')
        session.pop('fecha')
        return redirect(url_for('home'))

# Create User
@app.route('/', methods=['POST'])
def add_user():

        if request.method == 'POST':
                name=request.form['txtName']
                password=request.form['txtPass']
                repeatPassword=request.form['txtRepeatPass']
                if password == repeatPassword:
                        flash(user_controller.create_user(name,password))
                        return render_template('signin.html')
                else:
                        flash("Passwords are not equal")
                        return render_template('home.html')

        #user_controller=user_controller()
        
        
# User Page        
@app.route("/user")
def user():
        if "usuario" in session:
                books=book_controller.return_books()
                print("--------------------Books: ",books[0].getnombre())
                flash('Welcome Mr. '+session["usuario"])
                return render_template("user.html",allBooks=books)
        else:
                flash('You have not logged in')
                return redirect(url_for('signin'))

        
# Sign in Route
@app.route('/signin')
def signin():
        return render_template("signin.html")

#About me 
@app.route('/about')
def about():
    return render_template("about.html")

# page to rent a book
@app.route('/borrow_book/<string:id_book>',methods=['GET'])
def borrow_book(id_book):
    bookSelected=id_book
    bookFound=book_controller.return_a_book(bookSelected)
    print("---------------------borrow_book_get:",bookFound)

    return render_template("borrow_book.html",book_found=bookFound)

@app.route('/rented_book/<string:id_book>',methods=['GET'])

#rent a book and show rented books
def rented_book(id_book):

        try:

                print("--------------------------------------------------------index.id_book:",id_book)
                if request.method=="GET":
                
                        quantity=request.args.get('NumberBooks')
                        print("--------------------------------------------------------index.quantity:",quantity)
                        books_rented=rented_books_controller.rentBook(id_book, session['usuario'], quantity)
                        return render_template("rented_book.html",books=books_rented)
        except Exception as ex:
                print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++Exception building rout rented book:"+str(ex))
                
#show rented books without get dates
@app.route('/rented_book_info')
def rented_book_info():

        id_usuario=rented_books_controller.searchIdUser(session['usuario'])
        books_rented=rented_books_controller.return_books(id_usuario)
        return render_template("rented_book.html",books=books_rented)



#Running my program
if __name__=='__main__':
    app.run(port=3000, debug=True)
    print(platform.architecture(), sys.maxsize)