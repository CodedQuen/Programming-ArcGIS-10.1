import arcpy
try:
    arcpy.env.workspace = "c:/ArcpyBook/data"
    arcpy.Buffer_analysis("Streams.shp", "Streams_Buff.shp")
except:
    print("Error found in Buffer tool \n")
    errCode = arcpy.GetReturnCode(3)
    if str(errCode) == "735":
        print("Distance value not provided \n")
        print("Running the buffer again with a default value \n")
        defaultDistance = "100 Feet"
        arcpy.Buffer_analysis("Streams.shp", "Streams_Buff", defaultDistance)
        print("Buffer complete")
