from flask import Blueprint, render_template, request

from decorators.login_required import login_required


class StatisticsController(Blueprint):
    def __init__(self, name, import_name):
        super().__init__(name, import_name)

        @self.route('/statistics', methods=['POST', 'GET'])
        @login_required
        def stats():
            if request.method == 'POST':
                return render_template('statistics.html')
            return render_template('statistics.html')
