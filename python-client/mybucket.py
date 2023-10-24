import boto3
from botocore.config import Config

endpoint_url = 'http://dvcs3.crc.nd.edu:4566'

client = boto3.client( 's3', 
                        endpoint_url=endpoint_url,
                        aws_access_key_id='',
                        aws_secret_access_key='',
                        aws_session_token=''
                     )

print(client.create_bucket(Bucket='test-bucket'))