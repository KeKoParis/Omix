from controllers.AbstractController import AbstractController


class MenuController(AbstractController):

    def _control(self):
        @self._app.route('/')
        def render():
            pass

        @self._app.route('/')
        def switch():
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
