


from azure.eventhub.aio import EventHubConsumerClient
from azure.identity.aio import DefaultAzureCredential

from app.utils.events import on_event


class EventHubConsumer:
    """
    This class is used to for every messages consume purpose within the Azure Event Hub. To make 
    it work, you need to provide the following information:
    - connection_specs: The connection string to the Event Hub instance
    - eventhub_id: The name of the Event Hub instance
    - eventhub_namespace: The name of the Event Hub namespace

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

    def __init__(self, connection_specs: str, eventhub_id: str, eventhub_namespace: str):

        self.eventhub_name = eventhub_id
        self.eventhub_namespace = eventhub_namespace
        self.connection_features = connection_specs

        self.credential = DefaultAzureCredential()


    # TODO. create a function that checks if the features provided are valid
    def check_features(self):
        """
        This method is used to check if the features provided are valid.
        """

        pass


    def create_consumer(self, consumer_group: str = '$Default'):
        """
        This method is used to create a consumer client for the Event Hub instance.

        :return: a consumer client for the Event Hub instance
        """

        client = EventHubConsumerClient.from_connection_string(
            conn_str = self.connection_features,
            consumer_group = consumer_group,
            eventhub_name = self.eventhub_name
        )

        return client
    

    async def get_messages(self):
        """
        This method is used to consume events from the Event Hub instance.
        
        :return: a string pointing out the partition and the content of the message
        """

        client = self.create_consumer()

        async with client:
            # Start receiving messages from the beginning of the partition.
            await client.receive(on_event=on_event, starting_position="-1")

        # Close credential when no longer needed.
        await self.credential.close()
