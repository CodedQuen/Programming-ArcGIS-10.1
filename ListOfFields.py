import arcpy

arcpy.env.workspace = "C:/ArcpyBook/data/CityOfSanAntonio.gdb"
try:
    fieldList = arcpy.ListFields("Burglary")
    for fld in fieldList:
        print("%s is a type of %s with a length of %i" % (fld.name, fld.type, fld.length))
except Exception as e:
    print(e.message)
