

from abc import ABC
from typing import List

from azure.mgmt.eventhub import EventHubManagementClient

from app.constants.eventhub import CONNECTION_STRING


class AzureStockManager(ABC):
    """
    This class is used to manage some of the Azure res. 
    
    To make it work, you need to provide the following arguments:
    :param credential: client secret credential to access the Azure account
    :param subscription_id: subscription id to the Azure account
    
    On this class you can find the following methods:
    - list_namespaces: list all the Event Hub namespaces within the eventhub client created;
    - list_instances: list all the Event Hub instances within the Event Hub namespace provided;
    - list_consumer_groups: list all the consumer groups within the Event Hub namespace provided;
    - list_connection_specs: list all the connection specs within the Event Hub namespace provided.
    """

    # TODO. self.eventhub_namespace needs to be added to the __init__ method.
    def __init__(self, credential: str, subscription_id: str):

        self.eventhub_mgmt_client = EventHubManagementClient(
            credential=credential, 
            subscription_id=subscription_id
        )


    def list_namespaces(self) -> List[str]:
        """
        List all the Event Hub namespaces within the subscription provided.

        :return: list of Event Hub namespaces
        """
        return [namespace.name for namespace in self.eventhub_mgmt_client.namespaces.list()]

    
    def list_instances(self, resource_group: str, eventhub_namespace: str) -> List[str]:
        """
        List all the Event Hub instances within the Event Hub namespace provided.
        
        :param resource_group: name of the resource group
        :param eventhub_namespace: name of the Event Hub namespace
        :return: list of Event Hub instances
        """
        return [eventhub.name for eventhub in self.eventhub_mgmt_client.list_event_hubs(resource_group, eventhub_namespace)]


    def list_connection_specs(self, resource_group: str, eventhub_namespace: str, key_name: str = 'RootManageSharedAccessKey') -> List[str]:
        """
        List all the connection strings of a given Event Hub namespace.

        :param resource_group: name of the resource group
        :param eventhub_namespace: name of the Event Hub namespace
        :return: list of connection strings
        """
        return [
            CONNECTION_STRING.replace('EVENTHUB_NAMESPACE', eventhub_namespace).replace('PRIMARY_KEY', key.primary_key) 
            for key in self.eventhub_mgmt_client.list_keys(resource_group, eventhub_namespace, key_name)
        ]


    def list_consumer_groups(self, resource_group: str, eventhub_namespace: str) -> List[str]:
        """
        List all the consumer groups within the Event Hub namespace provided.

        :param resource_group: name of the resource group
        :param eventhub_namespace: name of the Event Hub namespace
        :return: list of consumer groups
        """
        return [
            resource_group.name 
            for resource_group in self.eventhub_mgmt_client.consumer_groups.list_by_event_hub(resource_group, eventhub_namespace)
        ]