import json

from Layer.MessageHandlers.MessageHandlerInterface import MessageHandlerInterface
from Layer.Types.CreateUser import CreateUser


class CreateUserInPPSHandler(MessageHandlerInterface):
    def handle_message(self, ch, method, properties, body):
        data = json.loads(body)
        user = CreateUser(email=data['email'], employeeId=data['employee_id'])

        self.httpModule.start(user)
