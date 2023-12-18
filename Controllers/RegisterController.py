from flask import Blueprint, render_template, request, redirect, url_for

from models import auth


class RegisterController(Blueprint):
    """
    Register controller
    """
    def __init__(self, name, import_name):
        super().__init__(name, import_name)

        @self.route('/register', methods=['GET', 'POST'])
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
