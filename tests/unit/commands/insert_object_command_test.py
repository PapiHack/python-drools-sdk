import unittest
from ..data import *

from src.commands.insert_object_command import InsertObjectCommand

class InsertObjectCommandTest(unittest.TestCase):

    def test_instance_creation(self):
        insert_command = InsertObjectCommand(object=person, out_identifier="john").initialize()
        self.assertIsInstance(insert_command, dict)
