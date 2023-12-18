from flask import Flask


class NotificationsController:
    def __init__(self, app: Flask):
        self._app = app
        self._control()

    def _control(self):
        @self._app.route('/')
        def render():
            pass

        @self._app.route('/')
        def send():
            pass

        @self._app.route('/')
        def menu():
            pass

        @self._app.route('/')
        def field3():
            pass
