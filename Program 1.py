import pandas
import os
from geopy.geocoders import ArcGIS


df=pandas.read_csv("supermarkets.csv")


Geomap=ArcGIS()

"""

Address1=Geomap.geocode("735 Dolores St, San Francisco, CA 94119 ")

Long=Address1.longitude
Lat=Address1.latitude

print(Long,Lat)

"""

df["Address"]=df["Address"]+' , '+df["City"]+" , "+df["State"]+" , "+df["Country"]

"""

print(df.to_string())

"""

df["Coordinates"]=df["Address"].apply(Geomap.geocode)


"""
print(df.Coordinates)
print(df.Coordinates[0].longitude)

"""

df["Latitude"]=df["Coordinates"].apply(lambda x: x.latitude)
df["Longitude"]=df["Coordinates"].apply(lambda x: x.longitude)

print(df.to_string())















