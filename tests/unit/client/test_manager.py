


from unittest import TestCase, mock

from app.client.manager import EventHubManager


class EventHubManagerTests(TestCase):

    def test__init__(self):
        """
        This method is used to initialize the test class.
        """

        result = EventHubManager("connection_string", "eventhub_namespace")

        self.assertIsInstance(result, EventHubManager)
        self.assertEqual("connection_string", result.connection_features)
        self.assertEqual("eventhub_namespace", result.eventhub_namespace)


    # TODO. all the tests that we should cover to the list eventhubs method
    # 1. test that the function doesn't raise any errors when a valid connection string
    # 2. test that the function raise an Exception when a invalid connection string is provided.
    # 3. test that the function doesn't raise an Exception when the EventHub doesn't have any instances.
    # 4. make sure that the function returns an empty list when invalid subcription is provided.
    

    def test_list_eventhubs_tc1(self):
        """
        list_eventhubs - 1st Test Case Scenario

        Description: test that the function doesn't raise an Exception when a list of valid 
        eventhubs is obtained.
        """

        with mock.patch.object(EventHubManager, 'list_eventhubs') as mock_list_eventhubs:
            mock_list_eventhubs.return_value = [
                "consumer_group_1",
                "consumer_group_2"
            ]
            manager_client = EventHubManager("connection_string", "eventhub_namespace")

            result = manager_client.list_eventhubs()
            expected = ['consumer_group_1', 'consumer_group_2']

            self.assertEqual(result, expected)


    # TODO. all the tests that we should cover to the list consumer groups method
    # 1. test that the function doesn't raise any errors when a valid connection string
    # 2. test that the function raise an Exception when a invalid connection string is provided.
    # 3. test that the function doesn't raise an Exception when the EventHub doesn't have any instances.
    # 4. make sure that the function returns an empty list when invalid subcription is provided.

    def test_list_consumer_groups_tc1(self):
        """
        list_consumer_groups - 1st Test Case Scenario

        Description: test that the function doesn't raise an Exception when a list of valid 
        consumer_groups is obtained.
        """

        with mock.patch.object(EventHubManager, 'list_consumer_groups') as mock_list_consumer_groups:
            mock_list_consumer_groups.return_value = [
                "consumer_group_1",
                "consumer_group_2"
            ]
            manager_client = EventHubManager("connection_string", "eventhub_namespace")

            result = manager_client.list_consumer_groups()
            expected = ['consumer_group_1', 'consumer_group_2']

            self.assertEqual(result, expected)