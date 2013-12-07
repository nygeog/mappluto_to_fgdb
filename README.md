MapPluto (2003 to 2013) to Esri File Geodatabase
================

The purpose of this script is to download the newly freely available MapPluto data, extract, merge to a File Geodatabse.
You can find them here: http://www.nyc.gov/html/dcp/html/bytes/archive_pluto_mappluto.shtml

But you don't need to b/c the script will download the files and extract for you (hopefully). 

Issues
======

1) Should I not include the Mappinglots on the merge? Not sure if those should be in the final FGDB? 

2) If running by pasting into ArcGIS Python command window make sure you turn OFF your checkbox Enable Background Processsing under Geoprocessing -> Options. The Create FileGeodatabase command does not like 64 bit Background Processing for some reason. 

Requirements (or at least what I used successfully) :
=============

Windows 7

Python 2.7

-import os

-import errno

-import re, urllib, time, zipfile, os

-import arcpy

ArcGIS 10.2

Time
====
Took 58 mins on my machine (Windows 7 virtual on Parallels iMac (12 GB allocated to Windows) while running from Sublime Text 2. 

Took 2 hours from pasting into ArcGIS python command. 

Errors
=======
If you find anything wrong or some part of the script that could be better please contact me. I don't have too much exp. with forking and pushing so if you'd like to modify something please be patient while I figure out how to incorporate your changes
