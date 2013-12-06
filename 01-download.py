import os
import errno
import re, urllib, time, zipfile, os
import arcpy


#put your file location here between quotes ie. "/Users/<YOURUSERNAME>/Downloads/census_2000"
folder_path = "C:/GIS/MapPluto"
folder_path_dl = folder_path+"/downloads"

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
l2 = ".zip"
lvars = ["13v2","13v1","12v2","12v1","11v2","11v1","10v2","10v1","09v2","09v1","07c","06c","05d","04c","03c","02b"]

stop_time = 5

for lvar in lvars:
    make_sure_path_exists(folder_path_dl+"/"+lvar)


#loop through all the mappluto files
for lvar in lvars:
        folder_path_dl_M = folder_path_dl + "/" +lvar

        print "Downloading... " + lvar
        #download the zip file
        urllib.urlretrieve(l1 + lvar + l2, folder_path_dl_M + "/mappluto_" + lvar + l2)

        #unzip the file
        zipfile.ZipFile(folder_path_dl_M + "/mappluto_" + lvar + l2).extractall(folder_path_dl_M + "/")

        #delete the zip file
        os.remove(folder_path_dl_M + "/mappluto_" + lvar + l2)
        print "Deleting... " + lvar + "'s ZIP file"

        #wait 3 seconds in case network connection is slow
        time.sleep(stop_time)
