#Rule 23 - Check for Reference link for each entity and Ref URLs should not be there in Text.
def import_csvfile(file):
	import pandas as pd
	import pymongo
	import json
	import os
 
	mng_client = pymongo.MongoClient('mongodb://mPhase:mphase@cluster0-shard-00-00-2b0ur.mongodb.net:27017,cluster0-shard-00-01-2b0ur.mongodb.net:27017,cluster0-shard-00-02-2b0ur.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true&w=majority')
	print(mng_client)
	mng_db = mng_client['mPhase']
	print(mng_db)
	collection_name = 'stock'
	db_cm = mng_db[collection_name]
	data = pd.read_csv(file)
	data_json = json.loads(data.to_json(orient='records'))
	# data_json = json.dumps(data_json)

	for item in data_json:
		print(item)
		item['date'] = item.pop('Date')
		item['open_price'] = item.pop('Open Price')
		item['high_price'] = item.pop('High Price')
		item['low_price'] = item.pop('Low Price')
		item['close_price'] = item.pop('Close Price')
		item['wap'] = item.pop('WAP')
		item['no_of_shares'] = item.pop('No.of Shares')
		item['no_of_trades'] = item.pop('No. of Trades')
		item['total_turn_over'] = item.pop('Total Turnover (Rs.)')
		item['deliverable_quantities'] = item.pop('Deliverable Quantity')
		item['quantities_to_trade'] = item.pop('% Deli. Qty to Traded Qty')
		item['speed_high_low'] = item.pop('Spread High-Low')
		item['spread_close_open'] = item.pop('Spread Close-Open')

	db_cm.remove()
	db_cm.insert(data_json)