from .abstract_command import AbstractCommand
from ..utils.data_store import DataStore

class InsertObjectCommand(AbstractCommand):

    def __init__(self, **kwargs) -> None:
        self.object = kwargs.get('object', None)
        self.disconnected = kwargs.get('disconnected', False)
        self.__dict__['out-identifier'] = kwargs.get('out_identifier', self.object.__class__.__name__)
        self.__dict__['return-object'] = kwargs.get('return_object', True)
        self.__dict__['entry-point'] = kwargs.get('entry_point', 'DEFAULT')
        DataStore.add_item(self.__dict__['out-identifier'], self.object.__class__.__name__)
        if self.object is not None:
            object_name = self.object.__class__.__name__
            self.object = { object_name: self.object, }

    def initialize(self) -> dict:
        return { 'insert': self, }

    def __str__(self) -> str:
        return ''