class DroolsException(Exception):
    def __init__(self, **kwargs) -> None:
        self.message = kwargs.get('message', None)
        self.code = kwargs.get('code', 0)

    def __str__(self) -> str:
        return '[MESSAGE] => {} || [CODE] => {}'.format(self.message, self.code)