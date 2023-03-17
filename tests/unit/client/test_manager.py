


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
        result = AzureStockManager(credential="test_credential", subscription_id="test_subscription_id")

        self.assertIsInstance(result, AzureStockManager)


    def test__init__tc2(self):
        """
        __init__ - 2nd Test Case Scenario

        Description: test the initialization of the AzureStockManager class when the credential 
        is not provided.
        """
        with self.assertRaises(TypeError):
            AzureStockManager(credential="test_credential")


    def test__init__tc3(self):
        """
        __init__ - 3rd Test Case Scenario

        Description: test the initialization of the AzureStockManager class when the subscription_id 
        is not provided.
        """
        with self.assertRaises(TypeError):
            AzureStockManager(subscription_id="test_subscription_id")


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

            result = manager_client.list_instances('resource_group', 'eventhub_namespace')
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

            result = manager_client.list_instances('test_resource_group', 'test_eventhub_namespace')
            expected = []

            self.assertEqual(result, expected)

    
    def test_list_instances_tc3(self):
        """
        list_instances - 3rd Test Case Scenario

        Description: test that the function doesn't raise an Exception when the resource_group is not provided.
        """
        manager_client = AzureStockManager("test_credential", "test_subscription_id")

        with self.assertRaises(TypeError):
            manager_client.list_instances(eventhub_namespace='test_eventhub_namespace')


    def test_list_instances_tc4(self):
        """
        list_instances - 4th Test Case Scenario

        Description: test that the function doesn't raise an Exception when the eventhub_namespace is not provided.
        """
        manager_client = AzureStockManager("test_credential", "test_subscription_id")

        with self.assertRaises(TypeError):
            manager_client.list_instances(resource_group='test_resource_group')


class AzureStockManagerListConnectionSpecs(TestCase):
    """
    This class is used to test the list_connection_specs method of the AzureStockManager class.
    """

    def test_list_connection_specs_tc1(self):
        """
        list_connection_specs - 1st Test Case Scenario

        Description: test that the function doesn't raise an Exception when a list of valid 
        connection_specs is obtained.
        """
        with mock.patch.object(AzureStockManager, 'list_connection_specs') as mock_list_connection_specs:
            mock_list_connection_specs.return_value = [
                "connection_spec_1",
                "connection_spec_2"
            ]
            manager_client = AzureStockManager("test_credential", "test_subscription_id")

            result = manager_client.list_connection_specs('resource_group', 'eventhub_namespace', 'eventhub_instance')
            expected = ['connection_spec_1', 'connection_spec_2']

            self.assertEqual(result, expected)

    
    def test_list_connection_specs_tc2(self):
        """
        list_connection_specs - 2nd Test Case Scenario

        Description: test that the function doesn't raise an Exception when the EventHub doesn't have any connection_specs.
        """

        with mock.patch.object(AzureStockManager, 'list_connection_specs') as mock_list_connection_specs:
            mock_list_connection_specs.return_value = []
            manager_client = AzureStockManager("test_credential", "test_subscription_id")

            result = manager_client.list_connection_specs('test_resource_group', 'test_eventhub_namespace', 'test_eventhub_instance')
            expected = []

            self.assertEqual(result, expected)

    
    def test_list_connection_specs_tc3(self):
        """
        list_connection_specs - 3rd Test Case Scenario

        Description: test that the function doesn't raise an Exception when the resource_group is not provided.
        """
        manager_client = AzureStockManager("test_credential", "test_subscription_id")

        with self.assertRaises(TypeError):
            manager_client.list_connection_specs(eventhub_namespace='test_eventhub_namespace', eventhub_instance='test_eventhub_instance')


    def test_list_connection_specs_tc4(self):
        """
        list_connection_specs - 4th Test Case Scenario

        Description: test that the function doesn't raise an Exception when the eventhub_namespace is not provided.
        """
        manager_client = AzureStockManager("test_credential", "test_subscription_id")

        with self.assertRaises(TypeError):
            manager_client.list_connection_specs(resource_group='test_resource_group', eventhub_instance='test_eventhub_instance')


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

            result = manager_client.list_consumer_groups('test_resource_group', 'test_eventhub_namespace')
            expected = []

            self.assertEqual(result, expected)


    def test_list_consumer_groups_tc3(self):
        """
        test_list_consumer_groups - 3rd Test Case Scenario

        Description: test that the function doesn't raise an Exception when the resource_group is not provided.
        """
        manager_client = AzureStockManager("test_credential", "test_subscription_id")

        with self.assertRaises(TypeError):
            manager_client.list_consumer_groups(eventhub_namespace='test_eventhub_namespace')


    def test_list_consumer_groups_tc4(self):
        """
        list_consumer_groups - 4th Test Case Scenario

        Description: test that the function doesn't raise an Exception when the eventhub_namespace is not provided.
        """
        manager_client = AzureStockManager("test_credential", "test_subscription_id")

        with self.assertRaises(TypeError):
            manager_client.list_consumer_groups(resource_group='test_resource_group')
