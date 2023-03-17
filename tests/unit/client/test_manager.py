


from unittest import TestCase, mock

from app.client.manager import EventHubManager


class EventHubManagerInitTest(TestCase):
    """
    This class is used to test the __init__ method of the EventHubManager class.
    """

    def test__init__(self):
        """
        This method is used to initialize the test class.
        """
        result = EventHubManager("subscription_id")

        self.assertIsInstance(result, EventHubManager)
        self.assertEqual("subscription_id", result.subscription_id) 



class EventHubManagerListNamespacesTest(TestCase):
    """
    This class is used to test the list_namespaces method of the EventHubManager class.
    """

    def test_list_namespaces_tc1(self):
        """
        list_namespaces - 1st Test Case Scenario

        Description: test that the function doesn't raise an Exception when a list of valid namespaces 
        is obtained.
        """
        with mock.patch.object(EventHubManager, 'list_namespaces') as mock_list_namespaces:
            mock_list_namespaces.return_value = [
                "eventhub_namespace_1",
                "eventhub_namespace_2"
            ]
            manager_client = EventHubManager("test_subscription_id")

            result = manager_client.list_namespaces()
            expected = ['eventhub_namespace_1', 'eventhub_namespace_2']

            self.assertEqual(result, expected)

    
    def test_list_namespaces_tc2(self):
        """
        list_namespaces - 2nd Test Case Scenario

        Description: test that the function doesn't raise an Exception when the EventHub doesn't have any namespaces.
        """
        with mock.patch.object(EventHubManager, 'list_namespaces') as mock_list_namespaces:
            mock_list_namespaces.return_value = []
            manager_client = EventHubManager("test_subscription_id")

            result = manager_client.list_namespaces()
            expected = []

            self.assertEqual(result, expected)


class EventHubManagerListInstancesTest(TestCase):
    """
    This class is used to test the list_instances method of the EventHubManager class.
    """
    
    def test_list_instances_tc1(self):
        """
        list_instances - 1st Test Case Scenario

        Description: test that the function doesn't raise an Exception when a list of valid 
        eventhubs is obtained.
        """
        with mock.patch.object(EventHubManager, 'list_instances') as mock_list_instances:
            mock_list_instances.return_value = [
                "eventhub_instance_1",
                "eventhub_instance_2"
            ]
            manager_client = EventHubManager("test_subscription_id")

            result = manager_client.list_instances()
            expected = ['eventhub_instance_1', 'eventhub_instance_2']

            self.assertEqual(result, expected)

    
    def test_list_instances_tc2(self):
        """
        list_instances - 2nd Test Case Scenario

        Description: test that the function doesn't raise an Exception when the EventHub doesn't have any instances.
        """
        with mock.patch.object(EventHubManager, 'list_instances') as mock_list_instances:
            mock_list_instances.return_value = []
            manager_client = EventHubManager("test_subscription_id")

            result = manager_client.list_instances()
            expected = []

            self.assertEqual(result, expected)


class EventHubManagerListConsumerGroupsTest(TestCase):
    """
    This class is used to test the list_consumer_groups method of the EventHubManager class.
    """

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
            manager_client = EventHubManager("test_subscription_id")

            result = manager_client.list_consumer_groups()
            expected = ['consumer_group_1', 'consumer_group_2']

            self.assertEqual(result, expected)

    
    def test_list_consumer_groups_tc2(self):
        """
        list_consumer_groups - 2nd Test Case Scenario

        Description: test that the function doesn't raise an Exception when the EventHub doesn't have any instances.
        """
        with mock.patch.object(EventHubManager, 'list_consumer_groups') as mock_list_consumer_groups:
            mock_list_consumer_groups.return_value = []
            manager_client = EventHubManager("test_subscription_id")

            result = manager_client.list_consumer_groups()
            expected = []

            self.assertEqual(result, expected)


    def test_list_consumer_groups_tc3(self):
        """
        test_list_consumer_groups - 3rd Test Case Scenario

        Description: make sure that the function returns an empty list when invalid subcription is provided.
        """
        with mock.patch.object(EventHubManager, 'list_consumer_groups') as mock_list_consumer_groups:
            mock_list_consumer_groups.return_value = []
            manager_client = EventHubManager("test_subscription_id")

            result = manager_client.list_consumer_groups()
            expected = []

            self.assertEqual(result, expected)