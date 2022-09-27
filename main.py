from flask import Flask, request , render_template
import shapefile
from flask_cors import CORS
import json,os,zipfile
import patoolib
from shapefile_reader import *

app = Flask(__name__)
CORS(app)

@app.route('/')
def hello():
    return render_template('index.html') 

@app.route('/api/data')
def hello_world():
    response = getLatLongFromShapeFile("shapefile/"+os.path.splitext(request.args['file'])[0]+"/"+request.args['file'])
    return response

@app.route('/api/data', methods=['POST'])
def uploadShp():
    # return "hello"
    record1 = request.files['shp']
    record2 = request.files['dbf']
    record3 = request.files['shx']
    record4 = request.files['prj']

    os.makedirs("shapefile/"+os.path.splitext(record1.filename)[0], exist_ok=True)
    # record.save(secure_filename(record.filename))
    fn1 = "shapefile/"+os.path.splitext(record1.filename)[0]+"/"+record1.filename
    open(fn1, 'wb').write(record1.read())

    fn2 = "shapefile/"+os.path.splitext(record1.filename)[0]+"/"+record2.filename
    open(fn2, 'wb').write(record2.read())

    fn3 = "shapefile/"+os.path.splitext(record1.filename)[0]+"/"+record3.filename
    open(fn3, 'wb').write(record3.read())
     
    fn4 = "shapefile/"+os.path.splitext(record1.filename)[0]+"/"+record4.filename
    open(fn4, 'wb').write(record4.read())
    # print(record)
    # response = getLatLongFromShapeFile("shapefile/"+record1.filename)
    return record1.filename

@app.route('/api/data/zipfile', methods=['POST'])
def uploadZip():
    # return "hello"
    record1 = request.files['zip']

    # os.makedirs("zip/"+os.path.splitext(record1.filename)[0], exist_ok=True)
    # record.save(secure_filename(record.filename))
    fn = "zip/"+record1.filename
    open(fn, 'wb').write(record1.read())

    # patoolib.extract_archive("zip/"+record1.filename, "shapefile/"+os.path.splitext(record1.filename)[0]+"/"+os.path.splitext(record1.filename)[0]+".shp")

    with zipfile.ZipFile("zip/"+record1.filename,"r") as zip_ref:
        zip_ref.extractall("shapefile/"+os.path.splitext(record1.filename)[0]+"/"+os.path.splitext(record1.filename)[0]+".shp")
    # print(record)
    # response = getLatLongFromShapeFile("shapefile/"+record1.filename)
    return os.path.splitext(record1.filename)[0]+".shp"

# main driver function
if __name__ == '__main__':
    app.run()