import sys
import flask
from flask import Flask,g
import flask_restful

app = Flask(__name__)
api = flask_restful.Api(app)

class HelloWorld(flask_restful.Resource):
    def get(self):
        return {'hello': 'world'}

api.add_resource(HelloWorld,'/')

if __name__ == '__main__':
    app.run(host='0.0.0.0')

