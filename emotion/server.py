from flask import jsonify
from flask import Flask
from flask import request
from flask import make_response
from flask_cors import CORS

from tornado.wsgi import WSGIContainer
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop

from model import annotate

app = Flask(__name__)
CORS(app)

@app.route('/emotion')
def hello_world():
	return 'model'

@app.route('/emotion/annotate',methods=["POST"])
def api():
    list_of_dicts = request.json["messages"]
    output = annotate(list_of_dicts)
    return make_response(jsonify(output), 200)

@app.route('/emotion/annotate',methods=["GET","POST"])
def return_status():
    return make_response(jsonify({'status' : 'Up and running'}), 200)

if __name__ == '__main__':
    http_server = HTTPServer(WSGIContainer(app))
    http_server.listen(6015)
    IOLoop.instance().start()