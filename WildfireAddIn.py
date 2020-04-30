import arcpy
import pythonaddins

class ButtonClassImportWildfires(object):
    """Implementation for Wildfire_addin.button (Button)"""
    def __init__(self):
        self.enabled = True
        self.checked = False

    def onClick(self):
        layer_files = pythonaddins.OpenDialog('Select Layers to Add', True, r'C:\ArcpyBook\data\Wildfires', 'Add')
        mxd = arcpy.mapping.MapDocument('current')
        df = pythonaddins.GetSelectedTOCLayerOrDataFrame()
        if not isinstance(df, arcpy.mapping.Layer):
            for layer_file in layer_files:
                layer = arcpy.mapping.Layer(layer_file)
                arcpy.mapping.AddLayer(df, layer)
        else:
            pythonaddins.MessageBox('Select a data frame', 'INFO', 0)
