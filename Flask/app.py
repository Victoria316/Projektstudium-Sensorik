from flask import Flask, render_template, request, session, redirect, url_for
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:EWa?ss66@localhost/testdb'
app.config['SECRET_KEY'] = 'secret_key'
db = SQLAlchemy(app)



class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    user_type = db.Column(db.Boolean())
    training = db.Column(db.String(20)) 
    def __repr__(self):
        return f"User('{self.username}')"

@app.route('/login', methods=['GET', 'POST'])
def login():
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
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        user = Users(username=username, password=password, user_type=False) # Set user_type to False for all new users
        db.session.add(user)
        db.session.commit()

    return render_template('register.html')


@app.route('/student_waitingroom')
def student_waitingroom():
 
    if 'username' in session:
        username = session['username']
        user = Users.query.filter_by(username=username).first()
        if user.user_type == False:
            training = user.training
            return render_template('student_waitingroom.html', training=training)
    return redirect(url_for('login'))


@app.route('/Error')
def error():
    return render_template('Error.html')

@app.route('/professor_dashboard')
def professor_dashboard():
    if 'username' in session:
        username = session['username']
        user = Users.query.filter_by(username=username).first()
        if user.user_type == True:
            trainings = ['Training 1', 'Training 2', 'Training 3']  # Example list of available trainings
            return render_template('professor_dashboard.html', trainings=trainings)
        elif user.user_type == False:
            return redirect(url_for('student_waitingroom'))
    return redirect(url_for('login'))


@app.route('/select_training/<training>')
def select_training(training):
    students = Users.query.filter_by(user_type=False).all()
    for student in students:
        student.training = training
        db.session.commit()
    return redirect(url_for('training_page', training=training))


@app.route('/training_page/<training>')
def training_page(training):
        if 'username' in session:
            return render_template('training_page.html', training=training)
        else:
            return redirect(url_for('login'))


#not sure if working
@app.route('/check_training_assignment')
def check_training_assignment():
    if 'username' in session:
        username = session['username']
        user = Users.query.filter_by(username=username).first()
        if user.user_type == False:
            return {'training': user.training}
    return {}
    

@app.route('/')
def dashboard():
    return render_template('dashboard.html')

if __name__ == '__main__':
    app.run(debug=True)