from flask import render_template, session, request, redirect, url_for

from app_config import app
from models import auth


@app.route('/', methods=["POST", "GET"])
def home():
    if 'username' in session:
        return render_template('home.html', login=session['login'])
    else:
        return render_template('home.html')


@app.route('/login', methods=['GET', 'POST'])
def log_in():
    if request.method == 'POST':
        login = request.form['login']
        password = request.form['password']

        if auth.log_in(login).password == password:
            session['login'] = login
            return redirect(url_for('menu'))
        else:
            return render_template('log_in.html', error='Invalid login or password')
    else:
        return render_template('log_in.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        login = request.form['login']
        password = request.form['password']
        confirm_password = request.form['confirm_password']

        if password != confirm_password:
            return render_template('register.html', error='Retry Password')

        if auth.register(login, password):
            return redirect(url_for('log_in'))

    return render_template('register.html')


@app.route('/logout')
def logout():
    session.pop('login')
    redirect(url_for('home'))


@app.route('/menu', methods=['POST', 'GET'])
def menu():
    if request.method == 'POST':
        return render_template("menu.html")

    return render_template("menu.html")


@app.route('/house', methods=['POST', 'GET'])
def house():
    if request.method == 'POST':
        return render_template('house.html')

    return render_template('house.html')


@app.route('/statistics', methods=['POST', 'GET'])
def stats():
    if request.method == 'POST':
        return render_template('statistics.html')
    return render_template('statistics.html')


@app.route('/notifications', methods=['POST', 'GET'])
def nots():
    if request.method == 'POST':
        return render_template('notifications.html')
    return render_template('notifications.html')


@app.route('/profile', methods=['POST', 'GET'])
def profile():
    if request.method == 'POST':
        return render_template('profile.html')
    return render_template('profile.html')


if __name__ == '__main__':
    app.run(debug=True)
