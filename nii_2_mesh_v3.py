import vtk
import glob
import SimpleITK as sitk
import numpy as np

if __name__ == '__main__':
    
    # can be done in a loop if you have multiple files to be processed, speed is guaranteed if GPU is used:)
    filename_nii =  'verse096_seg.nii.gz'
    filename = filename_nii.split(".")[0]

    # read all the labels present in the file
    multi_label_image=sitk.ReadImage(filename_nii)
    img_npy = sitk.GetArrayFromImage(multi_label_image)
    labels = np.unique(img_npy)
    
    # read the file
    reader = vtk.vtkNIFTIImageReader()
    reader.SetFileName(filename_nii)
    reader.Update()
    
    
    for label in labels:

        if int(label) != 0:

            # apply marching cube surface generation
            surf = vtk.vtkDiscreteMarchingCubes()
            surf.SetInputConnection(reader.GetOutputPort())
            surf.SetValue(0, int(label)) # use surf.GenerateValues function if more than one contour is available in the file
            surf.Update()
            
            #smoothing the mesh
            smoother= vtk.vtkWindowedSincPolyDataFilter()
            if vtk.VTK_MAJOR_VERSION <= 5:
                smoother.SetInput(surf.GetOutput())
            else:
                smoother.SetInputConnection(surf.GetOutputPort())
            smoother.SetNumberOfIterations(30) 
            smoother.NonManifoldSmoothingOn()
            smoother.NormalizeCoordinatesOn() #The positions can be translated and scaled such that they fit within a range of [-1, 1] prior to the smoothing computation
            smoother.GenerateErrorScalarsOn()
            smoother.Update()
            
            # save the output
            writer = vtk.vtkSTLWriter()
            writer.SetInputConnection(smoother.GetOutputPort())
            writer.SetFileTypeToASCII()
            
            # file name need to be changed
            writer.SetFileName(f'{filename}_{label}.stl')
            writer.Write()
        
    
