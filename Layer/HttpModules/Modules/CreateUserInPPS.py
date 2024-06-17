from Layer.HttpModules.HttpModuleInterface import HttpModuleInterface
from Layer.Types.CreateUser import CreateUser
import requests
from requests.auth import HTTPBasicAuth


class CreateUserInPPS(HttpModuleInterface):
    def start(self, dto: CreateUser):
        url = "http://localhost:8000/allowed-emails/"
        username = 'admin@example.com'
        password = 'admin'

        auth = HTTPBasicAuth(username, password)

        data = {
            'email': dto.email,
            'employee_id': dto.employeeId,
        }
        headers = {
            'Content-Type': 'application/json'
        }

        response = requests.post(url, json=data, headers=headers, auth=auth)

        if response.status_code != 201:
            print(f"Ошибка: HTTP {response.status_code}")

            # Попытка извлечь сообщение об ошибке из тела ответа
            try:
                error_message = response.json().get('detail', 'Неизвестная ошибка')
                print(f"Сообщение об ошибке: {error_message}")
            except ValueError:
                # Если ответ не в формате JSON или не содержит ключ 'error'
                print("Не удалось получить детали ошибки из ответа.")
        else:
            print("Запрос выполнен успешно.")
