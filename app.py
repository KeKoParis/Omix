from Controllers.HomeController import HomeController
from Controllers.HouseController import HouseController
from Controllers.LogInController import LogInController
from Controllers.MenuController import MenuController
from Controllers.NotificationsController import NotificationsController
from Controllers.ProfileController import ProfileController
from Controllers.RegisterController import RegisterController
from Controllers.StatisticsController import StatisticsController

from app_config import app

home_controller = HomeController('home_controller', __name__)
log_in_controller = LogInController('log_in_controller', __name__)
register_controller = RegisterController('register_controller', __name__)
menu_controller = MenuController('menu_controller', __name__)
house_controller = HouseController('house_controller', __name__)
statistics_controller = StatisticsController('statistics_controller', __name__)
notifications_controller = NotificationsController('notifications_controller', __name__)
profile_controller = ProfileController('profile_controller', __name__)

app.register_blueprint(home_controller)
app.register_blueprint(log_in_controller)
app.register_blueprint(register_controller)
app.register_blueprint(menu_controller)
app.register_blueprint(house_controller)
app.register_blueprint(statistics_controller)
app.register_blueprint(notifications_controller)
app.register_blueprint(profile_controller)

if __name__ == '__main__':
    app.run(debug=True)
