from flask import Blueprint, render_template, request

from decorators.login_required import login_required


class ProfileController(Blueprint):
    def __init__(self, name, import_name):
        super().__init__(name, import_name)

        @self.route('/profile', methods=['POST', 'GET'])
        @login_required
        def profile():
            if request.method == 'POST':
                return render_template('profile.html')
            return render_template('profile.html')
