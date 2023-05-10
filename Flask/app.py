from flask import Flask, render_template, request, session, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
# Import Python Bibliothek (interaktiver Debugger für Python-Programme)
import pdb
#Erstellung Flask App
app = Flask(__name__)
# Verbindung zu einer PostgreSQL-Datenbank testdb
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:EWa?ss66@localhost/testdb'
# Setzung des geheimen Schlüssels um Daten zu speichern
app.config['SECRET_KEY'] = 'secret_key'
#Erzeugung SQLAlchemy-Datenbankinstanz und anhängen an App um auf Datenbank zuzugreifen
db = SQLAlchemy(app)


class Users(db.Model):
    """
    This class represents the Users table in the database.

    Attributes:
        id (int): The id of the user.
        username (str): The username of the user.
        password (str): The password of the user.
        user_type (bool): The type of the user, either a professor or a student.
        training (str): The training that the student is currently assigned to.
    """

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    user_type = db.Column(db.Boolean())
    training = db.Column(db.String(20))

    def __repr__(self):
        """
        Returns the username of the user.
        """
        return f"User('{self.username}')"


@app.route('/login', methods=['GET', 'POST'])
def login():
    """
    This function handles the login process.

    If the user submits a valid username and password, they are redirected to the professor dashboard.
    If the user submits an invalid username or password, they are returned to the login page with an error message.
    """
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = Users.query.filter_by(username=username).first()

        if user and user.password == password:
            session['username'] = username
            return redirect(url_for('professor_dashboard'))
        else:
            return render_template('login.html', error='Invalid username or password')

    return render_template('login.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    """
    This function handles the registration process.

    If the user submits a valid username and password, a new user is created in the database and they are redirected to the login page.
    """
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = Users(username=username, password=password, user_type=False) # Set user_type to False for all new users
        db.session.add(user)
        db.session.commit()

    return render_template('register.html')


@app.route('/student_waitingroom')
def student_waitingroom():
    """
    This function handles the student waiting room page.

    If the user is logged in as a student, they are shown the page with the training they are assigned to.
    If the user is not logged in as a student, they are redirected to the login page.
    """
    if 'username' in session:
        username = session['username']
        user = Users.query.filter_by(username=username).first()
        if user.user_type == False:
            training = user.training
            return render_template('student_waitingroom.html', training=training)
    return redirect(url_for('login'))


@app.route('/Error')
def error():
    """
    This function handles the error page.
    """
    return render_template('Error.html')

@app.route('/professor_dashboard')
def professor_dashboard():
    """
    This function handles the professor dashboard page.
    If the user is logged in as a professor, they are shown the page with the available trainings.
    If the user is logged in as a student, they are redirected to the student waiting room.
    If the user is not logged in, they are redirected to the login page.
    """
    if 'username' in session:
        username = session['username']
        user = Users.query.filter_by(username=username).first()
        if user.user_type == True:
            trainings = ['Training 1', 'Training 2', 'Training 3'] # Example list of available trainings
            return render_template('professor_dashboard.html', trainings=trainings)
        elif user.user_type == False:
            return redirect(url_for('student_waitingroom'))
    return redirect(url_for('login'))

@app.route('/select_training/<training>')
def select_training(training):
    """
    This function handles the selection of a training by a professor.
    It sets the 'training' attribute of all students to the selected training.
    After updating the database, it redirects to the training page for the selected training.
    """
    students = Users.query.filter_by(user_type=False).all()
    for student in students:
        student.training = training
        db.session.commit()
    return redirect(url_for('training_page', training=training))

@app.route('/training_page/<training>')
def training_page(training):
    """
    This function handles the training page for a selected training.
    If the user is not logged in, they are redirected to the login page.
    """
    if 'username' in session:
        return render_template('training_page.html', training=training)
    else:
        return redirect(url_for('login'))

#not working yet 
@app.route('/check_training_assignment')
def check_training_assignment():
    """
    This function returns the training assignment for a student if they are logged in.
    """
    if 'username' in session:
        username = session['username']
        user = Users.query.filter_by(username=username).first()
    if user.user_type == False:
        return {'training': user.training}
    return {}

@app.route('/')
def dashboard():
    """
    This function handles the main dashboard page.
    """
    return render_template('dashboard.html')

@app.route('/debug')
def debug():
    pdb.set_trace()
    return 'Debugging'

if __name__ == '__main__':
    app.run(debug=True)