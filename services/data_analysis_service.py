from models.dataClass.CRUD import CRUD
from services.notifications_service import NotificationService

class DataAnalysisService:

    def __init__(self):
        self._crud = CRUD()
        self._notifications = NotificationService()

    def run_service(self):
        pass

    def _collect_data(self):
        pass

    def _process_data(self):
        pass

    def _create_analytics(self):
        pass

    def _create_notification(self):
        pass


