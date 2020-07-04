from flask import json
import requests

from ServiceCore.Exceptions.CommonExceptions import CustomerException
from ServiceCore.Exceptions.CustomerError import CustomerError


class UserRepositoryInterface:

    def get_user_info(self, parameters: dict) -> requests.Response:
        """Overrides InformalParserInterface.load_data_source()"""
        pass


class UserRepository(UserRepositoryInterface):

    # Need to address another service and asks for the current games
    def get_user_info(self, parameters):
        try:
            url = "http://127.0.0.1:5001/getUser"
            self.validate_get_user_request(parameters)
            response = requests.post(url, data=parameters)

            return json.dumps(response.json())

        except CustomerException as e:
            return json.dumps(e.to_json_response())

    # Need to create a validator - for now it's good enough

    @staticmethod
    def validate_get_user_request(request_parameters: dict):
        if "id" not in request_parameters:
            raise CustomerException(CustomerError.InvalidRequest, "Can't get user without id")

        pass
