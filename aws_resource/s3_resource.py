import ntpath
from aws_resource.aws import AwsResource
from flask import jsonify, Response
from logging import getLogger

log = getLogger(__name__)


class S3Manager(AwsResource):
    """Class to manage operation of AWS S3 resource"""

    def __init__(self, access_key, secret_key, bucket_name):
        """Method to initialize the s3 resource"""
        super().__init__(access_key, secret_key)
        self.bucket = bucket_name
        self.resource = 's3'

    def is_bucket_exists(self, s3_resource):
        """Method to validate if bucket exists in s3 or not"""
        if not s3_resource.Bucket(self.bucket).creation_date:
            raise IOError

    def download_bucket_file(self, file_name):
        """Method to download file from aws s3 bucket"""
        try:
            s3_resource = self.aws_connect(self.resource)
            self.is_bucket_exists(s3_resource)
            base_file_name = ntpath.basename(file_name)
            file_obj = s3_resource.Bucket(self.bucket).Object(eval(file_name)).get()
            return Response(
                file_obj['Body'].read(),
                mimetype='text/plain',
                headers={"Content-Disposition": "attachment;filename={}".format(base_file_name)}
            )
        except IOError as err:
            return jsonify({"error": "Bucket '{}' does not exist in S3".format(self.bucket),
                            "status_code": 404})
        except Exception as err:
            log_statement = "Exception occurred while downloading file = '{filename}' " \
                            "from bucket = '{bucket}' | sf_error = {sf_error}".format(
                                filename=file_name, bucket=self.bucket, sf_error=err)
            log.error(log_statement)
            return jsonify({"error": log_statement, "status_code": 500})

    def get_bucket_files(self):
        """Method to get file list present in aws s3 bucket"""
        try:
            s3_resource = self.aws_connect(self.resource)
            self.is_bucket_exists(s3_resource)
            s3_objects = s3_resource.Bucket(self.bucket).objects.all()
            files_list = [x.key for x in s3_objects]
            return jsonify({"files": files_list}, 200)
        except IOError as err:
            return jsonify({"error": "Bucket '{}' does not exist in S3".format(self.bucket),
                            "status_code": 404})
        except Exception as err:
            log_statement = "Exception occurred while getting file list from bucket = '{bucket}' " \
                            "sf_error = {sf_error}".format(bucket=self.bucket, sf_error=err)
            return jsonify({"error": log_statement}, 500)
