from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello():
    return jsonify({
        'message': 'Hello from Python API!',
        'status': 'success',
        'date': 'March 10, 2025'
    })

if __name__ == '__main__':
    app.run(host='localhost', port=4949, debug=True)