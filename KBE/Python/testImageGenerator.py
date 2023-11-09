import math
import os
import NXOpen
import NXOpen.Gateway

class ImageGenerator:
    def __init__(self, filename):
        currentDirectory = os.path.dirname(os.path.abspath(__file__))
        image_directory_name = "Images"
        ImageFolderPath = os.path.join(currentDirectory, image_directory_name)
        self.filename = os.path.join(ImageFolderPath, filename)
        self.generate_image()
        
    def generate_image(self):
        theSession  = NXOpen.Session.GetSession()
        workPart = theSession.Parts.Work
        displayPart = theSession.Parts.Display
        
        markId1 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")
        
        imageExportBuilder1 = workPart.Views.CreateImageExportBuilder()
        
        imageExportBuilder1.RegionMode = False
        
        regiontopleftpoint1 = [None] * 2 
        regiontopleftpoint1[0] = 0
        regiontopleftpoint1[1] = 0
        imageExportBuilder1.SetRegionTopLeftPoint(regiontopleftpoint1)
        
        imageExportBuilder1.RegionWidth = 1
        
        imageExportBuilder1.RegionHeight = 1
        
        imageExportBuilder1.DeviceWidth = 1459
        
        imageExportBuilder1.DeviceHeight = 836
        
        imageExportBuilder1.FileFormat = NXOpen.Gateway.ImageExportBuilder.FileFormats.Png
        
        imageExportBuilder1.FileName = self.filename
        
        imageExportBuilder1.BackgroundOption = NXOpen.Gateway.ImageExportBuilder.BackgroundOptions.Original
        
        imageExportBuilder1.EnhanceEdges = False
        
        nXObject1 = imageExportBuilder1.Commit()
        
        theSession.DeleteUndoMark(markId1, "Export Image")
        
        imageExportBuilder1.Destroy()
