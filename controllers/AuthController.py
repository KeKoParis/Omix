from flask import Flask


class AuthController:
    def __init__(self, app: Flask):
        self._app = app
        self._control()

    def _control(self):
        @self._app.route('/')
        def log_in():
            pass

        @self._app.route('/')
        def register():
            pass

