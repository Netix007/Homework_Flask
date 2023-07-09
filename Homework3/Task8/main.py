from flask import Flask, render_template, request
from Task8.models import db, User
from Task8.forms import RegistrationForm
from flask_wtf.csrf import CSRFProtect
from werkzeug.security import generate_password_hash

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db.init_app(app)
app.config['SECRET_KEY'] = 'mysecretkey'
csrf = CSRFProtect(app)


@app.cli.command('init-db')
def init_db():
    db.create_all()
    print('OK')


@app.route('/')
@app.route('/index/')
def index():
    context = {
        'title': 'Главная'
    }
    return render_template('index.html', **context)


@app.route('/register/', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if request.method == 'POST' and form.validate():
        first_name = form.first_name.data
        last_name = form.last_name.data
        email = form.email.data
        password = generate_password_hash(form.password.data)
        user = User(first_name=first_name, last_name=last_name, email=email, password=password)
        db.session.add(user)
        db.session.commit()
        print(first_name, last_name,  email, password)
    return render_template('forms.html', form=form)


if __name__ == '__main__':
    app.run()
