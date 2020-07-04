from ServiceCore.Exceptions.CustomerError import CustomerError


class Error(Exception):
    """Base class for exceptions in this module."""
    pass


class CustomerException(Error):
    """Exception raised on a customer input error.

    Attributes:
        expression -- input expression in which the error occurred
        message -- explanation of the error
    """

    def __init__(self, error: CustomerError, message: str):
        self.error = error
        self.message = message

    def to_json_response(self):
        json_response = {'errorMessage': self.message, 'errorType': self.error.name}

        return json_response
