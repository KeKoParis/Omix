from IPython.display import HTML

from models.DB_Queries import Queries


class Wrapper:
    def __init__(self):
        self.indicators = None
        self.prop = None
        self.queries = Queries()

    def get_property(self, login: str, prop_num: int):
        """
        Method to get property in HTML.
        :param login:
        :param prop_num
        :return:
        """
        self.prop = self.queries.get_property_by_user(login)

        if self.prop is None:
            return None

        self.indicators = self.queries.get_property_indicators(self.prop[1][prop_num])[0]
        # TODO: тут список всей недвижимости юзера
        # TODO: надо отдавать 1 prop по радиобатону

        if self.indicators is None:
            return None

        res = (HTML(self._get_property_buttons(prop_num)), HTML(self._get_property_indicators()))

        return res

    def _get_property_buttons(self, prop_num: int):
        buttons = "<form>"
        for i in range(len(self.prop)):
            if i == prop_num:
                buttons += self._create_radio_button(i, self.prop[i][1].name, "checked")
            else:
                buttons += self._create_radio_button(i, self.prop[i][1].name, "")

        buttons += "</form>"

        return buttons

    @staticmethod
    def _create_radio_button(number: int, property_name: str, checked):
        button = f'\
            <input type="radio" name="option" value="{number}" onclick="handleRadioButtonClick.call(this)" {checked}>\
            {property_name}<br>\
        '

        return button

    def _get_property_indicators(self):
        indicators_str = ""
        print("self india=cator ", self.indicators[1])
        indicators_str += self._create_indicators(self.indicators[1].electricity, 'electricity')

        return indicators_str

    @staticmethod
    def _create_indicators(number: int, indicator_name):
        print("indicator ", indicator_name, number)
        indicator = f'\
        <p class="indicator">{indicator_name} {number}</p>'

        return indicator
