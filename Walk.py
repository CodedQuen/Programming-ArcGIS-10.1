import arcpy.da as da
import os

print("os walk")

for dirpath, dirnames, filenames in os.walk(os.getcwd()):
    for filename in filenames:
        print(filename)

print("arcpy da walk")

for dirpath, dirnames, filenames in da.Walk(os.getcwd(),datatype="FeatureClass"):
    for filename in filenames:
        print(os.path.join(dirpath, filename))
