import json


def lambda_handler(event, context):
    print('event: ', event)
    records = event.get('Records')
    if len(records) > 0:
        print('records: ', records)
        record = records[0]
        print("record: ", record)

    return event
