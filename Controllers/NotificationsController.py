from flask import Blueprint, render_template, request

from app_config import session
from decorators.login_required import login_required

from Processors.NotificationsData import Wrapper


class NotificationsController(Blueprint):
    def __init__(self, name, import_name):
        super().__init__(name, import_name)
        self.wrapper = Wrapper()

        @self.route('/notifications', methods=['POST', 'GET'])
        @login_required
        def nots():
            login = session['login']

            notif = self.wrapper.get_notifications(login)

            return render_template('notifications.html', notifications=notif)
