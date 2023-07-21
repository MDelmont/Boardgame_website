
#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, request
from flask_restful import Resource, Api
from app.endpoints import endpoints

app = Flask(__name__)
api = Api(app)

endpoints.import_all_endpoint(app)

if __name__ == '__main__':
    app.run(debug=True)