import base64, json
from consumer.processor import process_event

def receive_scrapy_item(event, context):
    print("""This Function was triggered by messageId {} published at {}
    """.format(context.event_id, context.timestamp))

    process_event(event)



