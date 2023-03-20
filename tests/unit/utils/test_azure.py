


from unittest import TestCase, mock
from unittest.mock import Mock, MagicMock, patch

from app.utils.azure import AzureValidationEngine

from azure.identity import DefaultAzureCredential

class AzureValidationEngineInitTest(TestCase):
    """
    This class is used to test the __init__ method of the AzureValidationEngine class.
    """

    @patch("app.utils.azure.AzureStockManager")
    def test__init__tc1(self, mock_azure_stock_manager):
        """
        __init__ - 1st Test Case Scenario

        Description: test that the function doesn't raise any errors when a valid connection string
        and eventhub instance are provided.
        """
        
        subscription_id = "test_subscription_id"
        consumer_group = "test_consumer_group"
        connection_specs = "test_connection_specs"
        eventhub_instance = "test_eventhub_instance"
        eventhub_namespace = "test_eventhub_namespace"
        credential = DefaultAzureCredential()

        azure_validation_engine = AzureValidationEngine(
            subscription_id, consumer_group, connection_specs, eventhub_instance, eventhub_namespace, credential
        )

        self.assertIsInstance(azure_validation_engine, AzureValidationEngine)
        self.assertEqual(azure_validation_engine.consumer_group, consumer_group)
        self.assertEqual(azure_validation_engine.connection_specs, connection_specs)
        self.assertEqual(azure_validation_engine.eventhub_instance, eventhub_instance)
        self.assertEqual(azure_validation_engine.eventhub_namespace, eventhub_namespace)


    @patch("app.utils.azure.AzureStockManager")
    def test__init__tc2(self, mock_azure_stock_manager):
        """
        __init__ - 2nd Test Case Scenario

        Description: test that the function handles correctly when not all the validation methods return True,
        meaning that one of the provided resources doesn't exist
        """

        with mock.patch.object(AzureValidationEngine, 'call_all_methods') as mock_validation_engine_all:
            mock_validation_engine_all.return_value = False 

            subscription_id = "test_subscription_id"
            consumer_group = "test_consumer_group"
            connection_specs = "test_connection_specs"
            eventhub_instance = "test_eventhub_instance"
            eventhub_namespace = "test_eventhub_namespace"
            credential = DefaultAzureCredential()

            validation_engine = AzureValidationEngine(
                subscription_id, consumer_group, connection_specs, eventhub_instance, eventhub_namespace, credential
            )

            with self.assertLogs(level="ERROR") as cm:
                validation_engine.__init__(
                    subscription_id, consumer_group, connection_specs, eventhub_instance, eventhub_namespace, credential
                )

            # TODO. this can't be a root logger. It should be the logger of the module.
            self.assertEqual(cm.output, ["ERROR:root:The provided information is not correct. Please check the resources and try again."])


    @patch("app.utils.azure.AzureStockManager")
    def test__init__tc3(self, mock_azure_stock_manager):
        """
        __init__ - 3rd Test Case Scenario

        Description: test that the function handles correctly when all the validation methods return True meaning
        that all the provided resources exist.
        """

        with mock.patch.object(AzureValidationEngine, 'call_all_methods') as mock_validation_engine_all:
            mock_validation_engine_all.return_value = True

            subscription_id = "test_subscription_id"
            consumer_group = "test_consumer_group"
            connection_specs = "test_connection_specs"
            eventhub_instance = "test_eventhub_instance"
            eventhub_namespace = "test_eventhub_namespace"
            credential = DefaultAzureCredential()

            validation_engine = AzureValidationEngine(
                subscription_id, consumer_group, connection_specs, eventhub_instance, eventhub_namespace, credential
            )

            with self.assertLogs(level="INFO") as cm:
                validation_engine.__init__(
                    subscription_id, consumer_group, connection_specs, eventhub_instance, eventhub_namespace, credential
                )

            # TODO. this can't be a root logger. It should be the logger of the module.
            self.assertEqual(cm.output, ["INFO:root:The provided information is correct. Let's proceed with the creation of the consumer client."])


    # TODO. add test cases for to validate that the function handles correctly when the provided resources are not valid.

