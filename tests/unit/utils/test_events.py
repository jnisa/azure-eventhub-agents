

from app.utils.events import on_event

import asyncio
import unittest
import logging
from io import StringIO
from unittest.mock import MagicMock, patch



class OnEventTest(unittest.TestCase):
    """
    Test the on_event decorator that is used to keep track on the messages received and their
    respective location (i.e. EventHub partition).
    """

    @patch("app.utils.events.EVENT_LOGGER")
    async def test_on_event_tc1(self, mock_logger):
        """
        on_event - 1st Test Case Scenario

        Description: Validate that the on_event decorator is able to provide the correct output
        when the function receives a message and partition ID. 
        """

        event = MagicMock()
        partition_context = MagicMock()

        event.body_as_str.return_value = "test-messsage-1"
        partition_context.partition_id = "partition-1"

        await on_event(partition_context, event)

        expected = 'Received the event: "test-messsage-1" from the partition with ID: "partition-"'
        mock_logger.assert_called_with(expected)
        mock_logger.assert_called_once()

        
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

    if __name__ == '__main__':
        asyncio.run(unittest.main())