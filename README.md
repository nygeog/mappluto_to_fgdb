MapPluto (2003 to 2013) to Esri File Geodatabase
================

The purpose of this script is to download the newly freely available MapPluto data, extract, merge to a File Geodatabse.
You can find them here: http://www.nyc.gov/html/dcp/html/bytes/archive_pluto_mappluto.shtml

But you don't need to b/c the script will download the files and extract for you (hopefully). 

Download
========
If you don't have the disk space, internet connection or patience - I've just posted the FGDB (I think its 10.2) to Dropbox - not sure how long I'll be able to have it up. So if you don't have 10.2, run the script, the Create File Geodatabase will create a current GDB, I think from 9.3.1 and up, whenever arcpy...
https://www.dropbox.com/s/8awhycijrs8tf4f/MapPluto.zip


Issues
======

1) Should I not include the Mappinglots on the merge? Not sure if those should be in the final FGDB? 

2) If running by pasting into ArcGIS Python command window make sure you turn OFF your checkbox Enable Background Processsing under Geoprocessing -> Options. The Create FileGeodatabase command does not like 64 bit Background Processing for some reason. 

Requirements (or at least what I used) :
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

May take longer from pasting into ArcGIS python command. Though, I got some weird urllib error. So maybe run in PythonWIN, Idle, Sublime Text 2 (need to save the .py file somewhere on your system then hit CTRL + B to run the code, you'll have needed to point to Python in your Python-Build see http://stackoverflow.com/questions/8551735/how-do-i-run-python-code-from-sublime-text-2). 

Time depends on your internet connection for downloads and your processor. 

Errors
=======
If you find anything wrong or some part of the script that could be better please contact me. I don't have too much exp. with forking and pushing so if you'd like to modify something please be patient while I figure out how to incorporate your changes
