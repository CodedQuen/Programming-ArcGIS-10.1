import arcpy.da
arcpy.env.workspace = "c:/ArcpyBook/Ch8"
with arcpy.da.SearchCursor("Schools.shp",("Facility","Name"), '"FACILITY" = \'HIGH SCHOOL\'') as cursor:
        for row in sorted(cursor):
                print("School name: " + row[1])
