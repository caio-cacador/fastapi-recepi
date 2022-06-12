class ClientNotFoundError(Exception):
    """Raised when the client was not found"""

    def __init__(self, client_id: str):
        super().__init__(f'Client "{client_id}" not found')


class ClientCanNotBeUpdatedError(Exception):
    """Raised when try update an inactive client"""

    def __init__(self, client_id: str, message: str="Client can not be updated"):
        self.client_id = client_id
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f'Client "{self.client_id}" -> {self.message}'


class ClientStatusError(Exception):
    """Raised when trying to inactive a inactived client or the opposit"""

    def __init__(self, client_id: str, message: str="Client is already active or inactive"):
        self.client_id = client_id
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f'Client "{self.client_id}" -> {self.message}'
