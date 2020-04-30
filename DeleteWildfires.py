import arcpy
import os

arcpy.env.workspace = "C:/ArcpyBook/Ch8/WildfireData/WildlandFires.mdb"
try:
	with arcpy.da.UpdateCursor("FireIncidents",("CONFID_RATING"),'[CONFID_RATING] = \'POOR\'') as cursor:
		cntr = 1
		for row in cursor:
			cursor.deleteRow()
			print("Record number " + str(cntr) + " deleted")
			cntr = cntr + 1
except Exception as e:
    print(e.message)
