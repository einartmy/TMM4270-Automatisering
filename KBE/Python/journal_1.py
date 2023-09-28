# NX 2206
# Journal created by mbergst on Tue Sep 19 13:47:28 2023 W. Europe Daylight Time
#
import math
import NXOpen
import NXOpen.Features
import NXOpen.GeometricUtilities
import NXOpen.Preferences
def main() : 

    theSession  = NXOpen.Session.GetSession()
    workPart = theSession.Parts.Work
    displayPart = theSession.Parts.Display
    # ----------------------------------------------
    #   Menu: Insert->Sketch
    # ----------------------------------------------
    markId1 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Enter Sketch")
    
    markId2 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Update Model from Sketch")
    
    theSession.BeginTaskEnvironment()
    
    markId3 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")
    
    sketchInPlaceBuilder1 = workPart.Sketches.CreateSketchInPlaceBuilder2(NXOpen.Sketch.Null)
    
    origin1 = NXOpen.Point3d(0.0, 0.0, 0.0)
    normal1 = NXOpen.Vector3d(0.0, 0.0, 1.0)
    plane1 = workPart.Planes.CreatePlane(origin1, normal1, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    sketchInPlaceBuilder1.PlaneReference = plane1
    
    unit1 = workPart.UnitCollection.FindObject("MilliMeter")
    expression1 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    expression2 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    sketchAlongPathBuilder1 = workPart.Sketches.CreateSketchAlongPathBuilder(NXOpen.Sketch.Null)
    
    simpleSketchInPlaceBuilder1 = workPart.Sketches.CreateSimpleSketchInPlaceBuilder()
    
    theSession.SetUndoMarkName(markId3, "Create Sketch Dialog")
    
    simpleSketchInPlaceBuilder1.UseWorkPartOrigin = False
    
    coordinates1 = NXOpen.Point3d(0.0, 0.0, 0.0)
    point1 = workPart.Points.CreatePoint(coordinates1)
    
    nErrs1 = theSession.UpdateManager.AddToDeleteList(point1)
    
    coordinates2 = NXOpen.Point3d(0.0, 0.0, 0.0)
    point2 = workPart.Points.CreatePoint(coordinates2)
    
    nErrs2 = theSession.UpdateManager.AddToDeleteList(point2)
    
    markId4 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Create Sketch")
    
    theSession.DeleteUndoMark(markId4, None)
    
    markId5 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Create Sketch")
    
    origin2 = NXOpen.Point3d(0.0, 0.0, 0.0)
    vector1 = NXOpen.Vector3d(1.0, 0.0, 0.0)
    direction1 = workPart.Directions.CreateDirection(origin2, vector1, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    coordinates3 = NXOpen.Point3d(0.0, 0.0, 0.0)
    point3 = workPart.Points.CreatePoint(coordinates3)
    
    origin3 = NXOpen.Point3d(0.0, 0.0, 0.0)
    matrix1 = NXOpen.Matrix3x3()
    
    matrix1.Xx = 1.0
    matrix1.Xy = 0.0
    matrix1.Xz = 0.0
    matrix1.Yx = 0.0
    matrix1.Yy = 1.0
    matrix1.Yz = 0.0
    matrix1.Zx = 0.0
    matrix1.Zy = 0.0
    matrix1.Zz = 1.0
    plane2 = workPart.Planes.CreateFixedTypePlane(origin3, matrix1, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    xform1 = workPart.Xforms.CreateXformByPlaneXDirPoint(plane2, direction1, point3, NXOpen.SmartObject.UpdateOption.WithinModeling, 1.0, False, False)
    
    cartesianCoordinateSystem1 = workPart.CoordinateSystems.CreateCoordinateSystem(xform1, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    simpleSketchInPlaceBuilder1.CoordinateSystem = cartesianCoordinateSystem1
    
    theSession.Preferences.Sketch.CreateInferredConstraints = False
    
    theSession.Preferences.Sketch.ContinuousAutoDimensioning = False
    
    theSession.Preferences.Sketch.DimensionLabel = NXOpen.Preferences.SketchPreferences.DimensionLabelType.Expression
    
    theSession.Preferences.Sketch.TextSizeFixed = False
    
    theSession.Preferences.Sketch.FixedTextSize = 3.0
    
    theSession.Preferences.Sketch.DisplayParenthesesOnReferenceDimensions = True
    
    theSession.Preferences.Sketch.DisplayReferenceGeometry = False
    
    theSession.Preferences.Sketch.DisplayShadedRegions = True
    
    theSession.Preferences.Sketch.FindMovableObjects = True
    
    theSession.Preferences.Sketch.ConstraintSymbolSize = 3.0
    
    theSession.Preferences.Sketch.DisplayObjectColor = False
    
    theSession.Preferences.Sketch.DisplayObjectName = True
    
    theSession.Preferences.Sketch.EditDimensionOnCreation = True
    
    theSession.Preferences.Sketch.CreateDimensionForTypedValues = True
    
    nXObject1 = simpleSketchInPlaceBuilder1.Commit()
    
    sketch1 = nXObject1
    feature1 = sketch1.Feature
    
    markId6 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "update")
    
    nErrs3 = theSession.UpdateManager.DoUpdate(markId6)
    
    sketch1.Activate(NXOpen.Sketch.ViewReorient.TrueValue)
    
    theSession.Preferences.Sketch.FindMovableObjects = True
    
    sketchFindMovableObjectsBuilder1 = workPart.Sketches.CreateFindMovableObjectsBuilder()
    
    nXObject2 = sketchFindMovableObjectsBuilder1.Commit()
    
    sketchFindMovableObjectsBuilder1.Destroy()
    
    theSession.DeleteUndoMark(markId5, None)
    
    theSession.SetUndoMarkName(markId3, "Create Sketch")
    
    sketchInPlaceBuilder1.Destroy()
    
    sketchAlongPathBuilder1.Destroy()
    
    simpleSketchInPlaceBuilder1.Destroy()
    
    try:
        # Expression is still in use.
        workPart.Expressions.Delete(expression2)
    except NXOpen.NXException as ex:
        ex.AssertErrorCode(1050029)
        
    try:
        # Expression is still in use.
        workPart.Expressions.Delete(expression1)
    except NXOpen.NXException as ex:
        ex.AssertErrorCode(1050029)
        
    plane1.DestroyPlane()
    
    theSession.DeleteUndoMarksUpToMark(markId2, None, True)
    
    markId7 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Open Sketch")
    
    theSession.ActiveSketch.SetName("SKETCH_000")
    
    # ----------------------------------------------
    #   Menu: Insert->Curve->Circle...
    # ----------------------------------------------
    markId8 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Profile short list")
    
    markId9 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Curve")
    
    rotMatrix1 = NXOpen.Matrix3x3()
    
    rotMatrix1.Xx = 0.98792222098905302
    rotMatrix1.Xy = 0.004729369824487138
    rotMatrix1.Xz = -0.15487839854905888
    rotMatrix1.Yx = -0.0054382732852853834
    rotMatrix1.Yy = 0.99997658534299316
    rotMatrix1.Yz = -0.0041537873612888165
    rotMatrix1.Zx = 0.15485512732787515
    rotMatrix1.Zy = 0.0049458898927778336
    rotMatrix1.Zz = 0.98792480873467114
    translation1 = NXOpen.Point3d(0.0, 0.0, 0.0)
    workPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix1, translation1, 0.28146919880873872)
    
    theSession.SetUndoMarkVisibility(markId9, "Curve", NXOpen.Session.MarkVisibility.Visible)
    
    nXMatrix1 = theSession.ActiveSketch.Orientation
    
    center1 = NXOpen.Point3d(0.0, 0.0, 0.0)
    arc1 = workPart.Curves.CreateArc(center1, nXMatrix1, 238.30387261332848, 0.0, ( 360.0 * math.pi/180.0 ))
    
    theSession.ActiveSketch.AddGeometry(arc1, NXOpen.Sketch.InferConstraintsOption.InferNoConstraints)
    
    theSession.ActiveSketch.Update()
    
    sketchFindMovableObjectsBuilder2 = workPart.Sketches.CreateFindMovableObjectsBuilder()
    
    nXObject3 = sketchFindMovableObjectsBuilder2.Commit()
    
    sketchFindMovableObjectsBuilder2.Destroy()
    
    # ----------------------------------------------
    #   Menu: Task->Finish Sketch
    # ----------------------------------------------
    sketchWorkRegionBuilder1 = workPart.Sketches.CreateWorkRegionBuilder()
    
    sketchWorkRegionBuilder1.Scope = NXOpen.SketchWorkRegionBuilder.ScopeType.EntireSketch
    
    nXObject4 = sketchWorkRegionBuilder1.Commit()
    
    sketchWorkRegionBuilder1.Destroy()
    
    theSession.ActiveSketch.CalculateStatus()
    
    theSession.Preferences.Sketch.SectionView = False
    
    markId10 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Deactivate Sketch")
    
    theSession.ActiveSketch.Deactivate(NXOpen.Sketch.ViewReorient.TrueValue, NXOpen.Sketch.UpdateLevel.Model)
    
    theSession.DeleteUndoMarksSetInTaskEnvironment()
    
    theSession.EndTaskEnvironment()
    
    # ----------------------------------------------
    #   Menu: Insert->Design Feature->Extrude...
    # ----------------------------------------------
    markId11 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")
    
    extrudeBuilder1 = workPart.Features.CreateExtrudeBuilder(NXOpen.Features.Feature.Null)
    
    section1 = workPart.Sections.CreateSection(0.0094999999999999998, 0.01, 0.5)
    
    extrudeBuilder1.Section = section1
    
    extrudeBuilder1.AllowSelfIntersectingSection(True)
    
    unit2 = extrudeBuilder1.Draft.FrontDraftAngle.Units
    
    expression3 = workPart.Expressions.CreateSystemExpressionWithUnits("2.00", unit2)
    
    extrudeBuilder1.DistanceTolerance = 0.01
    
    extrudeBuilder1.BooleanOperation.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Create
    
    targetBodies1 = [NXOpen.Body.Null] * 1 
    targetBodies1[0] = NXOpen.Body.Null
    extrudeBuilder1.BooleanOperation.SetTargetBodies(targetBodies1)
    
    extrudeBuilder1.Limits.StartExtend.Value.SetFormula("0")
    
    extrudeBuilder1.Limits.EndExtend.Value.SetFormula("25")
    
    extrudeBuilder1.Offset.StartOffset.SetFormula("0")
    
    extrudeBuilder1.Offset.EndOffset.SetFormula("5")
    
    smartVolumeProfileBuilder1 = extrudeBuilder1.SmartVolumeProfile
    
    smartVolumeProfileBuilder1.OpenProfileSmartVolumeOption = False
    
    smartVolumeProfileBuilder1.CloseProfileRule = NXOpen.GeometricUtilities.SmartVolumeProfileBuilder.CloseProfileRuleType.Fci
    
    theSession.SetUndoMarkName(markId11, "Extrude Dialog")
    
    section1.DistanceTolerance = 0.01
    
    section1.ChainingTolerance = 0.0094999999999999998
    
    section1.SetAllowedEntityTypes(NXOpen.Section.AllowTypes.OnlyCurves)
    
    markId12 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, None)
    
    selectionIntentRuleOptions1 = workPart.ScRuleFactory.CreateRuleOptions()
    
    selectionIntentRuleOptions1.SetSelectedFromInactive(False)
    
    curves1 = [NXOpen.ICurve.Null] * 1 
    curves1[0] = arc1
    seedPoint1 = NXOpen.Point3d(-31.385032236839333, -15.638617313818617, 0.0)
    regionBoundaryRule1 = workPart.ScRuleFactory.CreateRuleRegionBoundary(sketch1, curves1, seedPoint1, 0.01, selectionIntentRuleOptions1)
    
    selectionIntentRuleOptions1.Dispose()
    section1.AllowSelfIntersection(True)
    
    section1.AllowDegenerateCurves(False)
    
    rules1 = [None] * 1 
    rules1[0] = regionBoundaryRule1
    helpPoint1 = NXOpen.Point3d(0.0, 0.0, 0.0)
    section1.AddToSection(rules1, NXOpen.NXObject.Null, NXOpen.NXObject.Null, NXOpen.NXObject.Null, helpPoint1, NXOpen.Section.Mode.Create, False)
    
    theSession.DeleteUndoMark(markId12, None)
    
    markId13 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "section mark")
    
    markId14 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, None)
    
    theSession.DeleteUndoMark(markId14, None)
    
    direction2 = workPart.Directions.CreateDirection(sketch1, NXOpen.Sense.Forward, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    extrudeBuilder1.Direction = direction2
    
    extrudeBuilder1.BooleanOperation.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Create
    
    targetBodies2 = [NXOpen.Body.Null] * 1 
    targetBodies2[0] = NXOpen.Body.Null
    extrudeBuilder1.BooleanOperation.SetTargetBodies(targetBodies2)
    
    targetBodies3 = []
    extrudeBuilder1.BooleanOperation.SetTargetBodies(targetBodies3)
    
    theSession.DeleteUndoMark(markId13, None)
    
    extrudeBuilder1.BooleanOperation.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Create
    
    targetBodies4 = [NXOpen.Body.Null] * 1 
    targetBodies4[0] = NXOpen.Body.Null
    extrudeBuilder1.BooleanOperation.SetTargetBodies(targetBodies4)
    
    targetBodies5 = []
    extrudeBuilder1.BooleanOperation.SetTargetBodies(targetBodies5)
    
    extrudeBuilder1.Limits.EndExtend.Value.SetFormula("375")
    
    extrudeBuilder1.BooleanOperation.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Create
    
    targetBodies6 = [NXOpen.Body.Null] * 1 
    targetBodies6[0] = NXOpen.Body.Null
    extrudeBuilder1.BooleanOperation.SetTargetBodies(targetBodies6)
    
    targetBodies7 = []
    extrudeBuilder1.BooleanOperation.SetTargetBodies(targetBodies7)
    
    markId15 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Extrude")
    
    theSession.DeleteUndoMark(markId15, None)
    
    markId16 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Extrude")
    
    extrudeBuilder1.ParentFeatureInternal = False
    
    feature2 = extrudeBuilder1.CommitFeature()
    
    theSession.DeleteUndoMark(markId16, None)
    
    theSession.SetUndoMarkName(markId11, "Extrude")
    
    expression4 = extrudeBuilder1.Limits.StartExtend.Value
    expression5 = extrudeBuilder1.Limits.EndExtend.Value
    extrudeBuilder1.Destroy()
    
    workPart.Expressions.Delete(expression3)
    
    rotMatrix2 = NXOpen.Matrix3x3()
    
    rotMatrix2.Xx = 0.46678369014623849
    rotMatrix2.Xy = 0.88148167406360312
    rotMatrix2.Xz = -0.071435599692935184
    rotMatrix2.Yx = -0.083746813377222173
    rotMatrix2.Yy = 0.12447086667112749
    rotMatrix2.Yz = 0.98868269662177344
    rotMatrix2.Zx = 0.88039732954082817
    rotMatrix2.Zy = -0.45551845367687094
    rotMatrix2.Zz = 0.13192225171369529
    translation2 = NXOpen.Point3d(2.6788349884850695, -2.3185343415069468, 9.1311366388709949)
    workPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix2, translation2, 0.28146919880873872)
    
    scaleAboutPoint1 = NXOpen.Point3d(7.5200649862401869, -76.610662047321668, 0.0)
    viewCenter1 = NXOpen.Point3d(-7.5200649862401869, 76.610662047321668, 0.0)
    workPart.ModelingViews.WorkView.ZoomAboutPoint(1.25, scaleAboutPoint1, viewCenter1)
    
    origin4 = NXOpen.Point3d(-49.478841475530551, -90.098113321979071, -50.116260970285829)
    workPart.ModelingViews.WorkView.SetOrigin(origin4)
    
    origin5 = NXOpen.Point3d(-49.478841475530551, -90.098113321979071, -50.116260970285829)
    workPart.ModelingViews.WorkView.SetOrigin(origin5)
    
    rotMatrix3 = NXOpen.Matrix3x3()
    
    rotMatrix3.Xx = 0.72583030652068392
    rotMatrix3.Xy = 0.68677456179434104
    rotMatrix3.Xz = -0.038872450505226315
    rotMatrix3.Yx = -0.2608509649751668
    rotMatrix3.Yy = 0.3270949026307518
    rotMatrix3.Yz = 0.90827622381327699
    rotMatrix3.Zx = 0.63649598601060697
    rotMatrix3.Zy = -0.64911449371060193
    rotMatrix3.Zz = 0.41656120060228319
    translation3 = NXOpen.Point3d(97.714548717820023, 59.635217718468958, -1.542823944451051)
    workPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix3, translation3, 0.35183649851092341)
    
    origin6 = NXOpen.Point3d(-170.2218663630758, -154.92314847350846, 22.38686060263348)
    workPart.ModelingViews.WorkView.SetOrigin(origin6)
    
    origin7 = NXOpen.Point3d(-170.2218663630758, -154.92314847350846, 22.38686060263348)
    workPart.ModelingViews.WorkView.SetOrigin(origin7)
    
    rotMatrix4 = NXOpen.Matrix3x3()
    
    rotMatrix4.Xx = 0.81836085929142544
    rotMatrix4.Xy = -0.23069220418522651
    rotMatrix4.Xz = -0.52637117218552398
    rotMatrix4.Yx = 0.38146700344700879
    rotMatrix4.Yy = 0.9030853929956929
    rotMatrix4.Yz = 0.19728075993105881
    rotMatrix4.Zx = 0.42984698354293377
    rotMatrix4.Zy = -0.36224008597334806
    rotMatrix4.Zz = 0.82705120207461436
    translation4 = NXOpen.Point3d(249.10090103728203, 12.600910748898563, -16.936198999663457)
    workPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix4, translation4, 0.35183649851092341)
    
    origin8 = NXOpen.Point3d(-161.6687791217486, 129.0751643307207, 161.03626272268562)
    workPart.ModelingViews.WorkView.SetOrigin(origin8)
    
    origin9 = NXOpen.Point3d(-161.6687791217486, 129.0751643307207, 161.03626272268562)
    workPart.ModelingViews.WorkView.SetOrigin(origin9)
    
    rotMatrix5 = NXOpen.Matrix3x3()
    
    rotMatrix5.Xx = 0.75319658825355063
    rotMatrix5.Xy = -0.17760028342058456
    rotMatrix5.Xz = -0.63336643325340569
    rotMatrix5.Yx = 0.38769741032664118
    rotMatrix5.Yy = 0.89770459068605468
    rotMatrix5.Yz = 0.2093255500105049
    rotMatrix5.Zx = 0.5313996777089981
    rotMatrix5.Zy = -0.40321781606237711
    rotMatrix5.Zz = 0.74500320491972527
    translation5 = NXOpen.Point3d(250.85720383145537, -87.115626697450665, -13.859399106355117)
    workPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix5, translation5, 0.35183649851092341)
    
    origin10 = NXOpen.Point3d(118.97310443318241, 54.262908672283835, -36.889906695646978)
    workPart.ModelingViews.WorkView.SetOrigin(origin10)
    
    origin11 = NXOpen.Point3d(118.97310443318241, 54.262908672283835, -36.889906695646978)
    workPart.ModelingViews.WorkView.SetOrigin(origin11)
    
    rotMatrix6 = NXOpen.Matrix3x3()
    
    rotMatrix6.Xx = 0.46617073906541923
    rotMatrix6.Xy = -0.28897437595902375
    rotMatrix6.Xz = 0.83616903319741243
    rotMatrix6.Yx = 0.36520718686183468
    rotMatrix6.Yy = 0.92371782287304371
    rotMatrix6.Yz = 0.11562479998318148
    rotMatrix6.Zx = -0.80579684331949541
    rotMatrix6.Zy = 0.25147404189255623
    rotMatrix6.Zz = 0.53614573909577734
    translation6 = NXOpen.Point3d(-158.44543701236196, -83.601848571426032, -6.0272441379570871)
    workPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix6, translation6, 0.35183649851092341)
    
    origin12 = NXOpen.Point3d(-8.6942951082182915, 55.071410935121627, -27.655953660513063)
    workPart.ModelingViews.WorkView.SetOrigin(origin12)
    
    origin13 = NXOpen.Point3d(-8.6942951082182915, 55.071410935121627, -27.655953660513063)
    workPart.ModelingViews.WorkView.SetOrigin(origin13)
    
    # ----------------------------------------------
    #   Menu: Orient View->Trimetric
    # ----------------------------------------------
    workPart.ModelingViews.WorkView.Orient(NXOpen.View.Canned.Trimetric, NXOpen.View.ScaleAdjustment.Fit)
    
    # ----------------------------------------------
    #   Menu: Orient View->Right
    # ----------------------------------------------
    workPart.ModelingViews.WorkView.Orient(NXOpen.View.Canned.Right, NXOpen.View.ScaleAdjustment.Fit)
    
    # ----------------------------------------------
    #   Menu: Orient View->Top
    # ----------------------------------------------
    workPart.ModelingViews.WorkView.Orient(NXOpen.View.Canned.Top, NXOpen.View.ScaleAdjustment.Fit)
    
    # ----------------------------------------------
    #   Menu: Orient View->Front
    # ----------------------------------------------
    workPart.ModelingViews.WorkView.Orient(NXOpen.View.Canned.Front, NXOpen.View.ScaleAdjustment.Fit)
    
    # ----------------------------------------------
    #   Menu: Orient View->Right
    # ----------------------------------------------
    workPart.ModelingViews.WorkView.Orient(NXOpen.View.Canned.Right, NXOpen.View.ScaleAdjustment.Fit)
    
    # ----------------------------------------------
    #   Menu: Orient View->Right
    # ----------------------------------------------
    workPart.ModelingViews.WorkView.Orient(NXOpen.View.Canned.Right, NXOpen.View.ScaleAdjustment.Fit)
    
    # ----------------------------------------------
    #   Menu: Orient View->Top
    # ----------------------------------------------
    workPart.ModelingViews.WorkView.Orient(NXOpen.View.Canned.Top, NXOpen.View.ScaleAdjustment.Fit)
    
    # ----------------------------------------------
    #   Menu: Orient View->Front
    # ----------------------------------------------
    workPart.ModelingViews.WorkView.Orient(NXOpen.View.Canned.Front, NXOpen.View.ScaleAdjustment.Fit)
    
    # ----------------------------------------------
    #   Menu: Tools->Journal->Stop Recording
    # ----------------------------------------------
    
if __name__ == '__main__':
    main()