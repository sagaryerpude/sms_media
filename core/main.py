from flask import Flask
from logging import getLogger

from aws_resource.api import aws_api

log = getLogger(__name__)


class AWSAppManager:
    """Class to create flask application for AWS Manager"""

    def create_app(self, package_name=__name__):
        """Method to create the flask app"""
        # Register the flask app
        app = Flask(package_name)
        # Register all the blueprints
        self.register_blueprints(app)
        return app

    def register_blueprints(self, app):
        """Method to register all routing blueprints to app"""
        app.register_blueprint(aws_api)

