from abc import ABC, abstractmethod


class HttpModuleInterface(ABC):
    @abstractmethod
    def start(self, dto):
        pass
