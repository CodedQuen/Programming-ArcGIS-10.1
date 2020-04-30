import arcpy
arcpy.env.workspace = "c:/ArcpyBook/data"
try:
    descRaster = arcpy.Describe("AUSTIN_EAST_NW.sid")
    ext = descRaster.extent
    print("XMin: %f" % (ext.XMin))
    print("YMin: %f" % (ext.YMin))
    print("XMax: %f" % (ext.XMax))
    print("YMax: %f" % (ext.YMax))
	
    sr = descRaster.SpatialReference
    print(sr.name)
    print(sr.type)
except Exception as e:
    print e.message
