from core.main import AWSAppManager

if __name__ == "__main__":
    aws_app_manager = AWSAppManager()
    app = aws_app_manager.create_app("sms_media_task")
    app.run()

