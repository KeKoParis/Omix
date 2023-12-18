from controllers.AbstractController import AbstractController


class ProfileController(AbstractController):

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

        @self._app.route('/')
        def menu():
            pass
