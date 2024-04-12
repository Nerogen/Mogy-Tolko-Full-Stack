from datetime import datetime

from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

from db_init import initialize

app: Flask = Flask(__name__)
initialize()
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db: SQLAlchemy = SQLAlchemy(app)


class Client(db.Model):
    __tablename__: str = 'clients'
    account_number: db.Column = db.Column(db.Integer, primary_key=True)
    last_name: db.Column = db.Column(db.String(50))
    first_name: db.Column = db.Column(db.String(50))
    middle_name: db.Column = db.Column(db.String(50))
    date_of_birth: db.Column = db.Column(db.Date)
    inn: db.Column = db.Column(db.String(20))
    responsible_person: db.Column = db.Column(db.String(100))
    status: db.Column = db.Column(db.String(20), default='Не в работе')


class User(db.Model):
    __tablename__: str = 'users'
    id: db.Column = db.Column(db.Integer, primary_key=True)
    full_name: db.Column = db.Column(db.String(100))
    username: db.Column = db.Column(db.String(50), unique=True)
    password: db.Column = db.Column(db.String(100))


@app.route('/add_client', methods=['POST'])
def add_client():
    if request.method == 'POST':
        last_name: str = request.form['last_name']
        first_name: str = request.form['first_name']
        middle_name: str = request.form['middle_name']

        # Convert the date string to a Python date object
        date_of_birth: datetime.date = datetime.strptime(request.form['date_of_birth'], '%Y-%m-%d').date()

        inn: str = request.form['inn']
        responsible_person: str = request.form['responsible_person']

        # Create a new client
        new_client: Client = Client(
            last_name=last_name,
            first_name=first_name,
            middle_name=middle_name,
            date_of_birth=date_of_birth,
            inn=inn,
            responsible_person=responsible_person
        )

        # Add the new client to the database
        db.session.add(new_client)
        db.session.commit()

    # Redirect to the clients page after adding the client
    return redirect(url_for('login'))


# Add route for registration
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        full_name: str = request.form['full_name']
        username: str = request.form['username']
        password: str = request.form['password']

        # Check if username already exists
        existing_user: User = User.query.filter_by(username=username).first()
        if existing_user:
            return render_template('register.html', message='Username already exists. Please choose a different one.')

        # Create new user
        new_user: User = User(full_name=full_name, username=username, password=password)
        db.session.add(new_user)
        db.session.commit()

        # Redirect to login page after successful registration
        return redirect(url_for('login'))

    return render_template('register.html')


# Routes
@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username: str = request.form['username']
        password: str = request.form['password']
        user: User = User.query.filter_by(username=username).first()
        if user and user.password == password:
            return redirect(url_for('show_clients', username=username))
    return render_template('login.html')


@app.route('/clients/<username>', methods=['GET', 'POST'])
def show_clients(username):
    user: User = User.query.filter_by(username=username).first()
    clients: list[Client] = Client.query.filter_by(responsible_person=user.full_name).all()
    if request.method == 'POST':
        account_number: str = request.form['account_number']
        new_status: str = request.form['new_status']

        client: Client = Client.query.filter_by(account_number=account_number).first()
        if client:
            client.status = new_status
            db.session.commit()
    return render_template('clients.html', user=user, clients=clients)


if __name__ == '__main__':
    app.run(debug=True)
