from flask import Flask, request, render_template, redirect, url_for, flash
from config import config
from flask_mysqldb import MySQL
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from flask_wtf.csrf import CSRFProtect
from models.ModelUser import ModelUser
from models.entities.User import User

app = Flask(__name__)
db = MySQL(app)
login_manager_app = LoginManager(app)
csrf = CSRFProtect()

@login_manager_app.user_loader
def load_user(id):

    return ModelUser.get_by_id(db, id)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

        user = User(0, username, email, password)

        ModelUser.register(db, user)
        return redirect(url_for('login'))
    
    if request.method == 'GET':
        return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():

    if request.method == 'POST':

        email = request.form['email']
        password = request.form['password']

        user = User(0, '', email, password)

        logged_user = ModelUser.login(db, user)

        if logged_user:

            if logged_user.password:

                login_user(logged_user)
                return redirect(url_for('home'))
            else:

                flash('Invalid password...')
                return render_template('login.html')
        else:

            flash('User not found...')
            return render_template('login.html')
    else:

        # if current_user.is_authenticated:

        #     print('AUTENTICADO CON SESION')
        #     print(current_user.username)
        #     print(current_user.email)
        #     print(current_user.get_id())

        #     return redirect(url_for('home'))

        return render_template('login.html')

    if request.method == 'GET':
        
        return render_template('login.html')


# HOME
@app.route('/home')
@login_required
def home():

    return render_template('home.html', user=current_user)


if __name__ == '__main__':
    app.config.from_object(config['development'])
    app.run()