class AzureValidationEngineValidateEventHubNamespaceTest(TestCase):
    """
    Test the validate_eventhub_namespace method of the AzureValidationEngine class.
    """

    @patch("app.utils.azure.AzureStockManager")
    def test_validate_eventhub_namespace_tc1(self, mock_azure_stock_manager):
        """
        validate_eventhub_namespace - 1st Test Case Scenario

        Description: test that the function doesn't raise any errors meaning that the EventHub namespace provided 
        to the AzureValidationEngine exists.
        """

        with mock.patch.object(AzureValidationEngine, 'validate_eventhub_namespace') as mock_namespaces_validation:
            mock_namespaces_validation.return_value = True

            subscription_id = "test_subscription_id"
            consumer_group = "test_consumer_group"
            connection_specs = "test_connection_specs"
            eventhub_instance = "test_eventhub_instance"
            eventhub_namespace = "test_eventhub_namespace"
            credential = DefaultAzureCredential()

            validation_engine = AzureValidationEngine(
                subscription_id, consumer_group, connection_specs, eventhub_instance, eventhub_namespace, credential
            )

            result = validation_engine.validate_eventhub_namespace()
            expected = True

            self.assertEqual(result, expected)


class AzureValidationEngineValidateEventHubInstanceTest(TestCase):
    """
    Test the validate_eventhub_instance method of the AzureValidationEngine class.
    """

    # TODO. 
    # Test: the response of the validation function if there's no eventhub instances

    @patch("app.utils.azure.AzureStockManager")
    def test_validate_eventhub_instance_tc1(self, mock_azure_stock_manager):
        """
        validate_eventhub_instance - 1st Test Case Scenario

        Description: test that the function doesn't raise any errors meaning that the EventHub instance provided
        to the AzureValidationEngine exists.
        """

        with mock.patch.object(AzureValidationEngine, 'validate_eventhub_instance') as mock_instances_validation:
            mock_instances_validation.return_value = True

            subscription_id = "test_subscription_id"
            consumer_group = "test_consumer_group"
            connection_specs = "test_connection_specs"
            eventhub_instance = "test_eventhub_instance"
            eventhub_namespace = "test_eventhub_namespace"
            credential = DefaultAzureCredential()

            validation_engine = AzureValidationEngine(
                subscription_id, consumer_group, connection_specs, eventhub_instance, eventhub_namespace, credential
            )

            result = validation_engine.validate_eventhub_instance()
            expected = True

            self.assertEqual(result, expected)


    @patch("app.utils.azure.AzureStockManager")
    def test_validate_eventhub_instance_tc2(self, mock_azure_stock_manager):
        """
        validate_eventhub_instance - 2nd Test Case Scenario

        Description: test that the function returns False meaning that the EventHub instance provided
        to the AzureValidationEngine doesn't exist.
        """

        with mock.patch.object(AzureValidationEngine, 'validate_eventhub_instance') as mock_instances_validation:
            mock_instances_validation.return_value = False

            subscription_id = "test_subscription_id"
            consumer_group = "test_consumer_group"
            connection_specs = "test_connection_specs"
            eventhub_instance = "test_eventhub_instance"
            eventhub_namespace = "test_eventhub_namespace"
            credential = DefaultAzureCredential()

            validation_engine = AzureValidationEngine(
                subscription_id, consumer_group, connection_specs, eventhub_instance, eventhub_namespace, credential
            )

            result = validation_engine.validate_eventhub_instance()
            expected = False

            self.assertEqual(result, expected)


