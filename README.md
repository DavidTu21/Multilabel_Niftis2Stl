# Niftis2Stl
Simple python code to transfer segmented nii.gz file to a list of stl files based on the labels

The segmented nii.gz file contains series of identical labels, such as 1,2,4,5. Then the code could transfer this single nii.gz file into series of .stl file using simpleITK and vtk to create the mesh. 



Labels do not require to be continuous, but need to be numbers (int, float...)
