from Layer.HttpModules.HttpModuleInterface import HttpModuleInterface
from Layer.MessageHandlers.MessageHandlerInterface import MessageHandlerInterface
import json

from Layer.Types.Report import Report
from Layer.Types.ReportValue import ReportValue


class ConfirmReportHandler(MessageHandlerInterface):
    def __init__(self, httpModule: HttpModuleInterface):
        self.httpModule = httpModule

    def handle_message(self, ch, method, properties, body):
        data = json.loads(body)
        values = [ReportValue(**value) for value in data['values']]
        report = Report(year=data['year'], employeeId=data['employeeId'], values=values)

        self.httpModule.start(report)
