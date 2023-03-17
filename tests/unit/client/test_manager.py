


from unittest import TestCase, mock

from app.client.manager import AzureStockManager


class AzureStockManagerInitTest(TestCase):
    """
    This class is used to test the __init__ method of the AzureStockManager class.
    """

    def test__init__tc1(self):
        """
        __init__ - 1st Test Case Scenario

        Description: test the initialization of the AzureStockManager class when the correct parameters
        are provided.
        """
        result = AzureStockManager("test_credential", "test_subscription_id")

        self.assertIsInstance(result, AzureStockManager)
        self.assertEqual("test_credential", result.credential) 
        self.assertEqual("test_subscription_id", result.subscription_id) 


    # TODO. when the subscription_id is not provided
    def test__init__tc2(self):
        """
        __init__ - 2nd Test Case Scenario

        Description: test the initialization of the AzureStockManager class when the subscription_id 
        is not provided.
        """
        result = AzureStockManager("test_credential")

        self.assertIsInstance(result, AzureStockManager)
        self.assertEqual("test_credential", result.credential) 
        self.assertEqual("test_subscription_id", result.subscription_id) 


class AzureStockManagerListNamespacesTest(TestCase):
    """
    This class is used to test the list_namespaces method of the AzureStockManager class.
    """

    def test_list_namespaces_tc1(self):
        """
        list_namespaces - 1st Test Case Scenario

        Description: test that the function doesn't raise an Exception when a list of valid namespaces 
        is obtained.
        """
        with mock.patch.object(AzureStockManager, 'list_namespaces') as mock_list_namespaces:
            mock_list_namespaces.return_value = [
                "eventhub_namespace_1",
                "eventhub_namespace_2"
            ]
            manager_client = AzureStockManager("test_credential", "test_subscription_id")

            result = manager_client.list_namespaces()
            expected = ['eventhub_namespace_1', 'eventhub_namespace_2']

            self.assertEqual(result, expected)

    
    def test_list_namespaces_tc2(self):
        """
        list_namespaces - 2nd Test Case Scenario

        Description: test that the function doesn't raise an Exception when the EventHub doesn't have any namespaces.
        """
        with mock.patch.object(AzureStockManager, 'list_namespaces') as mock_list_namespaces:
            mock_list_namespaces.return_value = []
            manager_client = AzureStockManager("test_credential", "test_subscription_id")

            result = manager_client.list_namespaces()
            expected = []

            self.assertEqual(result, expected)


class AzureStockManagerListInstancesTest(TestCase):
    """
    This class is used to test the list_instances method of the AzureStockManager class.
    """
    
    def test_list_instances_tc1(self):
        """
        list_instances - 1st Test Case Scenario

        Description: test that the function doesn't raise an Exception when a list of valid 
        eventhubs is obtained.
        """
        with mock.patch.object(AzureStockManager, 'list_instances') as mock_list_instances:
            mock_list_instances.return_value = [
                "eventhub_instance_1",
                "eventhub_instance_2"
            ]
            manager_client = AzureStockManager("test_credential", "test_subscription_id")

            result = manager_client.list_instances()
            expected = ['eventhub_instance_1', 'eventhub_instance_2']

            self.assertEqual(result, expected)

    
    def test_list_instances_tc2(self):
        """
        list_instances - 2nd Test Case Scenario

        Description: test that the function doesn't raise an Exception when the EventHub doesn't have any instances.
        """
        with mock.patch.object(AzureStockManager, 'list_instances') as mock_list_instances:
            mock_list_instances.return_value = []
            manager_client = AzureStockManager("test_credential", "test_subscription_id")

            result = manager_client.list_instances()
            expected = []

            self.assertEqual(result, expected)

    
    # TODO. when the resource_group is not provided
    # TODO. when the eventhub_namespace is not provided



class AzureStockManagerListConsumerGroupsTest(TestCase):
    """
    This class is used to test the list_consumer_groups method of the AzureStockManager class.
    """

    def test_list_consumer_groups_tc1(self):
        """
        list_consumer_groups - 1st Test Case Scenario

        Description: test that the function doesn't raise an Exception when a list of valid 
        consumer_groups is obtained.
        """
        with mock.patch.object(AzureStockManager, 'list_consumer_groups') as mock_list_consumer_groups:
            mock_list_consumer_groups.return_value = [
                "consumer_group_1",
                "consumer_group_2"
            ]
            manager_client = AzureStockManager("test_credential", "test_subscription_id")

            result = manager_client.list_consumer_groups()
            expected = ['consumer_group_1', 'consumer_group_2']

            self.assertEqual(result, expected)

    
    def test_list_consumer_groups_tc2(self):
        """
        list_consumer_groups - 2nd Test Case Scenario

        Description: test that the function doesn't raise an Exception when the EventHub doesn't have any instances.
        """
        with mock.patch.object(AzureStockManager, 'list_consumer_groups') as mock_list_consumer_groups:
            mock_list_consumer_groups.return_value = []
            manager_client = AzureStockManager("test_credential", "test_subscription_id")

            result = manager_client.list_consumer_groups()
            expected = []

            self.assertEqual(result, expected)


    def test_list_consumer_groups_tc3(self):
        """
        test_list_consumer_groups - 3rd Test Case Scenario

        Description: make sure that the function returns an empty list when invalid subcription is provided.
        """
        with mock.patch.object(AzureStockManager, 'list_consumer_groups') as mock_list_consumer_groups:
            mock_list_consumer_groups.return_value = []
            manager_client = AzureStockManager("test_credential", "test_subscription_id")

            result = manager_client.list_consumer_groups()
            expected = []

            self.assertEqual(result, expected)