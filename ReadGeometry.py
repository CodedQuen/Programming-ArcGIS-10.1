import arcpy
infc = "c:/ArcpyBook/data/CityOfSanAntonio.gdb/SchoolDistricts"
# Enter for loop for each feature
for row in arcpy.da.SearchCursor(infc, ["OID@", "SHAPE@"]):
    # Print the current multipoint's ID
    print("Feature {0}:".format(row[0]))
    partnum = 0

    # Step through each part of the feature
    #
    for part in row[1]:
        # Print the part number
        #
        print("Part {0}:".format(partnum))

        # Step through each vertex in the feature
        #
        for pnt in part:
            if pnt:
                # Print x,y coordinates of current point
                #
                print("{0}, {1}".format(pnt.X, pnt.Y))
            else:
                # If pnt is None, this represents an interior ring
                #
                print("Interior Ring:")
        partnum += 1
