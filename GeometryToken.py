import arcpy.da
import time
arcpy.env.workspace = "c:/ArcpyBook/Ch8"
start = time.clock()
with arcpy.da.SearchCursor("coa_parcels.shp",("PY_FULL_OW","SHAPE@XY")) as cursor:
    for row in cursor:
        print("Parcel owner: {0} has a location of: {1}".format(row[0], row[1]))
elapsed = (time.clock() - start)
print("Execution time: " + str(elapsed))
