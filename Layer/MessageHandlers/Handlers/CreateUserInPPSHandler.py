import json

from Layer.HttpModules.HttpModuleInterface import HttpModuleInterface
from Layer.MessageHandlers.MessageHandlerInterface import MessageHandlerInterface
from Layer.Types.CreateUser import CreateUser


class CreateUserInPPSHandler(MessageHandlerInterface):
    def __init__(self, httpModule: HttpModuleInterface):
        self.httpModule = httpModule

    def handle_message(self, ch, method, properties, body):
        data = json.loads(body)
        user = CreateUser(email=data['email'], employeeId=data['employee_id'])

        self.httpModule.start(user)
