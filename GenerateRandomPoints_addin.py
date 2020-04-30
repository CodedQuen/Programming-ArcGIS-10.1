import arcpy
import pythonaddins

def __init__(self):
  self.enabled = True
  self.cursor = 3
  self.shape = 'Rectangle'

def onRectangle(self, rectangle_geometry):
    extent = rectangle_geometry
    arcpy.env.workspace = r'c:\ArcpyBook\Ch10'
    if arcpy.Exists('randompts.shp'):
        arcpy.Delete_management('randompts.shp')
    randompts = arcpy.CreateRandomPoints_management(arcpy.env.workspace,'randompts.shp',"",rectangle_geometry)
    arcpy.RefreshActiveView()
    return randompts
