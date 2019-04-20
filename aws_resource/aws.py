import boto3
from logging import getLogger
from _ast import Raise

log = getLogger(__name__)


class AwsResource():
    """Class to manage aws connection and resource"""

    def __init__(self, access_key, secret_key):
        self.aws_access_key = access_key
        self.aws_secret_key = secret_key

    def aws_connect(self, resource):
        """Method to connect to aws resource"""
        try:
            client = boto3.resource(
                resource,
                aws_access_key_id=self.aws_access_key,
                aws_secret_access_key=self.aws_secret_key
            )
            return client
        except Exception as err:
            log_statement = "Exception occurred while connecting to aws {resource} resource |" \
                            "sf_error = {sf_error}".format(resource=resource, sf_error=err)
            log.error(log_statement)
            raise Exception(err)
