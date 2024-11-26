#Convert multipage pdf into a series of tif files
#Update area between lines before running
#Written by Randy Wierda

import arcpy
import os

#__________________________________________________________________________________________________________________
#In PDF parameters
inPdfPath = r"C:\Users\rwierda\Downloads"
inPdfFile = "5454-003-00 IFR 2020.09.16 prelim review.pdf"
inPdf = os.path.join(inPdfPath,inPdfFile)

#Basic Tiff parameters
outTiffPath = inPdfPath
outTiffPrefix = "2020_Water_Reservoir_and_Pumping_Station_Upgrading" #the filename prefix for your tif file
#__________________________________________________________________________________________________________________

#Convert pdf to pdf object and make a tif for each page
pdfObject = arcpy.mp.PDFDocumentOpen(inPdf)
pgzfill = int((len(str(pdfObject.pageCount))))#number of characters needed to make all filepaths the same length

for page in range(1,pdfObject.pageCount+1):
    outName = outTiffPrefix + "_" + str(page).zfill(pgzfill) + ".tif"
    print(outName)
    outTiff = os.path.join(outTiffPath,outName)
    #arcpy.PDFToTIFF_conversion(inPdf,outTiff,'#',str(page))
