from flask import Flask, request, jsonify
app = Flask(__name__)
app.debug = True


@app.route('/process_csv', methods = ['POST'])
def process_csv():
	data = request.get_json()
	try:
		if not data:
			return jsonify({'error': 'No data available'}), 400
		else:
			return jsonify({'message': 'Data successfully loaded','data': data}), 200
	except:
		return jsonify({'error':'Internal Server Error'}), 500
	

if __name__ == "__main__":
	app.run()
