import pandas as pd

def filter_table_by_banking_sector():
	try:
		df = pd.read_csv('wig20.csv')
		filtered_table = df[df['Sector'] == 'Banking']
		return filtered_table
	except FileNotFoundError as e:
		print(e)
		return pd.DataFrame([])

def adjust_table():
	filtered_table = filter_table_by_banking_sector()
	if filtered_table.empty:
		return filtered_table
	else:
		filtered_table['MarketCap/Price'] = filtered_table['Market Cap (in billions PLN)'] / filtered_table['Price (PLN)']
		adjusted_table = filtered_table[['Company Name', 'MarketCap/Price']]
		return adjusted_table
	
def convert_to_json():
	df = adjust_table()
	if df.empty:
		return []	
	else:
		json_table = df.to_json(orient='records')
		return json_table
