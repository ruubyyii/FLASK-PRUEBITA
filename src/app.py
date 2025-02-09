from flask import Flask, request, render_template, redirect, url_for
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

        user = User(username, email, password)

        ModelUser.register(db, user)
    
    return render_template('register.html')


if __name__ == '__main__':
    app.config.from_object(config['development'])
    app.run()