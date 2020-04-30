import arcpy
try:
    arcpy.env.workspace = "c:/ArcpyBook/data"
    arcpy.Buffer_analysis("Streams.shp","Streams_Buff.shp")
except:
    print("Error")
