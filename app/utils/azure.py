

from app.client.manager import EventHubManager



class ValidationEngine:
    """
    This class is used to validate all the features provided by the user to create the consumer client.
    To make that happen the class will leverage the ValidationEngine class, that makes sure that:
    
    1. the connection_specs are correct;
    2. the eventhub instance (i.e. eventhub_id) is correct or exists;
    3. the eventhub namespace is correct or exists.
    """

    def __init__(self, connection_specs: str, eventhub_id: str, eventhub_namespace: str):

        self.connection_specs = connection_specs
        self.eventhub_id = eventhub_id
        self.eventhub_namespace = eventhub_namespace

        self.eventhub_manager = EventHubManager(self.connection_specs, self.eventhub_namespace)


    def validate_connection_specs(self) -> bool:
        """
        This method is used to validate the connection_specs provided by the user.
        """

        # TODO. the following line is not right, replace after realizing how to list the connection string
        return self.connection_specs in self.eventhub_manager.list_eventhubs()




    def validate_eventhub_id(self) -> bool:
        """
        This method is used to validate the eventhub_id provided by the user.
        """

        return self.eventhub_id in self.eventhub_manager.list_eventhubs()


    # TODO. the following method is not right, replace after creating a namespace manager client
    # def validate_eventhub_namespace(self) -> bool:
    #     """
    #     This method is used to validate the eventhub_namespace provided by the user.
    #     """

    #     return self.eventhub_namespace in self.eventhub_manager.list_eventhubs()