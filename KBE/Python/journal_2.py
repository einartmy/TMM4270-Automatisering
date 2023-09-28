# NX 2206
# Journal created by mbergst on Tue Sep 19 14:06:46 2023 W. Europe Daylight Time
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
    
    sketchAlongPathBuilder1.PlaneLocation.Expression.SetFormula("0")
    
    theSession.SetUndoMarkName(markId3, "Create Sketch Dialog")
    
    simpleSketchInPlaceBuilder1.UseWorkPartOrigin = False
    
    coordinates1 = NXOpen.Point3d(0.0, 0.0, 0.0)
    point1 = workPart.Points.CreatePoint(coordinates1)
    
    nErrs1 = theSession.UpdateManager.AddToDeleteList(point1)
    
    markId4 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Create Sketch")
    
    theSession.DeleteUndoMark(markId4, None)
    
    markId5 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Create Sketch")
    
    origin2 = NXOpen.Point3d(0.0, 0.0, 0.0)
    vector1 = NXOpen.Vector3d(1.0, 0.0, 0.0)
    direction1 = workPart.Directions.CreateDirection(origin2, vector1, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    coordinates2 = NXOpen.Point3d(0.0, 0.0, 0.0)
    point2 = workPart.Points.CreatePoint(coordinates2)
    
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
    
    xform1 = workPart.Xforms.CreateXformByPlaneXDirPoint(plane2, direction1, point2, NXOpen.SmartObject.UpdateOption.WithinModeling, 1.0, False, False)
    
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
    
    nErrs2 = theSession.UpdateManager.DoUpdate(markId6)
    
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
    
    rotMatrix1.Xx = 0.94105988465415091
    rotMatrix1.Xy = 0.022261279871261162
    rotMatrix1.Xz = 0.33750663536175018
    rotMatrix1.Yx = 0.014321285062488398
    rotMatrix1.Yy = 0.99431461532112919
    rotMatrix1.Yz = -0.10551467458583041
    rotMatrix1.Zx = -0.33793667200952754
    rotMatrix1.Zy = 0.10412915623055884
    rotMatrix1.Zz = 0.93539078706914669
    translation1 = NXOpen.Point3d(-16.612937684080947, 4.0732380576746436, -92.135892961801687)
    workPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix1, translation1, 0.2785013480417885)
    
    rotMatrix2 = NXOpen.Matrix3x3()
    
    rotMatrix2.Xx = 0.99991772797824496
    rotMatrix2.Xy = -0.011539375184042612
    rotMatrix2.Xz = 0.0056017939256171791
    rotMatrix2.Yx = 0.012024381975874261
    rotMatrix2.Yy = 0.99530053450371547
    rotMatrix2.Yz = -0.096084651504372898
    rotMatrix2.Zx = -0.0044667116452097831
    rotMatrix2.Zy = 0.096144104535745831
    rotMatrix2.Zz = 0.9953574029714648
    translation2 = NXOpen.Point3d(-16.626220577242176, 4.0737564171077807, -92.211149641384864)
    workPart.ModelingViews.WorkView.SetRotationTranslationScale(rotMatrix2, translation2, 0.2785013480417885)
    
    theSession.SetUndoMarkVisibility(markId9, "Curve", NXOpen.Session.MarkVisibility.Visible)
    
    nXMatrix1 = theSession.ActiveSketch.Orientation
    
    center1 = NXOpen.Point3d(0.0, 0.0, 0.0)
    arc1 = workPart.Curves.CreateArc(center1, nXMatrix1, 212.40354378049722, 0.0, ( 360.0 * math.pi/180.0 ))
    
    theSession.ActiveSketch.AddGeometry(arc1, NXOpen.Sketch.InferConstraintsOption.InferNoConstraints)
    
    theSession.ActiveSketch.Update()
    
    sketchFindMovableObjectsBuilder2 = workPart.Sketches.CreateFindMovableObjectsBuilder()
    
    nXObject3 = sketchFindMovableObjectsBuilder2.Commit()
    
    sketchFindMovableObjectsBuilder2.Destroy()
    
    markId10 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Sketch Drag")
    
    sketchDragGeometryBuilder1 = workPart.Sketches.CreateDragGeometryBuilder()
    
    sketchDragGeometryBuilder1.SnapRadius = 25.080668546537577
    
    sketchDragGeometryBuilder1.SplineLinearScale = False
    
    snapgeometry1 = NXOpen.Sketch.SketchGeometry()
    
    snapgeometry1.Geometry = arc1
    snapgeometry1.PointType = NXOpen.Sketch.PointType.NotSet
    snapgeometry1.PointIndex = 0
    sketchDragGeometryBuilder1.SnapGeometry = snapgeometry1
    
    dragobjects1 = [None] * 1 
    dragobjects1[0] = NXOpen.Sketch.SketchGeometry()
    dragobjects1[0].Geometry = arc1
    dragobjects1[0].PointType = NXOpen.Sketch.PointType.NotSet
    dragobjects1[0].PointIndex = 0
    sketchDragGeometryBuilder1.SetDragGeometry(dragobjects1)
    
    initialposition1 = NXOpen.Point3d(-193.23066685530935, 92.260793735080924, 0.0)
    sketchDragGeometryBuilder1.InitializeDrag(initialposition1)
    
    newposition1 = NXOpen.Point3d(-209.36916079321693, 93.410276428695354, 0.0)
    sketchDragGeometryBuilder1.DragToPoint(newposition1)
    
    nXObject4 = sketchDragGeometryBuilder1.Commit()
    
    sketchDragGeometryBuilder1.Destroy()
    
    theSession.ActiveSketch.Update()
    
    sketchFindMovableObjectsBuilder3 = workPart.Sketches.CreateFindMovableObjectsBuilder()
    
    nXObject5 = sketchFindMovableObjectsBuilder3.Commit()
    
    sketchFindMovableObjectsBuilder3.Destroy()
    
    # ----------------------------------------------
    #   Menu: Edit->Undo
    # ----------------------------------------------
    marksRecycled1, undoUnavailable1 = theSession.UndoLastNVisibleMarks(1)
    
    # ----------------------------------------------
    #   Menu: Edit->Undo
    # ----------------------------------------------
    marksRecycled2, undoUnavailable2 = theSession.UndoLastNVisibleMarks(1)
    
    theSession.ActiveSketch.UpdateDimensionDisplay()
    
    theSession.ActiveSketch.UpdateDimensionDisplay()
    
    # ----------------------------------------------
    #   Menu: Insert->Curve->Circle...
    # ----------------------------------------------
    markId11 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Profile short list")
    
    markId12 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Curve")
    
    theSession.SetUndoMarkVisibility(markId12, "Curve", NXOpen.Session.MarkVisibility.Visible)
    
    nXMatrix2 = theSession.ActiveSketch.Orientation
    
    center2 = NXOpen.Point3d(0.0, 0.0, 0.0)
    arc2 = workPart.Curves.CreateArc(center2, nXMatrix2, 237.91590318762402, 0.0, ( 360.0 * math.pi/180.0 ))
    
    theSession.ActiveSketch.AddGeometry(arc2, NXOpen.Sketch.InferConstraintsOption.InferNoConstraints)
    
    theSession.ActiveSketch.Update()
    
    sketchFindMovableObjectsBuilder4 = workPart.Sketches.CreateFindMovableObjectsBuilder()
    
    nXObject6 = sketchFindMovableObjectsBuilder4.Commit()
    
    sketchFindMovableObjectsBuilder4.Destroy()
    
    # ----------------------------------------------
    #   Menu: Task->Finish Sketch
    # ----------------------------------------------
    sketchWorkRegionBuilder1 = workPart.Sketches.CreateWorkRegionBuilder()
    
    sketchWorkRegionBuilder1.Scope = NXOpen.SketchWorkRegionBuilder.ScopeType.EntireSketch
    
    nXObject7 = sketchWorkRegionBuilder1.Commit()
    
    sketchWorkRegionBuilder1.Destroy()
    
    theSession.ActiveSketch.CalculateStatus()
    
    theSession.Preferences.Sketch.SectionView = False
    
    markId13 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Deactivate Sketch")
    
    theSession.ActiveSketch.Deactivate(NXOpen.Sketch.ViewReorient.TrueValue, NXOpen.Sketch.UpdateLevel.Model)
    
    theSession.DeleteUndoMarksSetInTaskEnvironment()
    
    theSession.EndTaskEnvironment()
    
    # ----------------------------------------------
    #   Menu: Insert->Design Feature->Extrude...
    # ----------------------------------------------
    markId14 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")
    
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
    
    extrudeBuilder1.Limits.EndExtend.Value.SetFormula("375")
    
    extrudeBuilder1.Draft.FrontDraftAngle.SetFormula("2")
    
    extrudeBuilder1.Draft.BackDraftAngle.SetFormula("2")
    
    extrudeBuilder1.Offset.StartOffset.SetFormula("0")
    
    extrudeBuilder1.Offset.EndOffset.SetFormula("5")
    
    smartVolumeProfileBuilder1 = extrudeBuilder1.SmartVolumeProfile
    
    smartVolumeProfileBuilder1.OpenProfileSmartVolumeOption = False
    
    smartVolumeProfileBuilder1.CloseProfileRule = NXOpen.GeometricUtilities.SmartVolumeProfileBuilder.CloseProfileRuleType.Fci
    
    theSession.SetUndoMarkName(markId14, "Extrude Dialog")
    
    section1.DistanceTolerance = 0.01
    
    section1.ChainingTolerance = 0.0094999999999999998
    
    section1.SetAllowedEntityTypes(NXOpen.Section.AllowTypes.OnlyCurves)
    
    markId15 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, None)
    
    selectionIntentRuleOptions1 = workPart.ScRuleFactory.CreateRuleOptions()
    
    selectionIntentRuleOptions1.SetSelectedFromInactive(False)
    
    curves1 = [NXOpen.ICurve.Null] * 1 
    curves1[0] = arc2
    seedPoint1 = NXOpen.Point3d(-31.333935992371607, -15.613156941263501, 0.0)
    regionBoundaryRule1 = workPart.ScRuleFactory.CreateRuleRegionBoundary(sketch1, curves1, seedPoint1, 0.01, selectionIntentRuleOptions1)
    
    selectionIntentRuleOptions1.Dispose()
    section1.AllowSelfIntersection(True)
    
    section1.AllowDegenerateCurves(False)
    
    rules1 = [None] * 1 
    rules1[0] = regionBoundaryRule1
    helpPoint1 = NXOpen.Point3d(0.0, 0.0, 0.0)
    section1.AddToSection(rules1, NXOpen.NXObject.Null, NXOpen.NXObject.Null, NXOpen.NXObject.Null, helpPoint1, NXOpen.Section.Mode.Create, False)
    
    theSession.DeleteUndoMark(markId15, None)
    
    markId16 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "section mark")
    
    markId17 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, None)
    
    theSession.DeleteUndoMark(markId17, None)
    
    direction2 = workPart.Directions.CreateDirection(sketch1, NXOpen.Sense.Forward, NXOpen.SmartObject.UpdateOption.WithinModeling)
    
    extrudeBuilder1.Direction = direction2
    
    extrudeBuilder1.BooleanOperation.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Create
    
    targetBodies2 = [NXOpen.Body.Null] * 1 
    targetBodies2[0] = NXOpen.Body.Null
    extrudeBuilder1.BooleanOperation.SetTargetBodies(targetBodies2)
    
    targetBodies3 = []
    extrudeBuilder1.BooleanOperation.SetTargetBodies(targetBodies3)
    
    theSession.DeleteUndoMark(markId16, None)
    
    extrudeBuilder1.BooleanOperation.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Create
    
    targetBodies4 = [NXOpen.Body.Null] * 1 
    targetBodies4[0] = NXOpen.Body.Null
    extrudeBuilder1.BooleanOperation.SetTargetBodies(targetBodies4)
    
    targetBodies5 = []
    extrudeBuilder1.BooleanOperation.SetTargetBodies(targetBodies5)
    
    markId18 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Extrude")
    
    theSession.DeleteUndoMark(markId18, None)
    
    markId19 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Extrude")
    
    extrudeBuilder1.ParentFeatureInternal = False
    
    feature2 = extrudeBuilder1.CommitFeature()
    
    theSession.DeleteUndoMark(markId19, None)
    
    theSession.SetUndoMarkName(markId14, "Extrude")
    
    expression4 = extrudeBuilder1.Limits.StartExtend.Value
    expression5 = extrudeBuilder1.Limits.EndExtend.Value
    extrudeBuilder1.Destroy()
    
    workPart.Expressions.Delete(expression3)
    
    # ----------------------------------------------
    #   Menu: Tools->Journal->Stop Recording
    # ----------------------------------------------
    
if __name__ == '__main__':
    main()