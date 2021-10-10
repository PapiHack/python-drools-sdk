import jsons

def json2object(json, klass):
    return jsons.load(json, klass)

def object2json(obj):
    return jsons.dump(obj)