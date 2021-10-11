import jsons

def json2object(json, klass):
    """Convert a json/dict to an object of type klass.

    Args:
        json: the json or dict to be converted
        klass: The type destination of the conversion
    Returns:
        object of type klass
    """
    return jsons.load(json, klass)

def object2json(obj):
    """Convert an object to json/dict.

    Args:
        obj: the object to be converted
    Returns:
        the obj converted to json/dict
    """
    return jsons.dump(obj)