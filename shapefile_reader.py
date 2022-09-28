import string
import shapefile
import pandas as pd
import json,os
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
    # files = os.listdir(os.path.splitext(shp_file)[0])
    # print(files)
    geojson_data = geopandas.read_file(shp_file)
    old_crs = geojson_data.crs
    data = geojson_data.to_crs(epsg = 4326)
    id = 0
    datas = data
    datas.__geo_interface__["features"][id]["geometry"]["coordinates"] = swapCoordinate(data.__geo_interface__["features"][id]["geometry"]["coordinates"])
    
    response = {
        "old_crs" : "{}".format(old_crs),
        "new_crs" : "epsg:4326",
        "features": [
            {
                "bbox" : datas.__geo_interface__["features"][id]["bbox"][::-1],
                "geometry" : {
                    "coordinates": swapCoordinate(data.__geo_interface__["features"][id]["geometry"]["coordinates"]),
                    "type" : datas.__geo_interface__["features"][id]["geometry"]["type"]
                },
                "id": "0",
                "properties": datas.__geo_interface__["features"][id]["properties"],
                "type": datas.__geo_interface__["features"][id]["type"]
            }
        ],
        "type": datas.__geo_interface__["type"]
    }

    return json.dumps(response)