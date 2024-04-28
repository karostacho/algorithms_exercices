from flask import Flask, jsonify
from zadnie_csv import convert_to_json
app = Flask(__name__)
app.debug = True


@app.route('/process_csv', methods = ['POST'])
def process_csv():
	data = convert_to_json()
	try:
		if not data:
			return jsonify({'error': 'No data available'}), 400
		else:
			return jsonify({'message': 'Data successfully loaded', 'data': data}), 201
	except:
		return jsonify({'error':'Internal Server Error'}), 500
	

if __name__ == "__main__":
	app.run()
