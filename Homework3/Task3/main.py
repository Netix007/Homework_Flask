from flask import Flask, render_template
from Task3.models import db, Student, Rating
import random


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.db'
db.init_app(app)


@app.cli.command('init-db')
def init_db():
    db.create_all()
    print('OK')


@app.cli.command('fill-db')
def fill_db():
    count_students = 10
    for i in range(1, count_students + 1):
        new_student = Student(first_name=f'Name_{i}', last_name=f'Surname_{i}', group=random.randint(1, 3),
                              email=f'email_{i}@mail.ru')
        db.session.add(new_student)
        count_subjects = random.randint(3, 6)
        subjects_list = ['математика', 'физика', 'химия', 'биология', 'русский язык', 'иностранный язык']
        for j in range(1, count_subjects + 1):
            student_subject = random.choice(subjects_list)
            new_rating = Rating(student_id=i, subject_name=student_subject, score=random.randint(2, 5))
            db.session.add(new_rating)
            subjects_list.remove(student_subject)
    db.session.commit()


@app.route('/')
@app.route('/index/')
def index():
    context = {
        'title': 'Главная'
    }
    return render_template('index.html', **context)


@app.route('/students/')
def show_students():
    all_students = Student.query.all()
    context = {
        'title': 'Студенты',
        'students': all_students
    }
    return render_template('students.html', **context)


if __name__ == '__main__':
    app.run()
