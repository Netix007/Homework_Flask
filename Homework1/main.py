from flask import Flask, render_template

app = Flask(__name__, static_url_path='/static')


@app.route('/index/')
def get_index_page():
    return render_template('index.html')


@app.route('/catalog/')
def get_catalog():
    return render_template('catalog.html')


@app.route('/items/')
def get_items():
    return render_template('items.html')


if __name__ == '__main__':
    app.run()
