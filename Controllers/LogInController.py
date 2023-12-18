from flask import Blueprint, render_template, request, redirect

from app_config import session
from models import auth


class LogInController(Blueprint):
    """
    Log in controller
    """

    def __init__(self, name, import_name):
        super().__init__(name, import_name)

        @self.route('/login', methods=['GET', 'POST'])
        def log_in():
            if request.method == 'POST':
                login = request.form['login']
                password = request.form['password']

                if auth.log_in(login).password == password:
                    session['login'] = login
                    return redirect('/menu')
                else:
                    return render_template('log_in.html', error='Invalid login or password')
            else:
                return render_template('log_in.html')
