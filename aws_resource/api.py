from aws_resource.s3_resource import S3Manager
from core.config import (AWS_ACCESS_KEY, AWS_SECRET_KEY,
                         AWS_S3_BUCKET, credentials_required)
from flask import Blueprint, request


aws_api = Blueprint('aws', __name__, url_prefix='/v1/aws')


@aws_api.route('/s3/files/lists', methods=['GET'])
@credentials_required
def call_get_bucket_files():
    """Method to call get_bucket_files from s3_resource"""
    s3_manager_obj = S3Manager(AWS_ACCESS_KEY, AWS_SECRET_KEY, AWS_S3_BUCKET)
    response = s3_manager_obj.get_bucket_files()
    return response


@aws_api.route('/s3/files/download', methods=['GET'])
@credentials_required
def call_download_bucket_file():
    """Method to call download_bucket_file from s3_resource"""
    file_name = request.args.get('key', None)
    s3_manager_obj = S3Manager(AWS_ACCESS_KEY, AWS_SECRET_KEY, AWS_S3_BUCKET)
    response = s3_manager_obj.download_bucket_file(file_name)
    return response
