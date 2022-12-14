from flask import jsonify
from flask import Flask
from flask import request
from flask import make_response
from flask_cors import CORS

from tornado.wsgi import WSGIContainer
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop

from annotate import annotate

app = Flask(__name__)
CORS(app)

@app.route('/change_point_detection')
def hello_world():
	return 'model'

@app.route('/change_point_detection/annotate', methods=["POST"])
def api():
    try:
        message_file = open(request.json["message_file"])
    except:
        output = {}
    else:
        output = annotate(message_file)
    return make_response(jsonify(output), 200)

@app.route('/change_point_detection/annotate',methods=["GET","POST"])
def return_status():
    return make_response(jsonify({'status' : 'Up and running'}), 200)

if __name__ == '__main__':
    http_server = HTTPServer(WSGIContainer(app))
    http_server.listen(6021)
    IOLoop.instance().start()
