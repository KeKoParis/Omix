from IPython.display import HTML

from models.DB_Queries import Queries


class Wrapper:
    def __init__(self):
        self.queries = Queries()

    def get_profile_data(self, login):
        profile = self.queries.get_user_profile(login)[0][1]

        if profile is None:
            return ""

        data = self._wrap(profile)

        return data

    @staticmethod
    def _wrap(profile):
        data = list()

        data.append(HTML(str(profile.phone_num)))
        data.append(HTML(profile.email))

        return data
