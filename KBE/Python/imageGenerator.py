# NX 2206
# Journal created by mbergst on Thu Nov  9 15:21:41 2023 W. Europe Standard Time
#
import math
import NXOpen
import NXOpen.Gateway
def main() : 

    theSession  = NXOpen.Session.GetSession()
    workPart = theSession.Parts.Work
    displayPart = theSession.Parts.Display
    # ----------------------------------------------
    #   Menu: File->Export->Image...
    # ----------------------------------------------
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
    
    imageExportBuilder1.FileName = "M:\\Desktop\\TMM4270\\TMM4270-Automatisering\\KBE\\Python\\Images\\model1.png"
    
    imageExportBuilder1.BackgroundOption = NXOpen.Gateway.ImageExportBuilder.BackgroundOptions.Original
    
    imageExportBuilder1.EnhanceEdges = False
    
    nXObject1 = imageExportBuilder1.Commit()
    
    theSession.DeleteUndoMark(markId1, "Export Image")
    
    imageExportBuilder1.Destroy()
    
    # ----------------------------------------------
    #   Menu: Tools->Journal->Stop Recording
    # ----------------------------------------------
    
if __name__ == '__main__':
    main()