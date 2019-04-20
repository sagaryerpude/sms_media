from functools import wraps
from flask import jsonify
from os import getenv

AWS_ACCESS_KEY = getenv('AWS_ACCESS_KEY')
AWS_SECRET_KEY = getenv('AWS_SECRET_KEY')
AWS_S3_BUCKET = getenv('AWS_S3_BUCKET')


def credentials_required(f):
    """Decorator to check aws credentials has configured or not"""
    @wraps(f)
    def wrapper(*args, **kwargs):
        if all([AWS_ACCESS_KEY, AWS_SECRET_KEY, AWS_S3_BUCKET]):
            return f(*args, **kwargs)
        else:
            return jsonify({"error": "AWS credential hasn't been configured",
                            "status_code": 403})
    return wrapper
