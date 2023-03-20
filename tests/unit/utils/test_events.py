

from app.utils.events import on_event

import asyncio
from io import StringIO
from unittest.mock import MagicMock
from unittest import TestCase, IsolatedAsyncioTestCase


class OnEventTest(TestCase):
    """
    Test the on_event decorator that is used to keep track on the messages received and their
    respective location (i.e. EventHub partition).
    """

    async def test_on_event_tc1(self):
        """
        on_event - 1st Test Case Scenario

        Description: Validate that the on_event decorator is able to provide the correct output
        when the function receives a message and partition ID. 
        """

        event = MagicMock()
        partition_context = MagicMock()

        event.body_as_str.return_value = "test-messsage-1"
        partition_context.partition_id = "partition-1"

        output = StringIO()
        await on_event(partition_context, event, output=output)

        expected = 'Received the event: "test-messsage-1" from the partition with ID: "partition-1"'
        self.assertEqual(output.getvalue(), expected)

        
    async def test_on_event_tc2(self):
        """
        on_event - 2nd Test Case Scenario

        Description: Guarantee that the function updates the checkpoint by providing a mock partition
        context and event objects. 
        """

        event = MagicMock()
        partition_context = MagicMock()

        await on_event(partition_context, event)

        partition_context.update_checkpoint.assert_called_with(event)


    async def test_on_event_tc3(self):
        """
        on_event - 3rd Test Case Scenario

        Description: Test if the function handles enconding errors by providing a mock event object 
        with a body that cannot be decoded using UTF-8.
        TODO. assert that the printed output contains an error message indicating the type and message
        of the exception. 
        """

        event = MagicMock()
        partition_context = MagicMock()

        event.body_as_str.side_effect = UnicodeDecodeError("utf-8", b"test", 0, 1, "test")

        with self.assertRaises(UnicodeDecodeError):
                    await on_event(partition_context, event)        


    async def test_on_event_tc4(self):
        """
        on_event - 4th Test Case Scenario

        Description: Test how the function handles exceptions by providing a mock partition and event
        objects that can cause an Exception. 
        """

        event = MagicMock()
        partition_context = MagicMock()

        partition_context.update_checkpoint.side_effect = Exception("Test exception")

        with self.assertRaises(Exception):
            await on_event(partition_context, event)