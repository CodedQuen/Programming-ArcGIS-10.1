import arcpy
arcpy.env.workspace = "C:/ArcpyBook/data/CityOfSanAntonio.gdb"
fcList = arcpy.ListFeatureClasses("C*")
for fc in fcList:
    print(fc)

