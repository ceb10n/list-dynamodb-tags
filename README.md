# list-dynamodb-tags

Simple script to check if the given tags are present in dynamodb tables

## example

```shell
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
