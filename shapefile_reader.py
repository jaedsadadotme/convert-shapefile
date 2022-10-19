import shapefile
import pandas as pd

shp_file = "./shapefile/979fc2b6b36d3aae-polygon.shp"

def swapCoordinate(coordinates) :
    coordinates[0] = [list(s) for s in coordinates[0]]

    long = [s[0] for s in coordinates[0]]
    lat = [s[1] for s in coordinates[0]]
    df = pd.DataFrame(list(zip(lat,long)))

    new_coordinate = df.values.tolist()
    return new_coordinate


def getLatLongFromShapeFile(shp_file) :
    geojson_data = shapefile.Reader(shp_file, encoding = 'unicode_escape').__geo_interface__
    coordinates = []
    for id, features in enumerate(geojson_data['features']):
        # coordinates.append(swapCoordinate(features["geometry"]["coordinates"]))
        geojson_data["features"][id]["geometry"]["coordinates"] = swapCoordinate(features["geometry"]["coordinates"])


    # id = 0
    
    
    return geojson_data

# getLatLongFromShapeFile("./shapefile/shapefile_test.shp")