from flask import Blueprint, render_template, request, redirect

from Processors.HouseData import Wrapper
from app_config import session
from decorators.login_required import login_required

radio_button_value = -1

class HouseController(Blueprint):
    """
    House page controller.
    """

    def __init__(self, name, import_name):
        global radio_button_value
        radio_button_value = -1
        super().__init__(name, import_name)
        self.wrapper = Wrapper()

        @self.route('/house', methods=['POST', 'GET'])
        @login_required
        def house():
            login = session['login']
            global radio_button_value

            buttons_indicators = self.wrapper.get_property(login, radio_button_value)
            print("val ind ", buttons_indicators[1].data)
            print("val house ", radio_button_value)
            print(render_template('house.html', buttons=buttons_indicators[0], indicators=buttons_indicators[1]))
            return render_template('house.html', buttons=buttons_indicators[0], indicators=buttons_indicators[1])

        @self.route('/house/radio_button', methods=['POST', 'GET'])
        @login_required
        def radio_button_prop():
            print("change global ")
            global radio_button_value

            val = request.args.get('option')
            print("val ", val)
            if val is not None:
                radio_button_value = int(val)
            return redirect('/house')
