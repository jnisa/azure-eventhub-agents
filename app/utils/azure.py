

import logging

from app.client.manager import EventHubManager

from azure.identity import DefaultAzureCredential
from azure.mgmt.eventhub.models import EHNamespace
from azure.mgmt.eventhub import EventHubManagementClient


class ValidationEngine:
    """
    This class is used to validate all the features provided by the user to create the consumer client.
    To make that happen the class will leverage the ValidationEngine class, that makes sure that:
    
    1. the connection_specs are correct;
    2. the eventhub instance (i.e. eventhub_id) is correct or exists;
    3. the eventhub namespace is correct or exists.

    To make this class work you need to provide the following information:
    :param subscritpion_id: The subscription id to the Azure account
    :param connection_specs: The connection string to the Event Hub instance
    :param eventhub_instance: The name of the Event Hub instance
    :param eventhub_namespace: The name of the Event Hub namespace
    """

    def __init__(
            self, 
            subscription_id: str, 
            consumer_group: str,
            connection_specs: str, 
            eventhub_instance: str, 
            eventhub_namespace: str
        ):

        self.subscription_id = subscription_id
        self.consumer_group = consumer_group
        self.connection_specs = connection_specs
        self.eventhub_instance = eventhub_instance
        self.eventhub_namespace = eventhub_namespace

        self.credential = DefaultAzureCredential()

        self.eventhub_manager = EventHubManager(self.connection_specs, self.eventhub_namespace)

        if not self.call_all_methods():
            logging.error("The provided information is not correct. Please check the documentation and try again.")
        else:
            logging.info("The provided information is correct. Let's proceed with the creation of the consumer client.")


    def validate_eventhub_namespace(self) -> bool:
        """
        This method is used to validate the eventhub_namespace provided by the user.
        """
        return self.eventhub_namespace in self.eventhub_manager.list_namespaces()
    

    def validate_eventhub_instance(self) -> bool:
        """
        This method is used to validate the eventhub_instance provided by the user.
        """
        return self.eventhub_id in self.eventhub_manager.list_instances()


    def validate_consumer_group(self) -> bool:
        """
        This method is used to validate the consumer_group provided by the user.
        """
        return self.consumer_group in self.eventhub_manager.list_consumer_groups()


    def validate_connection_specs(self) -> bool:
        """
        This method is used to validate the connection_specs provided by the user.
        """
        return self.connection_specs in self.eventhub_manager.list_keys()


    def call_all_methods(self) -> None:
        """
        This method is used to call all the methods in this class.
        """
        self.validate_eventhub_namespace()
        self.validate_eventhub_instance()
        self.validate_consumer_group()