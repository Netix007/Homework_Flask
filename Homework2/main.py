from flask import Flask, render_template, request, session, redirect, url_for, make_response

app = Flask(__name__)
app.secret_key = '5f214cacbd30c2ae4784b520f17912ae0d5d8c16ae98128e3f549546221265e4'


@app.route('/')
def main():
    return render_template('index.html')


@app.route('/task07/', methods=['GET', 'POST'])
def task07():
    if request.method == 'POST':
        num = int(request.form.get('num'))
        return f'Input number: {num}. Square number: {num*num}'
    return render_template('task07.html')


@app.route('/task09/', methods=['GET', 'POST'])
def task09():
    if 'username' in session:
        return render_template('hello_page.html', name=session['username'])
    else:
        return redirect(url_for('login'))


@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form.get('username') or 'NoName'
        session['email'] = request.form.get('email') or 'NoName'
        return redirect(url_for('task09'))
    return render_template('login.html')


@app.route('/logout/')
def logout():
    session.pop('username', None)
    session.pop('email', None)
    return redirect(url_for('login'))


if __name__ == '__main__':
    app.run()
