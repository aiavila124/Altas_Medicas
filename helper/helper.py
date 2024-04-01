import json

def get_data(string):
    try:
        return json.loads(string)
    except Exception as e:
        return str(e)