from IPython.display import HTML

from models.DB_Queries import Queries


class Wrapper:
    def __init__(self):
        self.queries = Queries()

    def get_notifications(self, login):
        notif = self.queries.get_notifications_by_user(login)
        print("notnot ", notif)
        html_notif = HTML(self._wrap(notif))

        return html_notif

    @staticmethod
    def _wrap(notif):
        notifications_str = ""
        for i in notif:
            notifications_str += f'\
                <li>\
                    <div class="notification">\
                        <span class="notification-title">Notification</span>\
                        <div class="popup">\
                            <p>{i[1].notification}</p>\
                        </div>\
                    </div>\
                </li>'

        return notifications_str
