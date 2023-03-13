

import json
import asyncio
from azure.eventhub import EventData
from azure.eventhub.aio import EventHubProducerClient
# from azure.identity import DefaultAzureCredential


EVENTHUB_NAME = 'jnisa-eventhub-instance'
EVENTHUB_FULLY_QUALIFIED_NAMESPACE = "jnisa-eventhub-namespace"
CONNECTION_SPECS = 'Endpoint=sb://jnisa-eventhub-namespace.servicebus.windows.net/;SharedAccessKeyName=RootManageSharedAccessKey;SharedAccessKey=qpM2Ko5Rb4vHjI1HoZNB5NG5xb+MrP/Jo+AEhKQr6Ko='

# credential = DefaultAzureCredential()

msgs_lst = [
    {'id': 1, 'drinkID': 'Martini Rosso', 'price': '14.99GBP'},
    {'id': 2, 'drinkID': 'Gin Tonic', 'price': '12.99GBP'},
    {'id': 3, 'drinkID': 'Bottle of Water', 'price': '4.99GBP'}
]

async def run():
    # Create a producer client to send messages to the event hub.
    # Specify a credential that has correct role assigned to access
    # event hubs namespace and the event hub name.
    producer = EventHubProducerClient.from_connection_string(
        conn_str=CONNECTION_SPECS, 
        eventhub_name=EVENTHUB_NAME
    )

    async with producer:
        # Create a batch.
        event_data_batch = await producer.create_batch()

        # Add events to the batch.
        for msg in msgs_lst:
            event_data_batch.add(EventData(json.dumps(msg)))

        # Send the batch of events to the event hub.
        await producer.send_batch(event_data_batch)

        # Close credential when no longer needed.
        # await credential.close()

asyncio.run(run())