

from unittest import TestCase
from unittest.mock import Mock

from app.utils.azure import AzureValidationEngine


class AzureValidationEngineInitTest(TestCase):
    """
    This class is used to test the __init__ method of the AzureValidationEngine class.
    """

    def test__init__tc1(self):
        """
        __init__ - 1st Test Case Scenario

        Description: test that the function doesn't raise any errors when a valid connection string
        and eventhub instance are provided.
        """
        result = AzureValidationEngine(
            subscription_id = "test_subscription_id",
            consumer_group = "test_consumer_group",
            connection_specs = "test_connection_specs",
            eventhub_instance = "test_eventhub_instance",
            eventhub_namespace = "test_eventhub_namespace"
        )

        self.assertIsInstance(result, AzureValidationEngine)

        self.assertEqual(result.subscription_id, "test_subscription_id")
        self.assertEqual(result.consumer_group, "test_consumer_group")
        self.assertEqual(result.connection_specs, "test_connection_specs")
        self.assertEqual(result.eventhub_instance, "test_eventhub_instance")
        self.assertEqual(result.eventhub_namespace, "test_eventhub_namespace")

    