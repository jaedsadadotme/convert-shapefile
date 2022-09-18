from flask import Flask, request , render_template
import shapefile
from flask_cors import CORS
import json,os
from shapefile_reader import *

app = Flask(__name__)
CORS(app)

@app.route('/')
def hello():
    return render_template('index.html') 

@app.route('/api/data')
def hello_world():
    response = getLatLongFromShapeFile("shapefile/"+request.args['file'])
    return response

@app.route('/api/data', methods=['POST'])
def uploadShp():
    # return "hello"
    record1 = request.files['shp']
    record2 = request.files['dbf']
    print(record1)
    # record.save(secure_filename(record.filename))
    fn1 = "shapefile/"+record1.filename
    open(fn1, 'wb').write(record1.read())

    fn2 = "shapefile/"+record2.filename
    open(fn2, 'wb').write(record2.read())
    # print(record)
    # response = getLatLongFromShapeFile("shapefile/"+record1.filename)
    return record1.filename

# main driver function
if __name__ == '__main__':
    app.run()