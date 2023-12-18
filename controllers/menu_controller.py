from flask import Flask


class MenuController:
    def __init__(self, app: Flask):
        self._app = app
        self._control()

    def _control(self):
        @self._app.route('/')
        def render():
            pass

        @self._app.route('/')
        def field():
            pass

        @self._app.route('/')
        def field2():
            pass

        @self._app.route('/')
        def field3():
            pass
