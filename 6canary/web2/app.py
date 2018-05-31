from flask import Flask, jsonify


app = Flask(__name__)


@app.route('/demo/api/v1.0/servername/<int:no>', methods = ['GET'])
def get_sname(no):
    return jsonify( { 'server-name': "demo-2", "no":no} )

if __name__ == '__main__':
    app.run()
