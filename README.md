# Niftis2Stl
Simple python code to transfer onesegmented nii.gz file to a list of stl files based on the labels

The segmented nii.gz file contains series of identical labels, such as 1,2,4,5. Then the code could transfer this single nii.gz file into series of .stl file using simpleITK and vtk to create the mesh. 

![name-of-you-image](img/new.PNG)

This code can be used in many medical imaging situations as a final step of processing output that be read by clients.

![name-of-you-image](img/GL_2018.PNG)

![name-of-you-image](img/image.png)
![name-of-you-image](img/1.png)
![name-of-you-image](img/2.png)

Labels do not require to be continuous, but need to be numbers (int, float...)
