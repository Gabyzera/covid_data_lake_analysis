import os
import boto3
import dotenv

dotenv.load_dotenv()

REGION_NAME = os.environ.get("REGION_NAME")
BUCKET_NAME = os.environ.get("BUCKET_NAME")
DATABASE_NAME = os.environ.get("DATABASE_NAME")
AWS_ACCESS_KEY = os.environ.get("AWS_ACCESS_KEY")
AWS_SECRET_ACCESS_KEY = os.environ.get("AWS_SECRET_ACCESS_KEY")
BUCKET_KEY_HOSPITAL_BEDS = os.environ.get("BUCKET_KEY_HOSPITAL_BEDS")
BUCKET_KEY_CASES_AND_DEATHS = os.environ.get("BUCKET_KEY_CASES_AND_DEATHS")
BUCKET_KEY_GLOBAL_DEATHS = os.environ.get("BUCKET_KEY_GLOBAL_DEATHS")
BUCKET_KEYS_VACCINATED_PER_HUNDRED = os.environ.get("BUCKET_KEYS_VACCINATED_PER_HUNDRED")
BUCKET_KEY_DOSES_PFIZER = os.environ.get("BUCKET_KEY_DOSES_PFIZER")

session = boto3.Session(
    region_name=REGION_NAME,
    aws_access_key_id=AWS_ACCESS_KEY,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY
)