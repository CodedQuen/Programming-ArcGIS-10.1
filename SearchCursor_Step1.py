import arcpy.da
arcpy.env.workspace = "c:/ArcpyBook/Ch8"
with arcpy.da.SearchCursor("Schools.shp",("Facility","Name")) as cursor:
    for row in sorted(cursor):
        print("High school name: " + row[1])
