from flask import Flask, request, jsonify

app = Flask(__name__)
split = []


@app.route('/data', methods=['POST'])
def process_json():
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        json = request.json
        storage = open("output.txt", "a")
        storage.write(str(json) + "\n")
        storage.close()
        return ("{\"code\":\"success\"}")
        
    else:
        return 'Content-Type not supported!'
        
        
if __name__ == '__main__':
    app.run(host= '0.0.0.0', port=3800,debug=True)

