


from unittest.mock import Mock
from app.client.consumer import EventHubConsumer
from azure.eventhub import EventHubClient, EventData


class GetMessagesTests(unittest.TestCase):

    def test_get_messages_tc1(self):
        """
        
        """

        # Create a mock instance of EventHubClient
        mock_client = Mock(spec=EventHubClient)

        # Send an event to the event hub using the mock client
        event_data = EventData("Hello, world!")
        mock_client.send.return_value = None
        mock_client.send(event_data)

        assert result == expected

