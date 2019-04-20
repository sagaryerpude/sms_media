# SMS Media Assignment (AWS S3 Operations Using Flask)

## Configuration
1. Create python3 virtual environment.
```shell
virtualenv -p python3 smsenv
source smsenv/bin/activate
```

2. Install Dependencies from requirement.txt
```shell
pip install -r requirements.txt
```

3. Initialize below environment variable
```shell
export AWS_ACCESS_KEY=<aws_access_key_id>
export AWS_SECRET_KEY=<aws_access_secret_key>
export AWS_S3_BUCKET=<aws_s3_bucket_name>
```

4. Set PYTHONPATH
```shell
export PYTHONPATH=$PYTHONPATH:<location of your python application folder>
```

5. Run flask application in cmd
```Shell
python app.py
```

6. Enter below url's in browser to see results:
```shell
a. Listing files from s3 bucket:
URL: /v1/aws/s3/files/lists

b. Download file from s3 bucket:
URL: /v1/aws/s3/files/download?key=<file_name>
```

