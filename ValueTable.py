import arcpy
try:

    arcpy.env.workspace = r'c:\ArcpyBook\data'

    vTab = arcpy.ValueTable()

    vTab.setRow (0, "5")
    vTab.setRow (1, "10")
    vTab.setRow (2, "20")

    inFeature = 'Hospitals.shp'
    outFeature = 'HospitalMBuff.shp'
    dist = vTab
    bufferUnit = "meters"

    arcpy.MultipleRingBuffer_analysis(inFeature,outFeature,dist,bufferUnit, '', 'ALL')
    print("Multi-Ring Buffer Complete")
except Exception as e:
    print(e.message)


