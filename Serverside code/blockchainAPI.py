from hashlib import sha1 # Could expriment with different algorithms
import json
from datetime import datetime
from flask import Flask, request, jsonify

app = Flask(__name__)
chain = []
split = []

@app.route('/data', methods=['POST'])
def process_json():
	content_type = request.headers.get('Content-Type')
	if (content_type == 'application/block'):
		byteData = request.get_data()
		decodeData = byteData.decode('UTF-8')
		print("\n\nDecode data")
		print(decodeData)
		returnHash = sha1(decodeData.encode())
		chain.append(returnHash.hexdigest() + ":" + decodeData)
		return (returnHash.hexdigest())
	else:
		return 'Content-Type not supported!'


if __name__ == '__main__':
	app.run(host= '0.0.0.0', port=3800,debug=True)

