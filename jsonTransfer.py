import json


def jsontransform(items):
    data = json.dumps(items)
    jsonStr = json.loads(data)
    return jsonStr
