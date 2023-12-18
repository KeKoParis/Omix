from abc import ABC, abstractmethod

from flask import Flask

from models.dataClass.CRUD import CRUD


class AbstractController(ABC):
    def __init__(self, app: Flask):
        self._crud = CRUD()
        self._app = app
        self._control()

    @abstractmethod
    def _control(self):
        pass
