from flask import Flask, request
import shapefile
from flask_cors import CORS
import json,os
from shapefile_reader import *

app = Flask(__name__)
CORS(app)

@app.route('/')
def hello_world():
    response = getLatLongFromShapeFile()
    return response

@app.route('/', methods=['POST'])
def uploadShp():
    record1 = request.files['shp']
    record2 = request.files['dbf']
    # record.save(secure_filename(record.filename))
    fn1 = "shapefile/"+record1.filename
    open(fn1, 'wb').write(record1.read())

    fn2 = "shapefile/"+record2.filename
    open(fn2, 'wb').write(record2.read())
    # print(record)
    # response = getLatLongFromShapeFile()
    # return "hello"

# main driver function
if __name__ == '__main__':
    app.run()