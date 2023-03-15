

from abc import ABC

from azure.identity import DefaultAzureCredential
from azure.mgmt.eventhub import EventHubManagementClient


class EventHubManager(ABC):
    """
    This class is used to manage all the Event Hub related resources. To make it work, you need to
    provide the following arguments:
    :param subscription_id: The subscription id to the Azure account
    
    On this class you can find the following methods:
    - list_instances: This method is used to list all the Event Hub instances within the Event Hub
    namespace provided.
    - list_namespaces: This method is used to list all the Event Hub namespaces within the subscription
    - list_consumer_groups: This method is used to list all the consumer groups within the Event Hub
    namespace provided.
    """

    def __init__(self, subscription_id: str):
        
        self.credential = DefaultAzureCredential()
        self.subscription_id = subscription_id

        self.management_client = EventHubManagementClient(
            credential=self.credential, 
            subscription_id=self.subscription_id
        )


    def list_namespaces(self) -> list[str]:
        """
        List all the Event Hub namespaces within the subscription provided.
        """
        return [namespace.name for namespace in self.management_client.namespaces.list()]

    
    def list_instances(self) -> list[str]:
        """
        List all the Event Hub instances within the Event Hub namespace provided.
        """
        return [eventhub.name for eventhub in self.management_client.list_event_hubs()]

    
    def list_consumer_groups(self) -> list[str]:
        """
        List all the consumer groups within the Event Hub namespace provided.
        """
        return [cg.name for cg in self.management_client.list_consumer_groups(self.eventhub_namespace)]
    

    def list_connection_specs(self) -> list[str]:
        """
        List all the connection specs within the Event Hub namespace provided.
        """
        return [cs.name for cs in self.management_client.list_authorization_rules(self.eventhub_namespace)]