import os
import json
from coinbase.wallet.client import Client
import boto3

def main(event, context):
    COINBASE_API_KEY = os.environ['COINBASE_API_KEY']
    COINBASE_API_SECRET = os.environ['COINBASE_API_SECRET']
    DYNAMODB_TABLE = os.environ['bitcoin_data_table']

    dynamodb_client = boto3.client('dynamodb')
    sns_client = boto3.client('sns')
    
    # Initialises coinbase client
    client = Client(
        COINBASE_API_KEY, 
        COINBASE_API_SECRET,
        api_version='2017-12-30'
    )
    
    btc_buy_price = client.get_buy_price(currency_pair='BTC-GBP')

    # Retrieves current time
    time = client.get_time()

    # Puts the item in the DynamoDB table
    data_put = dynamodb_client.put_item(
        TableName=DYNAMODB_TABLE,
        Item={
            'timestamp': {'S': time.iso },
            'btc_buy_price': {'S': btc_buy_price.amount }
        }
    )

    return {
        "statusCode": 200
    }

if __name__ == "__main__":
    main('', '')