class Config:

    def __init__(self, **kwargs) -> None:
        self.kie_server_username = kwargs.get('kie_server_username')
        self.kie_server_password = kwargs.get('kie_server_password')
        self.kie_server_root_url = kwargs.get('kie_server_root_url')
        self.kie_session = kwargs.get('kie_session', None)
        self.kie_server_container_id = kwargs.get('kie_server_container_id')
        self.kie_server_container_package = kwargs.get('kie_server_container_package')