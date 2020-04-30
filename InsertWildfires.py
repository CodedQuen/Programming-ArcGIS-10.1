import arcpy
import os

arcpy.env.workspace = "C:/ArcpyBook/Ch8/WildfireData/WildlandFires.mdb"
f = open("C:/ArcpyBook/Ch8/WildfireData/NorthAmericaWildfires_2007275.txt","r")
lstFires = f.readlines()
try:
        with arcpy.da.InsertCursor("FireIncidents",("SHAPE@XY","CONFIDENCEVALUE")) as cur:
                cntr = 1
                for fire in lstFires:
                        if 'Latitude' in fire:
                                continue
                        vals = fire.split(",")
                        latitude = float(vals[0])
                        longitude = float(vals[1])
                        confid = int(vals[2])
                        rowValue = [(latitude,longitude),confid]
                        cur.insertRow(rowValue)
                        print("Record number " + str(cntr) + " written to feature class")
                        cntr = cntr + 1
except Exception as e:
        print(e.message)
finally:
    f.close()
