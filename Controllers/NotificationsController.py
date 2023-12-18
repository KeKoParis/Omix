from flask import Blueprint, render_template, request

from decorators.login_required import login_required


class NotificationsController(Blueprint):
    def __init__(self, name, import_name):
        super().__init__(name, import_name)

        @self.route('/notifications', methods=['POST', 'GET'])
        @login_required
        def nots():
            if request.method == 'POST':
                return render_template('notifications.html')
            return render_template('notifications.html')
