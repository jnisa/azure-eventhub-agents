

from abc import ABC

from azure.identity import DefaultAzureCredential
from azure.mgmt.eventhub import EventHubManagementClient


class EventHubManager(ABC):
    """
    This class is used to manage all the Event Hub related resources. To make it work, you need to
    provide the following information:
    - connection_specs: The connection string to the Event Hub instance
    - eventhub_namespace: The name of the Event Hub namespace
    
    On this class you can find the following methods:
    - list_eventhubs: This method is used to list all the Event Hub instances within the Event Hub
    namespace provided.
    - list_consumer_groups: This method is used to list all the consumer groups within the Event Hub
    namespace provided.
    """

    def __init__(self, connection_specs: str, eventhub_namespace: str):
        
        self.credential = DefaultAzureCredential()

        self.connection_features = connection_specs
        self.eventhub_namespace = eventhub_namespace
        self.management_client = EventHubManagementClient(self.credential, self.connection_features)


    @staticmethod
    def list_eventhubs(self) -> list:
        """
        This method is used to list all the Event Hub instances within the Event Hub namespace provided.
        """

        return [eventhub.name for eventhub in self.management_client.list_event_hubs()]


    @staticmethod
    def list_consumer_groups(self) -> list:
        """
        This method is used to list all the consumer groups within the Event Hub namespace provided.
        """

        return [consumer_group.name for consumer_group in self.management_client.list_consumer_groups(self.eventhub_namespace)]
    