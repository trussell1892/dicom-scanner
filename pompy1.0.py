import os
import pydicom
from datetime import datetime
from shutil import copyfile

rootdir = os.path.dirname(os.path.realpath(__file__))

rootdir = input("Enter path eg: 'C:\\projects\\dicom'  \n")
print("This is the path you entered:", rootdir, "\n")

for subdir, dirs, files in os.walk(rootdir):
    for file in files:
        #print os.path.join(subdir, file)
        filepath = subdir + os.sep + file
        ds = pydicom.dcmread(filepath)
        if ds.PatientName == 'palmer^leonard':
            print('Name: ', ds.PatientName, 'Study Date: ', 
                        str(ds.StudyDate),'Path: ', filepath, '\n')
            with open("log.csv", "a") as file:
                file.write(str(ds.PatientName) + "," + str(ds.StudyInstanceUID) + 
                 filepath + "\n")
            copyfile(filepath, filepath + 'PalmerLeonard' )

    else:
        pass