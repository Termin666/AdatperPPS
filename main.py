from Layer.HttpModules.Modules.ConfirmReport import ConfirmReport
from Layer.HttpModules.Modules.CreateUserInPPS import CreateUserInPPS
from Layer.MessageHandlers.Handlers.ConfirmReportHandler import ConfirmReportHandler
from Layer.MessageHandlers.Handlers.CreateUserInPPSHandler import CreateUserInPPSHandler
from Layer.RabbitMQClient.RabbitMQClient import RabbitMQClient


def main():
    connect = RabbitMQClient()
    connect.start()
    connect.add_topic("rating_exchange", ConfirmReportHandler(ConfirmReport()))
    connect.add_topic("user_exchange", CreateUserInPPSHandler(CreateUserInPPS()))

    connect.start_consuming()


main()
