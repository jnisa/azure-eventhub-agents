


import unittest
from unittest.mock import Mock
from azure.eventhub import EventData

from app.client.consumer import EventHubConsumer


# class CreateConsumerTests(unittest.TestCase):

#     def test_create_consumer_tc1(self):
#         """
#         create_consumer - 1st Test Case Scenario

#         Description: test that the function doesn't raise any errors when a valid connection string
#         and eventhub instance are provided.
#         """

#         # # Create a mock instance of EventHubClient
#         # mock_client = Mock(spec=EventHubClient)

#         # # Send an event to the event hub using the mock client
#         # event_data = EventData("Hello, world!")
#         # mock_client.send.return_value = None
#         # mock_client.send(event_data)

#         return True


# class GetMessagesTests(unittest.TestCase):

#     def test_get_messages_tc1(self):
#         """
#         get_messages - 1st Test Case Scenario

#         Description: This test case is used to test the consumption of events from the Event Hub 
#         instance.
#         """

#         # # Create a mock instance of EventHubClient
#         # mock_client = Mock(spec=EventHubClient)

#         # # Send an event to the event hub using the mock client
#         # event_data = EventData("Hello, world!")
#         # mock_client.send.return_value = None
#         # mock_client.send(event_data)

#         return True
