import arcpy
arcpy.env.workspace = "C:/ArcpyBook/data/CityOfSanAntonio.gdb"
fcList = arcpy.ListFeatureClasses()
for fc in fcList:
    print(fc)

