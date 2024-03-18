import os
import boto3
import dotenv

dotenv.load_dotenv()

REGION_NAME = os.environ.get("REGION_NAME")
BUCKET_NAME = os.environ.get("BUCKET_NAME")
DATABASE_NAME = os.environ.get("DATABASE_NAME")
AWS_ACCESS_KEY = os.environ.get("AWS_ACCESS_KEY")
AWS_SECRET_ACCESS_KEY = os.environ.get("AWS_SECRET_ACCESS_KEY")

session = boto3.Session(
    region_name=REGION_NAME,
    aws_access_key_id=AWS_ACCESS_KEY,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
)