import json

def render_json(data):
    return json.dumps(data)

def render_error(message):
    return json.dumps({"error": message})