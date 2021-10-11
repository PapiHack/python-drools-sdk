from ..utils import endpoints
from ..utils.make_request import MakeRequest
from ..exceptions.drools_exception import DroolsException
from ..utils.data_store import DataStore

class Drools:
    KIE_SERVER_USERNAME = None
    KIE_SERVER_PASSWORD = None
    KIE_SERVER_ROOT_URL = None
    KIE_SESSION_NAME = None
    KIE_SERVER_CONTAINER_ID = None
    KIE_SERVER_CONTAINER_PACKAGE = None
    commands = []

    @classmethod
    def execute_commands(cls):
        cls.commands.append({'fire-all-rules': ''})
        data = { 'lookup': cls.KIE_SESSION_NAME, 'commands': cls.commands, }
        url = '{}{}{}'.format(cls.KIE_SERVER_ROOT_URL, endpoints.KIE_SESSION_ASSETS, cls.KIE_SERVER_CONTAINER_ID)
        response = MakeRequest.post(url, data, auth=(cls.KIE_SERVER_USERNAME, cls.KIE_SERVER_PASSWORD))
        return cls.extract_data_from_response(response)

    @classmethod
    def extract_data_from_response(cls, response):
        json_response = response.json()
        try:
            data = {}
            results = json_response['result']['execution-results']['results']
            for result in results:
                if 'key' in result:
                    identifier = result['key']
                    if identifier in DataStore.store:
                        object_class_name = DataStore.store[identifier]
                        complete_object_class_name = '{}.{}'.format(cls.KIE_SERVER_CONTAINER_PACKAGE, object_class_name)
                        if len(identifier) > 0 and identifier.find('__') > 0:
                            _id = identifier.split('__')[0]
                            if _id not in data:
                                data[_id] = []
                            data[_id].append(result['value'][complete_object_class_name])
                        else:
                            data[identifier] = result['value'][complete_object_class_name]
            return data
        except TypeError:
            message = 'An error has occurred 😕 !!!'
            if 'msg' in json_response:
                message = json_response['msg']
            raise DroolsException(message=message, code=-99)

    @classmethod
    def add_command(cls, command):
        if type(command) is list:
            cls.commands.extend(command)
        else:
            cls.commands.append(command)

    @classmethod
    def reset_commands(cls):
        """
        Reset Drools.commands and remove all commands in it.
        """
        cls.commands = []