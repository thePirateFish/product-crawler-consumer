import base64, json

def remove_metadata(jsonObj):
    d = dict(jsonObj)
    del d['metadata']
    return d

def get_data(event):
    return json.loads(base64.b64decode(event['data']).decode('utf-8'))

def get_type(data):
    if 'metadata' in data:
        metadata = data['metadata']
        if 'type' in metadata:
            return metadata['type']