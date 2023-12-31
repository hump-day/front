from storages.backends.s3boto3 import S3Boto3Storage, S3StaticStorage


class MediaStorage(S3Boto3Storage):
    bucket_name = 'hump-bucket'
    location = 'media'


class StaticStorage(S3Boto3Storage)  :
    bucket_name = 'hump-bucket'
    location = 'static'
