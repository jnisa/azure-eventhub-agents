

from abc import ABC
from typing import List

from azure.identity import DefaultAzureCredential
from azure.mgmt.eventhub import EventHubManagementClient


class EventHubManager(ABC):
    """
    This class is used to manage all the Event Hub related resources. To make it work, you need to
    provide the following arguments:
    :param credential: client secret credential to access the Azure account
    :param subscription_id: subscription id to the Azure account
    
    On this class you can find the following methods:
    - list_instances: This method is used to list all the Event Hub instances within the Event Hub
    namespace provided.
    - list_namespaces: This method is used to list all the Event Hub namespaces within the subscription
    - list_consumer_groups: This method is used to list all the consumer groups within the Event Hub
    namespace provided.
    """

    def __init__(self, credential: str, subscription_id: str):

        self.management_client = EventHubManagementClient(
            credential=credential, 
            subscription_id=subscription_id
        )


    def list_namespaces(self) -> List[str]:
        """
        List all the Event Hub namespaces within the subscription provided.

        :return: list of Event Hub namespaces
        """
        return [namespace.name for namespace in self.management_client.namespaces.list()]

    
    def list_instances(self) -> List[str]:
        """
        List all the Event Hub instances within the Event Hub namespace provided.

        :return: list of Event Hub instances
        """
        return [eventhub.name for eventhub in self.management_client.list_event_hubs()]

    
    def list_consumer_groups(self) -> List[str]:
        """
        List all the consumer groups within the Event Hub namespace provided.

        :return: list of consumer groups
        """
        return [cg.name for cg in self.management_client.list_consumer_groups(self.eventhub_namespace)]
    

    def list_connection_specs(self) -> List[str]:
        """
        List all the connection specs within the Event Hub namespace provided.

        :return: list of connection specs
        """
        return [cs.name for cs in self.management_client.list_authorization_rules(self.eventhub_namespace)]