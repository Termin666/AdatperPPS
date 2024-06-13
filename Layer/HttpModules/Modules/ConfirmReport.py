from Layer.HttpModules.HttpModuleInterface import HttpModuleInterface
from Layer.Types.Report import Report
import requests


class ConfirmReport(HttpModuleInterface):
    def start(self, dto: Report):
        url = 'http://localhost:8080/rating'

        for item in dto.values:
            data = {
                'value': item.criterionValue,
                'date': dto.year,
                'code': dto.employeeId,
                'param': item.criterionKey
            }
            headers = {
                'Content-Type': 'application/json'
            }

            response = requests.post(url, json=data, headers=headers)

            if response.status_code != 200:
                raise requests.RequestException('Ошибка выполнения запроса')
