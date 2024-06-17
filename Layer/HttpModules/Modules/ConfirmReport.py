from Layer.HttpModules.HttpModuleInterface import HttpModuleInterface
from Layer.Types.Report import Report
import requests
from base64 import b64encode


class ConfirmReport(HttpModuleInterface):
    def start(self, dto: Report):
        url = 'http://localhost:8080/InfoBase/hs/rating/value'

        username = 'ЭВМ'
        password = 'pO5qy1tu'

        auth_encoded = b64encode(f"{username}:{password}".encode('utf-8')).decode('utf-8')

        for item in dto.values:
            data = {
                'value': item.criterionValue,
                'date': f"{dto.year}",
                'code': dto.employeeId,
                'param': item.criterionKey
            }

            print(data)

            headers = {
                'Content-Type': 'application/json',
                'Authorization': f'Basic {auth_encoded}'
            }

            response = requests.post(url, json=data, headers=headers)

            if response.status_code != 200:
                raise requests.RequestException(f"Ошибка выполнения запроса  {response.status_code}")
