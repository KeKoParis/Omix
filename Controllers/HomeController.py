from flask import Blueprint, render_template

from app_config import session


class HomeController(Blueprint):
    """
    Home (greeting) page controller
    """
    def __init__(self, name, import_name):
        super().__init__(name, import_name)

        @self.route('/', methods=["POST", "GET"])
        def home():
            if 'username' in session:
                return render_template('home.html', login=session['login'])
            else:
                return render_template('home.html')
