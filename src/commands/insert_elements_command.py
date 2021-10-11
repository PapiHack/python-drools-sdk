from .abstract_command import AbstractCommand
from .insert_object_command import InsertObjectCommand

class InsertElementsCommand(AbstractCommand):

    def __init__(self, **kwargs) -> None:
        self.objects = kwargs.get('objects', None)
        self.out_identifier = kwargs.get('out_identifier', None)

    def initialize(self):
        object_id = 0
        inserts = []
        if self.objects is not None and len(self.objects) > 0:
            if self.out_identifier is not None and len(self.out_identifier) > 0 :
                for obj in self.objects:
                    out_identifier = '{}__{}'.format(self.out_identifier, object_id)
                    insert_object_command = InsertObjectCommand(object=obj, out_identifier=out_identifier).initialize()
                    inserts.append(insert_object_command)
                    object_id += 1
        return inserts