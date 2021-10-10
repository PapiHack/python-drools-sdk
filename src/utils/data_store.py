class DataStore:
    store = {}

    @classmethod
    def add_item(cls, key, value):
        cls.store[key] = value

    @classmethod
    def remove_item(cls, key):
        del cls.store[key]

    @classmethod
    def reset(cls):
        cls.store = {}