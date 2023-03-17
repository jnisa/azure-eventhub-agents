


from azure.eventhub import EventHubConsumerClient
from azure.identity import DefaultAzureCredential, ClientSecretCredential

from app.utils.events import on_event
from app.utils.azure import AzureValidationEngine


class EventHubConsumer:
    """
    This class is used to for every messages consume purpose within the Azure Event Hub. To make 
    it work, you need to provide the following arguments:
    :param subscription_id: The subscription id to the Azure account
    :param connection_specs: The connection specs to the Event Hub instance
    :param eventhub_instance: The Event Hub instance name
    :param eventhub_namespace: The Event Hub namespace name
    :param tenant_id: app registration tenant_id
    :param client_id: app registration client_id 
    :param client_secret: app registration client_secret
    :param consumer_group: The consumer group to the Event Hub instance
    :param starting_position: The starting position to consume the events from the Event Hub instance

    On this class you can find the following methods:
    - create_consumer: This method is used to create a consumer client for the Event Hub instance.
    - get_messages: This method is used to consume events from the Event Hub instance.
    """

    # TODO. raise an exception if the consumer_group is not provided
    # TODO. raise an exception if the consumer_group is not a string
    # TODO. raise an exception if the consumer_group is not a valid one
    # TODO. raise an exception if the eventhub_id is not provided
    # TODO. raise an exception if the eventhub_id is not a string
    # TODO. raise an exception if the eventhub_id is not a valid one
    # TODO. raise an exception if the eventhub_namespace is not provided
    # TODO. raise an exception if the eventhub_namespace is not a string
    # TODO. raise an exception if the eventhub_namespace is not a valid one
    # TODO. raise an exception if the connection_specs is not provided
    # TODO. raise an exception if the connection_specs is not a string
    # TODO. raise an exception if the connection_specs is not a valid one

    def __init__(
            self, subscription_id: str, connection_specs: str, eventhub_instance: str, eventhub_namespace: str, 
            tenant_id: str, client_id: str, client_secret: str, consumer_group: str = '$Default', starting_position: str = "-1"
        ):

        self.connection_specs = connection_specs
        self.consumer_group = consumer_group
        self.eventhub_instance = eventhub_instance
        self.eventhub_namespace = eventhub_namespace
        self.starting_position = starting_position

        # Create a credential object to authenticate the client
        credential = ClientSecretCredential(tenant_id, client_id, client_secret)

        # Validate the provided arguments
        AzureValidationEngine(
            subscription_id = subscription_id,
            consumer_group = self.consumer_group,
            connection_specs = self.connection_specs,
            eventhub_instance = self.eventhub_instance,
            eventhub_namespace = self.eventhub_namespace,
            credential = credential
        )


    def create_consumer(self) -> EventHubConsumerClient:
        """
        This method is used to create a consumer client for the Event Hub instance.

        :return: a consumer client for the Event Hub instance
        """
        return EventHubConsumerClient.from_connection_string(
            conn_str = self.connection_specs,
            consumer_group = self.consumer_group,
            eventhub_name = self.eventhub_instance
        )


    async def get_messages(self) -> str:
        """
        This method is used to consume events from the Event Hub instance.
        
        :return: a string pointing out the partition and the content of the message
        """
        consumer_client = self.create_consumer()

        async with consumer_client:
            # Start receiving messages from the beginning of the partition.
            await consumer_client.receive(on_event=on_event, starting_position=self.starting_position)

        # Close credential when no longer needed.
        await self.credential.close()
