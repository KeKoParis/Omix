from flask import Blueprint, render_template, request, redirect

from app_config import session
from decorators.login_required import login_required


class MenuController(Blueprint):
    """
    Menu controller
    """

    def __init__(self, name, import_name):
        super().__init__(name, import_name)

        @self.route('/menu', methods=['POST', 'GET'])
        @login_required
        def menu():
            if request.method == 'POST':
                return render_template("menu.html")

            return render_template("menu.html")

        @self.route('/logout', methods=['POST', 'GET'])
        def logout():
            session.pop('login')
            return redirect('/')
