from Layer.HttpModules.HttpModuleInterface import HttpModuleInterface
from Layer.Types.CreateUser import CreateUser
import requests


class CreateUserInPPS(HttpModuleInterface):
    def start(self, dto: CreateUser):
        url = "http://locahost:8000/allowed-emails"

        data = {
            'email': dto.email,
            'employee_id': dto.employeeId,
        }
        headers = {
            'Content-Type': 'application/json'
        }

        response = requests.post(url, json=data, headers=headers)

        if response.status_code != 200:
            raise requests.RequestException('Ошибка выполнения запроса')
