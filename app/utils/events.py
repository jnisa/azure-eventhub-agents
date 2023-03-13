

async def on_event(partition_context, event):
    """
    This method can be seen as the action performed on each and every message obtained 
    from EventHub. 
    It is used to keep track not only on the content of the messages received but also
    on which parity they were received from.

    :param partition_context: the partition context
    :param event: the event
    :return: logs indicating the messages from each position of each partition. 
    """

    # Define the output
    print(
        'Received the event: "{}" from the partition with ID: "{}"'.format(
            event.body_as_str(encoding="UTF-8"), partition_context.partition_id
        )
    )

    # Avoid reading the same message more than once.
    await partition_context.update_checkpoint(event)
