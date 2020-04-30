import arcpy
arcpy.env.workspace = "c:/ArcpyBook/data/CityOfSanAntonio.gdb"
try:
    descFC = arcpy.Describe("Burglary")
    print("The shape type is: " + descFC.ShapeType)
    flds = descFC.fields
    for fld in flds:
        print("Field: " + fld.name)
        print("Type: " + fld.type)
        print("Length: " + str(fld.length))
    ext = descFC.extent
    print("XMin: %f" % (ext.XMin))
    print("YMin: %f" % (ext.YMin))
    print("XMax: %f" % (ext.XMax))
    print("YMax: %f" % (ext.YMax))
except:
    print(arcpy.GetMessages())
