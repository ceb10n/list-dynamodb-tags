import argparse
import boto3


parser = argparse.ArgumentParser()
parser.add_argument(
    "--key",
    required=True,
    help="Account's Access Key")
parser.add_argument(
    "--secret",
    required=True,
    help="Account's Secret Access Key")
parser.add_argument(
    "--role",
    required=True,
    help="Account's Role")
parser.add_argument(
    "--tables",
    required=True,
    help="List of table names separeted by comma")
parser.add_argument(
    "--tags",
    required=True,
    help="List of tag names separeted by comma")
parser.add_argument(
    "--region",
    default="sa-east-1",
    required=True,
    help="Account's Role")


args = parser.parse_args()

account_info = {
    'key': args.key,
    'secret': args.secret,
    'role': args.role,
    'region': args.region
}

tables = []

for table_name in args.tables.split(','):
    tables.append(table_name)

tags = []

for tag_name in args.tags.split(','):
    tags.append(tag_name)


def dynamo_client(acc_info):
    role = assume_role(acc_info)

    return boto3.client(
        'dynamodb',
        region_name=acc_info['region'],
        aws_access_key_id=role['Credentials']['AccessKeyId'],
        aws_secret_access_key=role['Credentials']['SecretAccessKey'],
        aws_session_token=role['Credentials']['SessionToken'])


def assume_role(acc_info):
    sts = boto3.client(
        'sts',
        region_name=acc_info['region'],
        aws_access_key_id=acc_info['key'],
        aws_secret_access_key=acc_info['secret'])

    return sts.assume_role(
        RoleArn=acc_info['role'],
        RoleSessionName='assumeRole',
        DurationSeconds=3600)


if __name__ == '__main__':
    dynamodb = dynamo_client(account_info)

    for table in tables:
        described_table = dynamodb.describe_table(TableName=table)
        tags_of_resource = dynamodb.list_tags_of_resource(
            ResourceArn=described_table['Table']['TableArn'])

        for tag in tags:
            has_tag = False
            for resource_tag in tags_of_resource['Tags']:
                if resource_tag['Key'] == tag:
                    has_tag = True
                    break

            if not has_tag:
                print(f'Table {table} is missing tag {tag}')
