import boto3

client =boto3.client('s3')

# response = client.create_bucket(
#     Bucket='ashish-demo-boto3-s3-bucket',
# )

response = client.get_bucket_acl(
    Bucket='ashish-demo-boto3-s3-bucket',
  
)

print(response)