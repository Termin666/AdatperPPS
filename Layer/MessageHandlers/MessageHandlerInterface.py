from abc import ABC, abstractmethod

from Layer.HttpModules.HttpModuleInterface import HttpModuleInterface


class MessageHandlerInterface(ABC):
    def __init__(self, httpModule: HttpModuleInterface):
        self.httpModule = httpModule

    @abstractmethod
    def handle_message(self, ch, method, properties, body):
        pass
