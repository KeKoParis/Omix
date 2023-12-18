from flask import Blueprint, render_template, request

from decorators.login_required import login_required


class HouseController(Blueprint):
    """
    House page controller.
    """

    def __init__(self, name, import_name):
        super().__init__(name, import_name)

        @self.route('/house', methods=['POST', 'GET'])
        @login_required
        def house():
            if request.method == 'POST':
                return render_template('house.html')

            return render_template('house.html')
