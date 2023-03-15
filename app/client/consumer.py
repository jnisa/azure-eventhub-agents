


from azure.eventhub.aio import EventHubConsumerClient
from azure.identity.aio import DefaultAzureCredential

from app.utils.events import on_event
from app.utils.azure import ValidationEngine


class EventHubConsumer:
    """
    This class is used to for every messages consume purpose within the Azure Event Hub. To make 
    it work, you need to provide the following information:
    - connection_specs: The connection string to the Event Hub instance
    - eventhub_id: The name of the Event Hub instance
    - eventhub_namespace: The name of the Event Hub namespace
    - starting_position: the position from which the consumer will start reading the messages

    On this class you can find the following methods:
    - create_consumer: This method is used to create a consumer client for the Event Hub instance.
    - get_messages: This method is used to consume events from the Event Hub instance. 

    TO BE UPDATED:
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
            self, 
            subscription_id: str,
            connection_specs: str, 
            consumer_group: str, 
            eventhub_instance: str, 
            eventhub_namespace: str, 
            starting_position: str = "-1"
        ):

        self.subscription_id = subscription_id
        self.connection_specs = connection_specs
        self.consumer_group = consumer_group
        self.eventhub_instance = eventhub_instance
        self.eventhub_namespace = eventhub_namespace
        self.starting_position = starting_position

        self.credential = DefaultAzureCredential()

        self.validation_engine = ValidationEngine(
            subscription_id = self.subscription_id,
            consumer_group = self.consumer_group,
            connection_specs = self.connection_features,
            eventhub_instance = self.eventhub_instance,
            eventhub_namespace = self.eventhub_namespace
        )


    def create_consumer(self, consumer_group: str = '$Default'):
        """
        This method is used to create a consumer client for the Event Hub instance.

        :return: a consumer client for the Event Hub instance
        """
        return EventHubConsumerClient.from_connection_string(
            conn_str = self.connection_features,
            consumer_group = consumer_group,
            eventhub_name = self.eventhub_name
        )


    async def get_messages(self):
        """
        This method is used to consume events from the Event Hub instance.
        
        :return: a string pointing out the partition and the content of the message
        """
        consumer_client = self.create_consumer()

        async with consumer_client:
            # Start receiving messages from the beginning of the partition.
            await consumer_client.receive(on_event=on_event, starting_position=self.reading_position)

        # Close credential when no longer needed.
        await self.credential.close()
