# list-dynamodb-tags

Simple script to check if the given tags are present in dynamodb tables

## example

```shell
git clone https://github.com/ceb10n/list-dynamodb-tags.git
cd list-dynamodb-tags
pip install -r requirements.txt

python app.py \
    --key YOUR_KEY \
    --secret YOUR_SECRET_KEY \
    --region YOUR_TABLES_REGION \
    --role arn:aws:iam::account:role/YourRole \
    --tags tag1,tag2,tag3 \
    --tables table1,table2,table3

Table table1 is missing tag tag1
Table table1 is missing tag tag2
Table table2 is missing tag tag3
```

## help

```shell
python app.py --help
usage: app.py [-h] --key KEY --secret SECRET --role ROLE --tables TABLES
              --tags TAGS --region REGION

optional arguments:
  -h, --help       show this help message and exit
  --key KEY        Account's Access Key
  --secret SECRET  Account's Secret Access Key
  --role ROLE      Account's Role
  --tables TABLES  List of table names separeted by comma
  --tags TAGS      List of tag names separeted by comma
  --region REGION  Account's Role
```
