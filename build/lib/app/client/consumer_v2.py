


import asyncio

from azure.eventhub.aio import EventHubConsumerClient
from azure.identity.aio import DefaultAzureCredential


# EventHub specific
EVENT_HUB_FULLY_QUALIFIED_NAMESPACE = "jnisa-eventhub-namespace"
EVENT_HUB_NAME = "jnisa-eventhub-instance"
CONNECTION_SPECS = 'Endpoint=sb://jnisa-eventhub-namespace.servicebus.windows.net/;SharedAccessKeyName=RootManageSharedAccessKey;SharedAccessKey=qpM2Ko5Rb4vHjI1HoZNB5NG5xb+MrP/Jo+AEhKQr6Ko='

credential = DefaultAzureCredential()

async def on_event(partition_context, event):
    # Print the event data.
    print(
        'Received the event: "{}" from the partition with ID: "{}"'.format(
            event.body_as_str(encoding="UTF-8"), partition_context.partition_id
        )
    )

    # Update the checkpoint so that the program doesn't read the events
    # that it has already read when you run it next time.
    await partition_context.update_checkpoint(event)


async def main():
    # Create a consumer client for the event hub.
    client = EventHubConsumerClient.from_connection_string(
        conn_str = CONNECTION_SPECS,
        consumer_group = '$Default',
        eventhub_name = EVENT_HUB_NAME
    )

    async with client:
        # Call the receive method. Read from the beginning of the partition
        # (starting_position: "-1")
        await client.receive(on_event=on_event, starting_position="-1")

    # Close credential when no longer needed.
    await credential.close()

if __name__ == "__main__":
    # Run the main method.
    asyncio.run(main())