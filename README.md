MapPluto to Esri File Geodatabase
================

The purpose of this script is to download the newly freely available MapPluto data, extract, merge to a File Geodatabse.
You can find them here:

But you don't need to b/c the script will download the files and extract for you (hopefully). 

Issues
======

1) Should I not include the Mappinglots on the merge? Not sure if those should be in the final FGDB? 


Requirements (or at least what I used successfully) :
=============

Windows 7

Python 2.7

-import os

-import errno

-import re, urllib, time, zipfile, os

-import arcpy

ArcGIS 10.2



If you find anything wrong or some part of the script that could be better please contact me. I don't have too much exp. with forking and pushing so if you'd like to modify something please be patient while I figure out how to incorporate your changes
