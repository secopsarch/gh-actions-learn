from flask import Flask, jsonify
import time
import sys

app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello():
    return jsonify({
        'message': 'Hello from Python API!',
        'status': 'success',
        'date': 'March 10, 2025'
    })
if __name__ == '__main__':
    # Wait for 30 seconds before exiting
    time.sleep(30)
    print("Exiting after 30 seconds...")
    sys.exit(0)
    
if __name__ == '__main__':
    app.run(host='localhost', port=4949, debug=True)