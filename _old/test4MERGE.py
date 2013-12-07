import os
import fnmatch

folderSearch = r'C:\GIS\MapPluto\downloads\12v2\MapPLUTO_12v2'
workspacedirectory = r'C:\GIS\MapPluto\downloads\12v2\MapPLUTO_12v2'
bigshapefile = r'C:\GIS\MapPluto\TEST.shp'
 
shpfilearray = []
for filename in os.listdir(folderSearch):
    if fnmatch.fnmatch(filename, '*.shp'):
        shpfilearray.append(filename)
        print shpfilearray


import arcpy
arcpy.env.workspace = workspacedirectory
arcpy.Merge_management(shpfilearray,bigshapefile)