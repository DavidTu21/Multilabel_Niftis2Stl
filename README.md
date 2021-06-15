# Niftis2Stl
Simple python code to transfer onesegmented nii.gz file to a list of stl files based on the labels

The segmented nii.gz file contains series of identical labels, such as 1,2,4,5. Then the code could transfer this single nii.gz file into series of .stl file using simpleITK and vtk to create the mesh. 

![name-of-you-image](img/new.PNG)

This code can be used in many medical imaging situations as a final step of processing output that be read by clients.
Labels do not require to be continuous, but need to be numbers (int, float...)



#### Sample Output .STL Files

<table>
  <tr>
    <td>T7</td>
     <td>T10</td>
     <td>L5</td>
  </tr>
  <tr>
    <td><img src="img/image.png" width=480 height=220></td>
    <td><img src="img/1.png" width=480 height=220></td>
    <td><img src="img/2.png" width=480 height=220></td>
  </tr>
 </table>