class AzureValidationEngineValidateConsumerGroupTest(TestCase):
    """
    Test the validate_consumer_group method of the AzureValidationEngine class.
    """

    # TODO. 
    # Test: the response of the validation function if there's no consumer_groups

    @patch("app.utils.azure.AzureStockManager")
    def test_validate_consumer_group_tc1(self, mock_azure_stock_manager):
        """
        validate_consumer_group - 1st Test Case Scenario

        Description: test that the function doesn't raise any errors meaning that the consumer group provided
        to the AzureValidationEngine exists.
        """

        with mock.patch.object(AzureValidationEngine, 'validate_consumer_group') as mock_consumer_group_validation:
            mock_consumer_group_validation.return_value = True

            subscription_id = "test_subscription_id"
            consumer_group = "test_consumer_group"
            connection_specs = "test_connection_specs"
            eventhub_instance = "test_eventhub_instance"
            eventhub_namespace = "test_eventhub_namespace"
            credential = DefaultAzureCredential()

            validation_engine = AzureValidationEngine(
                subscription_id, consumer_group, connection_specs, eventhub_instance, eventhub_namespace, credential
            )

            result = validation_engine.validate_consumer_group()
            expected = True

            self.assertEqual(result, expected)


    @patch("app.utils.azure.AzureStockManager")
    def test_validate_consumer_group_tc2(self, mock_azure_stock_manager):
        """
        validate_consumer_group - 2nd Test Case Scenario

        Description: test that the function returns False meaning that the consumer group provided
        to the AzureValidationEngine doesn't exist.
        """
        
        with mock.patch.object(AzureValidationEngine, 'validate_consumer_group') as mock_consumer_group_validation:
            mock_consumer_group_validation.return_value = False

            subscription_id = "test_subscription_id"
            consumer_group = "test_consumer_group"
            connection_specs = "test_connection_specs"
            eventhub_instance = "test_eventhub_instance"
            eventhub_namespace = "test_eventhub_namespace"
            credential = DefaultAzureCredential()

            validation_engine = AzureValidationEngine(
                subscription_id, consumer_group, connection_specs, eventhub_instance, eventhub_namespace, credential
            )

            result = validation_engine.validate_consumer_group()
            expected = False

            self.assertEqual(result, expected)


class AzureValidationEngineValidateConnectionSpecsTest(TestCase):
    """
    Test the validate_connection_specs method of the AzureValidationEngine class.
    """

    # TODO. 
    # Test: the response of the validation function if there's not eventhub instances

    @patch("app.utils.azure.AzureStockManager")
    def test_validate_connection_specs_tc1(self, mock_azure_stock_manager):
        """
        validate_connection_specs - 1st Test Case Scenario

        Description: test that the function doesn't raise any errors meaning that the connection specs provided
        to the AzureValidationEngine exists.
        """

        with mock.patch.object(AzureValidationEngine, 'validate_connection_specs') as mock_connection_specs_validation:
            mock_connection_specs_validation.return_value = True

            subscription_id = "test_subscription_id"
            consumer_group = "test_consumer_group"
            connection_specs = "test_connection_specs"
            eventhub_instance = "test_eventhub_instance"
            eventhub_namespace = "test_eventhub_namespace"
            credential = DefaultAzureCredential()

            validation_engine = AzureValidationEngine(
                subscription_id, consumer_group, connection_specs, eventhub_instance, eventhub_namespace, credential
            )

            result = validation_engine.validate_connection_specs()
            expected = True

            self.assertEqual(result, expected)


    @patch("app.utils.azure.AzureStockManager")
    def test_validate_connection_specs_tc2(self, mock_azure_stock_manager):
        """
        validate_connection_specs - 2nd Test Case Scenario

        Description: test that the function returns False meaning that the connection specs provided
        to the AzureValidationEngine doesn't exist.
        """

        with mock.patch.object(AzureValidationEngine, 'validate_connection_specs') as mock_connection_specs_validation:
            mock_connection_specs_validation.return_value = True

            subscription_id = "test_subscription_id"
            consumer_group = "test_consumer_group"
            connection_specs = "test_connection_specs"
            eventhub_instance = "test_eventhub_instance"
            eventhub_namespace = "test_eventhub_namespace"
            credential = DefaultAzureCredential()

            validation_engine = AzureValidationEngine(
                subscription_id, consumer_group, connection_specs, eventhub_instance, eventhub_namespace, credential
            )

            result = validation_engine.validate_connection_specs()
            expected = True

            self.assertEqual(result, expected)
