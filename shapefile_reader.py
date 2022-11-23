import string
import shapefile
import pandas as pd
import json,os,pyproj
import geopandas,pandas

shp_file = "./shapefile/other/979fc2b6b36d3aae-polygon.shp"

def swapCoordinate(coordinates) :
    coordinates = [list(s) for s in coordinates]

    long = [s[0] for s in coordinates[0]]
    lat = [s[1] for s in coordinates[0]]
    df = pd.DataFrame(list(zip(lat,long)))

    new_coordinate = df.values.tolist()

    return new_coordinate

def getLatLongFromShapeFile(shp_file) :
    list_dir = os.listdir(shp_file);
    if(any(File.endswith(".shp") for File in list_dir)):
        print("true")
        geojson_data = _convertShapefile(shp_file+"/"+shp_file.split("/")[1]+".shp")
    else:
        print("false")
        for dir in list_dir:
            if(any(File.endswith(".shp") for File in os.listdir(shp_file+"/"+dir))):
                print("true")
                geojson_data = _convertShapefile(shp_file+"/"+dir+"/"+shp_file.split("/")[1]+".shp")
            else:
                print("false") 
    
    return geojson_data

    # id = 0
    
def _convertShapefile(shp_file) :
    print(shp_file)
    geojson_data = shapefile.Reader(shp_file, encoding = 'unicode_escape').__geo_interface__

    data = geopandas.read_file(shp_file)
    # change CRS to epsg 4326
    data = data.to_crs(epsg=4326)
    # coordinates = []
    # geojson_data = data.to_json()
    
    geojson_data = json.loads(data.to_json())
    for id , features in enumerate(geojson_data['features']):
        # coordinates.append(swapCoordinate(features["geometry"]["coordinates"]))
        geojson_data["features"][id]["geometry"]["coordinates"] = swapCoordinate(features["geometry"]["coordinates"])
    
    print(geojson_data)
    return geojson_data

getLatLongFromShapeFile("shapefile/aaa")
