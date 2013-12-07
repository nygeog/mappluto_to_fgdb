import os
import arcpy

root = r'C:\GIS\MapPluto\downloads\13v1\MapPLUTO_13v1'
output_file_spot = "C:/GIS/MapPluto/MapPluto.gdb/mappluto_13v1/test50"

fc_set = []
for path, subdirs, files in os.walk(root):
    arcpy.env.workspace = path
    fc_list = arcpy.ListFeatureClasses()
    for fc in fc_list:
      	fc_set.append(fc)
        print fc
        arcpy.Copy_management(fc, root+fc)
        arcpy.Delete_management(fc)
    print fc_set






    bringIT = fc_set
    finalFc_set = []
    for i in bringIT:
    	print i
    	finalFc_set.append("test"+i)
    print finalFc_set

    #print bringIT[]
    #arcpy.Merge_management(finalFc_set, output_file_spot)


