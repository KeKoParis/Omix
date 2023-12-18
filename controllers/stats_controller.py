from controllers.AbstractController import AbstractController


class StatsController(AbstractController):

    def _control(self):
        @self._app.route('/')
        def render():
            pass

        @self._app.route('/')
        def get_prediction():
            pass

        @self._app.route('/')
        def get_stats():
            pass

        @self._app.route('/')
        def menu():
            pass
