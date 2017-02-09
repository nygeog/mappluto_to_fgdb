import os
import errno
import re, urllib, time, zipfile, os
import arcpy
from arcpy import env
from os import listdir
from os.path import isfile, join

env.overwriteOutput = True

#################################################
### THIS IS THE ONLY THING YOU NEED TO MODIFY ###
#################################################
#put your file location here between quotes ie. 
folder_path = "C:/GIS/MapPluto/"
#################################################
### THIS IS THE ONLY THING YOU NEED TO MODIFY ###
#################################################

folder_path_dl = folder_path+"/downloads"

print 'Started entire script at this time: ' + time.strftime('%c') 

def make_sure_path_exists(path):
    try:
        os.makedirs(path)
    except OSError as exception:
        if exception.errno != errno.EEXIST:
            raise

make_sure_path_exists(folder_path)
make_sure_path_exists(folder_path_dl)

saveloc = folder_path_dl + "/"

l1 = "http://www.nyc.gov/html/dcp/download/bytes/mappluto_"
l1 = "https://www1.nyc.gov/assets/planning/download/zip/data-maps/open-data/mappluto_"
l2 = ".zip"
lvars = ["16v2"]
#test set below, use if you wanna check the script to see if it works before trying
#lvars = ["13v2","13v1","12v2", "02b"]

stop_time = 5

for lvar in lvars:
    make_sure_path_exists(folder_path_dl+"/"+lvar)


#loop through all the mappluto files
for lvar in lvars:
        folder_path_dl_M = folder_path_dl + "/" +lvar

        print "Downloading... MapPluto_", l1 + lvar + l2
        #download the zip file
        urllib.urlretrieve(l1 + lvar + l2, folder_path_dl_M + "/mappluto_" + lvar + l2)

        #unzip the file
        zipfile.ZipFile(folder_path_dl_M + "/mappluto_" + lvar + l2).extractall(folder_path_dl_M + "/")
        print "Expanding the .zip file for... MapPluto" + lvar

        onlyfiles = [f for f in listdir(folder_path_dl_M) if isfile(join(folder_path_dl_M, f))]
        for i in onlyfiles:
            print i
            zipfile.ZipFile(folder_path_dl_M + "/" + i).extractall(folder_path_dl_M + "/")


        # Turn the remove script - 3 lines below this - OFF by uncommenting if you'd like to keep the source ZIPS
        #delete the zip file
        os.remove(folder_path_dl_M + "/mappluto_" + lvar + l2)
        print "Deleting the .zip... " + lvar + "'s ZIP file"

        #wait 
        time.sleep(stop_time)

#create file gdb and feature dataset
arcpy.CreateFileGDB_management(folder_path,"MapPluto","CURRENT")
for lvar in lvars:
   arcpy.CreateFeatureDataset_management(folder_path + "/MapPluto.gdb","mappluto_"+lvar,"PROJCS['NAD_1983_StatePlane_New_York_Long_Island_FIPS_3104_Feet',GEOGCS['GCS_North_American_1983',DATUM['D_North_American_1983',SPHEROID['GRS_1980',6378137.0,298.257222101]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]],PROJECTION['Lambert_Conformal_Conic'],PARAMETER['False_Easting',984250.0],PARAMETER['False_Northing',0.0],PARAMETER['Central_Meridian',-74.0],PARAMETER['Standard_Parallel_1',40.66666666666666],PARAMETER['Standard_Parallel_2',41.03333333333333],PARAMETER['Latitude_Of_Origin',40.16666666666666],UNIT['Foot_US',0.3048006096012192]];-120039300 -96540300 3048.00609601219;-100000 10000;-100000 10000;3.28083333333333E-03;0.001;0.001;IsHighPrecision")

#below is a function from Esri that I modified to do a Merge
#below was shamelessly stolen and modifed from http://arcpy.wordpress.com/2012/02/22/recursive-list-feature-classes/
def recursive_list_fcs(workspace, theMergeFile, wild_card=None, feature_type=None):
    """Returns a list of all feature classes in a tree.  Returned
    list can be limited by a wildcard, and feature type.
    """
    preexisting_wks = arcpy.env.workspace
    arcpy.env.workspace = workspace
    print workspace
 
    try:
        list_fcs = []
        for root, dirs, files in os.walk(workspace):
            arcpy.env.workspace = root
            fcs = arcpy.ListFeatureClasses(wild_card, feature_type)
            if fcs:
                list_fcs += [os.path.join(root, fc) for fc in fcs]
 
            # Pick up workspace types that don't have a folder
            #  structure (coverages, file geodatabase do)
            workspaces = set(arcpy.ListWorkspaces()) - \
                         set(arcpy.ListWorkspaces('', 'FILEGDB')) -\
                         set(arcpy.ListWorkspaces('', 'COVERAGE'))
 
            for workspace in workspaces:
                arcpy.env.workspace = os.path.join(root, workspace)
                fcs = arcpy.ListFeatureClasses(wild_card,
                                               feature_type)
 
                if fcs:
                    list_fcs += [os.path.join(root, workspace, fc)
                                 for fc in fcs]
 
            for dataset in arcpy.ListDatasets('', 'FEATURE'):
                ds_fcs = arcpy.ListFeatureClasses(wild_card,
                                                  feature_type,
                                                  dataset)
                if ds_fcs:
                    list_fcs += [os.path.join(
                        root, workspace, dataset, fc)
                                 for fc in ds_fcs]
 
    except Exception as err:
        raise err
    finally:
        arcpy.env.workspace = preexisting_wks
 
    #return list_fcs
    arcpy.Merge_management(list_fcs, theMergeFile )

for lvar in lvars:
    print "Merging all boros for MapPluto_" + lvar
    workspaceUse = folder_path+'/downloads/'+lvar
    theMergeFileUse = folder_path +'/MapPluto.gdb/mappluto_'+lvar+'/mappluto_'+lvar
    recursive_list_fcs(workspaceUse, theMergeFileUse, wild_card=None, feature_type=None)
    
print 'Ended the entire script at this time: ' + time.strftime('%c') 
print "All right, all done. Let me know of any errors, how long it took to run completely, etc. Feel free to delete the 'downloads' folder "
