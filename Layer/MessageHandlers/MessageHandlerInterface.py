from abc import ABC, abstractmethod

from Layer.HttpModules.HttpModuleInterface import HttpModuleInterface


class MessageHandlerInterface(ABC):
    @abstractmethod
    def __init__(self, httpModule: HttpModuleInterface):
        pass

    @abstractmethod
    def handle_message(self, ch, method, properties, body):
        pass
