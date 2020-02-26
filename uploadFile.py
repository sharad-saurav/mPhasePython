#Rule 23 - Check for Reference link for each entity and Ref URLs should not be there in Text.
def import_csvfile(file):
    import pandas as pd
    import pymongo
    import json
    import os
    from datetime import datetime
    import dateutil.parser as parser

    mng_client = pymongo.MongoClient('mongodb://mPhase:mphase@cluster0-shard-00-00-2b0ur.mongodb.net:27017,cluster0-shard-00-01-2b0ur.mongodb.net:27017,cluster0-shard-00-02-2b0ur.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true&w=majority')
    mng_db = mng_client['mPhase']
    collection_name = 'stock'
    collection_name1 = 'stockData'
    db_cm = mng_db[collection_name]
    db_cm1 = mng_db[collection_name1]
    data = pd.read_csv(file)
    data_json = json.loads(data.to_json(orient='records'))
    print(data_json)
    stockInfo = '{"id": 500285, "stockName": "Spice Jet"}'
    stockInfo = json.loads(stockInfo)
    print(stockInfo)

     # convert into JSON:
    for item in data_json:
        item['date'] = item.pop('Date')

        item['date'] = datetime.strptime(item['date'], "%d-%B-%Y")
        item['date'] = item['date'].replace(tzinfo=None)
        item['openPrice'] = item.pop('Open Price')
        item['highPrice'] = item.pop('High Price')
        item['lowPrice'] = item.pop('Low Price')
        item['closePrice'] = item.pop('Close Price')
        item['wap'] = item.pop('WAP')
        item['noOfShares'] = item.pop('No.of Shares')
        item['noOfTrades'] = item.pop('No. of Trades')
        item['totalTurnOver'] = item.pop('Total Turnover (Rs.)')
        item['deliverableQuantities'] = item.pop('Deliverable Quantity')
        item['quantitiesToTrade'] = item.pop('% Deli. Qty to Traded Qty')
        item['spreadHighLow'] = item.pop('Spread High-Low')
        item['spreadOpenClose'] = item.pop('Spread Close-Open')
        item['id'] = 500285
    db_cm.remove()
    db_cm.insert(data_json)
    db_cm1.remove()
    db_cm1.insert(stockInfo)