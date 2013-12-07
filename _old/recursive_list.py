import os
import arcpy
 
workspaceUSE = r'C:\GIS\MapPluto\downloads\13v1'

def recursive_list_fcs(workspace, wild_card=None, feature_type=None):
    """Returns a list of all feature classes in a tree.  Returned
    list can be limited by a wildcard, and feature type.
    """
    preexisting_wks = arcpy.env.workspace
    arcpy.env.workspace = workspace
 
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
    arcpy.Merge_management(list_fcs, r'C:\GIS\MapPluto\MapPluto.gdb\mappluto_13v1\testNEW21')


recursive_list_fcs(workspaceUSE, wild_card=None, feature_type=None)