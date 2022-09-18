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


def getLatLongFromShapeFile() :
    geojson_data = shapefile.Reader(shp_file, encoding = 'unicode_escape').__geo_interface__

    id = 0
    coordinates = geojson_data["features"][id]["geometry"]["coordinates"]
    
    geojson_data["features"][id]["geometry"]["coordinates"] = swapCoordinate(coordinates)
    return geojson_data

# getLatLongFromShapeFile()