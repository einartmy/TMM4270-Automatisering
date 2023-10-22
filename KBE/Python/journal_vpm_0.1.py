# NX 2206
# Journal created by mbergst on Sun Oct 22 13:59:38 2023 W. Europe Daylight Time
#
import math
import NXOpen
import NXOpen.Assemblies
import NXOpen.CAE
import NXOpen.Features
import NXOpen.GeometricUtilities
import NXOpen.MenuBar
import NXOpen.Motion
def main() : 

    theSession  = NXOpen.Session.GetSession()
    workPart = theSession.Parts.Work
    displayPart = theSession.Parts.Display
    # ----------------------------------------------
    #   Menu: Tools->Journal->Play...
    # ----------------------------------------------
    part1 = theSession.Parts.Work
    
    cylinderBuilder1 = workPart.Features.CreateCylinderBuilder(NXOpen.Features.Feature.Null)
    
    expression1 = cylinderBuilder1.Diameter
    
    expression1.RightHandSide = "121.99999999999999"
    
    expression2 = cylinderBuilder1.Height
    
    expression2.RightHandSide = "121.99999999999999"
    
    origin1 = NXOpen.Point3d(0.0, 0.0, 0.0)
    cylinderBuilder1.Origin = origin1
    
    vector1 = NXOpen.Vector3d(0.0, 0.0, 1.0)
    cylinderBuilder1.Direction = vector1
    
    booleanOperation1 = cylinderBuilder1.BooleanOption
    
    booleanOperation1.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Create
    
    nXObject1 = cylinderBuilder1.Commit()
    
    cylinder1 = nXObject1
    bodies1 = cylinder1.GetBodies()
    
    cylinderBuilder1.Destroy()
    
    part2 = theSession.Parts.Work
    
    cylinderBuilder2 = workPart.Features.CreateCylinderBuilder(NXOpen.Features.Feature.Null)
    
    expression3 = cylinderBuilder2.Diameter
    
    expression3.RightHandSide = "12.2"
    
    expression4 = cylinderBuilder2.Height
    
    expression4.RightHandSide = "121.99999999999999"
    
    origin2 = NXOpen.Point3d(60.999999999999993, 0.0, 0.0)
    cylinderBuilder2.Origin = origin2
    
    vector2 = NXOpen.Vector3d(0.0, 0.0, 1.0)
    cylinderBuilder2.Direction = vector2
    
    booleanOperation2 = cylinderBuilder2.BooleanOption
    
    booleanOperation2.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Create
    
    nXObject2 = cylinderBuilder2.Commit()
    
    cylinder2 = nXObject2
    bodies2 = cylinder2.GetBodies()
    
    cylinderBuilder2.Destroy()
    
    part3 = theSession.Parts.Work
    
    booleanBuilder1 = workPart.Features.CreateBooleanBuilder(NXOpen.Features.BooleanFeature.Null)
    
    booleanBuilder1.Target = bodies1[0]
    
    booleanBuilder1.Tool = bodies2[0]
    
    booleanBuilder1.Operation = NXOpen.Features.Feature.BooleanType.Subtract
    
    nXObject3 = booleanBuilder1.Commit()
    
    booleanBuilder1.Destroy()
    
    part4 = theSession.Parts.Work
    
    cylinderBuilder3 = workPart.Features.CreateCylinderBuilder(NXOpen.Features.Feature.Null)
    
    expression5 = cylinderBuilder3.Diameter
    
    expression5.RightHandSide = "12.2"
    
    expression6 = cylinderBuilder3.Height
    
    expression6.RightHandSide = "121.99999999999999"
    
    origin3 = NXOpen.Point3d(59.827902104597051, 11.900509642983822, 0.0)
    cylinderBuilder3.Origin = origin3
    
    vector3 = NXOpen.Vector3d(0.0, 0.0, 1.0)
    cylinderBuilder3.Direction = vector3
    
    booleanOperation3 = cylinderBuilder3.BooleanOption
    
    booleanOperation3.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Create
    
    nXObject4 = cylinderBuilder3.Commit()
    
    cylinder3 = nXObject4
    bodies3 = cylinder3.GetBodies()
    
    cylinderBuilder3.Destroy()
    
    part5 = theSession.Parts.Work
    
    booleanBuilder2 = workPart.Features.CreateBooleanBuilderUsingCollector(NXOpen.Features.BooleanFeature.Null)
    
    booleanBuilder2.Target = bodies1[0]
    
    booleanBuilder2.Tool = bodies3[0]
    
    booleanBuilder2.Operation = NXOpen.Features.Feature.BooleanType.Unite
    
    nXObject5 = booleanBuilder2.Commit()
    
    booleanBuilder2.Destroy()
    
    part6 = theSession.Parts.Work
    
    cylinderBuilder4 = workPart.Features.CreateCylinderBuilder(NXOpen.Features.Feature.Null)
    
    expression7 = cylinderBuilder4.Diameter
    
    expression7.RightHandSide = "12.2"
    
    expression8 = cylinderBuilder4.Height
    
    expression8.RightHandSide = "121.99999999999999"
    
    origin4 = NXOpen.Point3d(56.356651483188486, 23.343689374270475, 0.0)
    cylinderBuilder4.Origin = origin4
    
    vector4 = NXOpen.Vector3d(0.0, 0.0, 1.0)
    cylinderBuilder4.Direction = vector4
    
    booleanOperation4 = cylinderBuilder4.BooleanOption
    
    booleanOperation4.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Create
    
    nXObject6 = cylinderBuilder4.Commit()
    
    cylinder4 = nXObject6
    bodies4 = cylinder4.GetBodies()
    
    cylinderBuilder4.Destroy()
    
    part7 = theSession.Parts.Work
    
    booleanBuilder3 = workPart.Features.CreateBooleanBuilder(NXOpen.Features.BooleanFeature.Null)
    
    booleanBuilder3.Target = bodies1[0]
    
    booleanBuilder3.Tool = bodies4[0]
    
    booleanBuilder3.Operation = NXOpen.Features.Feature.BooleanType.Subtract
    
    nXObject7 = booleanBuilder3.Commit()
    
    booleanBuilder3.Destroy()
    
    part8 = theSession.Parts.Work
    
    cylinderBuilder5 = workPart.Features.CreateCylinderBuilder(NXOpen.Features.Feature.Null)
    
    expression9 = cylinderBuilder5.Diameter
    
    expression9.RightHandSide = "12.2"
    
    expression10 = cylinderBuilder5.Height
    
    expression10.RightHandSide = "121.99999999999999"
    
    origin5 = NXOpen.Point3d(50.719646350455257, 33.889784214195728, 0.0)
    cylinderBuilder5.Origin = origin5
    
    vector5 = NXOpen.Vector3d(0.0, 0.0, 1.0)
    cylinderBuilder5.Direction = vector5
    
    booleanOperation5 = cylinderBuilder5.BooleanOption
    
    booleanOperation5.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Create
    
    nXObject8 = cylinderBuilder5.Commit()
    
    cylinder5 = nXObject8
    bodies5 = cylinder5.GetBodies()
    
    cylinderBuilder5.Destroy()
    
    part9 = theSession.Parts.Work
    
    booleanBuilder4 = workPart.Features.CreateBooleanBuilderUsingCollector(NXOpen.Features.BooleanFeature.Null)
    
    booleanBuilder4.Target = bodies1[0]
    
    booleanBuilder4.Tool = bodies5[0]
    
    booleanBuilder4.Operation = NXOpen.Features.Feature.BooleanType.Unite
    
    nXObject9 = booleanBuilder4.Commit()
    
    booleanBuilder4.Destroy()
    
    part10 = theSession.Parts.Work
    
    cylinderBuilder6 = workPart.Features.CreateCylinderBuilder(NXOpen.Features.Feature.Null)
    
    expression11 = cylinderBuilder6.Diameter
    
    expression11.RightHandSide = "12.2"
    
    expression12 = cylinderBuilder6.Height
    
    expression12.RightHandSide = "121.99999999999999"
    
    origin6 = NXOpen.Point3d(43.133513652379399, 43.133513652379399, 0.0)
    cylinderBuilder6.Origin = origin6
    
    vector6 = NXOpen.Vector3d(0.0, 0.0, 1.0)
    cylinderBuilder6.Direction = vector6
    
    booleanOperation6 = cylinderBuilder6.BooleanOption
    
    booleanOperation6.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Create
    
    nXObject10 = cylinderBuilder6.Commit()
    
    cylinder6 = nXObject10
    bodies6 = cylinder6.GetBodies()
    
    cylinderBuilder6.Destroy()
    
    part11 = theSession.Parts.Work
    
    booleanBuilder5 = workPart.Features.CreateBooleanBuilder(NXOpen.Features.BooleanFeature.Null)
    
    booleanBuilder5.Target = bodies1[0]
    
    booleanBuilder5.Tool = bodies6[0]
    
    booleanBuilder5.Operation = NXOpen.Features.Feature.BooleanType.Subtract
    
    nXObject11 = booleanBuilder5.Commit()
    
    booleanBuilder5.Destroy()
    
    part12 = theSession.Parts.Work
    
    cylinderBuilder7 = workPart.Features.CreateCylinderBuilder(NXOpen.Features.Feature.Null)
    
    expression13 = cylinderBuilder7.Diameter
    
    expression13.RightHandSide = "12.2"
    
    expression14 = cylinderBuilder7.Height
    
    expression14.RightHandSide = "121.99999999999999"
    
    origin7 = NXOpen.Point3d(33.889784214195736, 50.719646350455257, 0.0)
    cylinderBuilder7.Origin = origin7
    
    vector7 = NXOpen.Vector3d(0.0, 0.0, 1.0)
    cylinderBuilder7.Direction = vector7
    
    booleanOperation7 = cylinderBuilder7.BooleanOption
    
    booleanOperation7.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Create
    
    nXObject12 = cylinderBuilder7.Commit()
    
    cylinder7 = nXObject12
    bodies7 = cylinder7.GetBodies()
    
    cylinderBuilder7.Destroy()
    
    part13 = theSession.Parts.Work
    
    booleanBuilder6 = workPart.Features.CreateBooleanBuilderUsingCollector(NXOpen.Features.BooleanFeature.Null)
    
    booleanBuilder6.Target = bodies1[0]
    
    booleanBuilder6.Tool = bodies7[0]
    
    booleanBuilder6.Operation = NXOpen.Features.Feature.BooleanType.Unite
    
    nXObject13 = booleanBuilder6.Commit()
    
    booleanBuilder6.Destroy()
    
    part14 = theSession.Parts.Work
    
    cylinderBuilder8 = workPart.Features.CreateCylinderBuilder(NXOpen.Features.Feature.Null)
    
    expression15 = cylinderBuilder8.Diameter
    
    expression15.RightHandSide = "12.2"
    
    expression16 = cylinderBuilder8.Height
    
    expression16.RightHandSide = "121.99999999999999"
    
    origin8 = NXOpen.Point3d(23.343689374270479, 56.356651483188486, 0.0)
    cylinderBuilder8.Origin = origin8
    
    vector8 = NXOpen.Vector3d(0.0, 0.0, 1.0)
    cylinderBuilder8.Direction = vector8
    
    booleanOperation8 = cylinderBuilder8.BooleanOption
    
    booleanOperation8.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Create
    
    nXObject14 = cylinderBuilder8.Commit()
    
    cylinder8 = nXObject14
    bodies8 = cylinder8.GetBodies()
    
    cylinderBuilder8.Destroy()
    
    part15 = theSession.Parts.Work
    
    booleanBuilder7 = workPart.Features.CreateBooleanBuilder(NXOpen.Features.BooleanFeature.Null)
    
    booleanBuilder7.Target = bodies1[0]
    
    booleanBuilder7.Tool = bodies8[0]
    
    booleanBuilder7.Operation = NXOpen.Features.Feature.BooleanType.Subtract
    
    nXObject15 = booleanBuilder7.Commit()
    
    booleanBuilder7.Destroy()
    
    part16 = theSession.Parts.Work
    
    cylinderBuilder9 = workPart.Features.CreateCylinderBuilder(NXOpen.Features.Feature.Null)
    
    expression17 = cylinderBuilder9.Diameter
    
    expression17.RightHandSide = "12.2"
    
    expression18 = cylinderBuilder9.Height
    
    expression18.RightHandSide = "121.99999999999999"
    
    origin9 = NXOpen.Point3d(11.900509642983828, 59.827902104597051, 0.0)
    cylinderBuilder9.Origin = origin9
    
    vector9 = NXOpen.Vector3d(0.0, 0.0, 1.0)
    cylinderBuilder9.Direction = vector9
    
    booleanOperation9 = cylinderBuilder9.BooleanOption
    
    booleanOperation9.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Create
    
    nXObject16 = cylinderBuilder9.Commit()
    
    cylinder9 = nXObject16
    bodies9 = cylinder9.GetBodies()
    
    cylinderBuilder9.Destroy()
    
    part17 = theSession.Parts.Work
    
    booleanBuilder8 = workPart.Features.CreateBooleanBuilderUsingCollector(NXOpen.Features.BooleanFeature.Null)
    
    booleanBuilder8.Target = bodies1[0]
    
    booleanBuilder8.Tool = bodies9[0]
    
    booleanBuilder8.Operation = NXOpen.Features.Feature.BooleanType.Unite
    
    nXObject17 = booleanBuilder8.Commit()
    
    booleanBuilder8.Destroy()
    
    part18 = theSession.Parts.Work
    
    cylinderBuilder10 = workPart.Features.CreateCylinderBuilder(NXOpen.Features.Feature.Null)
    
    expression19 = cylinderBuilder10.Diameter
    
    expression19.RightHandSide = "12.2"
    
    expression20 = cylinderBuilder10.Height
    
    expression20.RightHandSide = "121.99999999999999"
    
    origin10 = NXOpen.Point3d(3.7351727373994268e-15, 60.999999999999993, 0.0)
    cylinderBuilder10.Origin = origin10
    
    vector10 = NXOpen.Vector3d(0.0, 0.0, 1.0)
    cylinderBuilder10.Direction = vector10
    
    booleanOperation10 = cylinderBuilder10.BooleanOption
    
    booleanOperation10.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Create
    
    nXObject18 = cylinderBuilder10.Commit()
    
    cylinder10 = nXObject18
    bodies10 = cylinder10.GetBodies()
    
    cylinderBuilder10.Destroy()
    
    part19 = theSession.Parts.Work
    
    booleanBuilder9 = workPart.Features.CreateBooleanBuilder(NXOpen.Features.BooleanFeature.Null)
    
    booleanBuilder9.Target = bodies1[0]
    
    booleanBuilder9.Tool = bodies10[0]
    
    booleanBuilder9.Operation = NXOpen.Features.Feature.BooleanType.Subtract
    
    nXObject19 = booleanBuilder9.Commit()
    
    booleanBuilder9.Destroy()
    
    part20 = theSession.Parts.Work
    
    cylinderBuilder11 = workPart.Features.CreateCylinderBuilder(NXOpen.Features.Feature.Null)
    
    expression21 = cylinderBuilder11.Diameter
    
    expression21.RightHandSide = "12.2"
    
    expression22 = cylinderBuilder11.Height
    
    expression22.RightHandSide = "121.99999999999999"
    
    origin11 = NXOpen.Point3d(-11.900509642983819, 59.827902104597051, 0.0)
    cylinderBuilder11.Origin = origin11
    
    vector11 = NXOpen.Vector3d(0.0, 0.0, 1.0)
    cylinderBuilder11.Direction = vector11
    
    booleanOperation11 = cylinderBuilder11.BooleanOption
    
    booleanOperation11.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Create
    
    nXObject20 = cylinderBuilder11.Commit()
    
    cylinder11 = nXObject20
    bodies11 = cylinder11.GetBodies()
    
    cylinderBuilder11.Destroy()
    
    part21 = theSession.Parts.Work
    
    booleanBuilder10 = workPart.Features.CreateBooleanBuilderUsingCollector(NXOpen.Features.BooleanFeature.Null)
    
    booleanBuilder10.Target = bodies1[0]
    
    booleanBuilder10.Tool = bodies11[0]
    
    booleanBuilder10.Operation = NXOpen.Features.Feature.BooleanType.Unite
    
    nXObject21 = booleanBuilder10.Commit()
    
    booleanBuilder10.Destroy()
    
    part22 = theSession.Parts.Work
    
    cylinderBuilder12 = workPart.Features.CreateCylinderBuilder(NXOpen.Features.Feature.Null)
    
    expression23 = cylinderBuilder12.Diameter
    
    expression23.RightHandSide = "12.2"
    
    expression24 = cylinderBuilder12.Height
    
    expression24.RightHandSide = "121.99999999999999"
    
    origin12 = NXOpen.Point3d(-23.343689374270472, 56.356651483188486, 0.0)
    cylinderBuilder12.Origin = origin12
    
    vector12 = NXOpen.Vector3d(0.0, 0.0, 1.0)
    cylinderBuilder12.Direction = vector12
    
    booleanOperation12 = cylinderBuilder12.BooleanOption
    
    booleanOperation12.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Create
    
    nXObject22 = cylinderBuilder12.Commit()
    
    cylinder12 = nXObject22
    bodies12 = cylinder12.GetBodies()
    
    cylinderBuilder12.Destroy()
    
    part23 = theSession.Parts.Work
    
    booleanBuilder11 = workPart.Features.CreateBooleanBuilder(NXOpen.Features.BooleanFeature.Null)
    
    booleanBuilder11.Target = bodies1[0]
    
    booleanBuilder11.Tool = bodies12[0]
    
    booleanBuilder11.Operation = NXOpen.Features.Feature.BooleanType.Subtract
    
    nXObject23 = booleanBuilder11.Commit()
    
    booleanBuilder11.Destroy()
    
    part24 = theSession.Parts.Work
    
    cylinderBuilder13 = workPart.Features.CreateCylinderBuilder(NXOpen.Features.Feature.Null)
    
    expression25 = cylinderBuilder13.Diameter
    
    expression25.RightHandSide = "12.2"
    
    expression26 = cylinderBuilder13.Height
    
    expression26.RightHandSide = "121.99999999999999"
    
    origin13 = NXOpen.Point3d(-33.889784214195714, 50.719646350455257, 0.0)
    cylinderBuilder13.Origin = origin13
    
    vector13 = NXOpen.Vector3d(0.0, 0.0, 1.0)
    cylinderBuilder13.Direction = vector13
    
    booleanOperation13 = cylinderBuilder13.BooleanOption
    
    booleanOperation13.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Create
    
    nXObject24 = cylinderBuilder13.Commit()
    
    cylinder13 = nXObject24
    bodies13 = cylinder13.GetBodies()
    
    cylinderBuilder13.Destroy()
    
    part25 = theSession.Parts.Work
    
    booleanBuilder12 = workPart.Features.CreateBooleanBuilderUsingCollector(NXOpen.Features.BooleanFeature.Null)
    
    booleanBuilder12.Target = bodies1[0]
    
    booleanBuilder12.Tool = bodies13[0]
    
    booleanBuilder12.Operation = NXOpen.Features.Feature.BooleanType.Unite
    
    nXObject25 = booleanBuilder12.Commit()
    
    booleanBuilder12.Destroy()
    
    part26 = theSession.Parts.Work
    
    cylinderBuilder14 = workPart.Features.CreateCylinderBuilder(NXOpen.Features.Feature.Null)
    
    expression27 = cylinderBuilder14.Diameter
    
    expression27.RightHandSide = "12.2"
    
    expression28 = cylinderBuilder14.Height
    
    expression28.RightHandSide = "121.99999999999999"
    
    origin14 = NXOpen.Point3d(-43.133513652379392, 43.133513652379399, 0.0)
    cylinderBuilder14.Origin = origin14
    
    vector14 = NXOpen.Vector3d(0.0, 0.0, 1.0)
    cylinderBuilder14.Direction = vector14
    
    booleanOperation14 = cylinderBuilder14.BooleanOption
    
    booleanOperation14.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Create
    
    nXObject26 = cylinderBuilder14.Commit()
    
    cylinder14 = nXObject26
    bodies14 = cylinder14.GetBodies()
    
    cylinderBuilder14.Destroy()
    
    part27 = theSession.Parts.Work
    
    booleanBuilder13 = workPart.Features.CreateBooleanBuilder(NXOpen.Features.BooleanFeature.Null)
    
    booleanBuilder13.Target = bodies1[0]
    
    booleanBuilder13.Tool = bodies14[0]
    
    booleanBuilder13.Operation = NXOpen.Features.Feature.BooleanType.Subtract
    
    nXObject27 = booleanBuilder13.Commit()
    
    booleanBuilder13.Destroy()
    
    part28 = theSession.Parts.Work
    
    cylinderBuilder15 = workPart.Features.CreateCylinderBuilder(NXOpen.Features.Feature.Null)
    
    expression29 = cylinderBuilder15.Diameter
    
    expression29.RightHandSide = "12.2"
    
    expression30 = cylinderBuilder15.Height
    
    expression30.RightHandSide = "121.99999999999999"
    
    origin15 = NXOpen.Point3d(-50.719646350455257, 33.889784214195728, 0.0)
    cylinderBuilder15.Origin = origin15
    
    vector15 = NXOpen.Vector3d(0.0, 0.0, 1.0)
    cylinderBuilder15.Direction = vector15
    
    booleanOperation15 = cylinderBuilder15.BooleanOption
    
    booleanOperation15.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Create
    
    nXObject28 = cylinderBuilder15.Commit()
    
    cylinder15 = nXObject28
    bodies15 = cylinder15.GetBodies()
    
    cylinderBuilder15.Destroy()
    
    part29 = theSession.Parts.Work
    
    booleanBuilder14 = workPart.Features.CreateBooleanBuilderUsingCollector(NXOpen.Features.BooleanFeature.Null)
    
    booleanBuilder14.Target = bodies1[0]
    
    booleanBuilder14.Tool = bodies15[0]
    
    booleanBuilder14.Operation = NXOpen.Features.Feature.BooleanType.Unite
    
    nXObject29 = booleanBuilder14.Commit()
    
    booleanBuilder14.Destroy()
    
    part30 = theSession.Parts.Work
    
    cylinderBuilder16 = workPart.Features.CreateCylinderBuilder(NXOpen.Features.Feature.Null)
    
    expression31 = cylinderBuilder16.Diameter
    
    expression31.RightHandSide = "12.2"
    
    expression32 = cylinderBuilder16.Height
    
    expression32.RightHandSide = "121.99999999999999"
    
    origin16 = NXOpen.Point3d(-56.356651483188486, 23.343689374270483, 0.0)
    cylinderBuilder16.Origin = origin16
    
    vector16 = NXOpen.Vector3d(0.0, 0.0, 1.0)
    cylinderBuilder16.Direction = vector16
    
    booleanOperation16 = cylinderBuilder16.BooleanOption
    
    booleanOperation16.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Create
    
    nXObject30 = cylinderBuilder16.Commit()
    
    cylinder16 = nXObject30
    bodies16 = cylinder16.GetBodies()
    
    cylinderBuilder16.Destroy()
    
    part31 = theSession.Parts.Work
    
    booleanBuilder15 = workPart.Features.CreateBooleanBuilder(NXOpen.Features.BooleanFeature.Null)
    
    booleanBuilder15.Target = bodies1[0]
    
    booleanBuilder15.Tool = bodies16[0]
    
    booleanBuilder15.Operation = NXOpen.Features.Feature.BooleanType.Subtract
    
    nXObject31 = booleanBuilder15.Commit()
    
    booleanBuilder15.Destroy()
    
    part32 = theSession.Parts.Work
    
    cylinderBuilder17 = workPart.Features.CreateCylinderBuilder(NXOpen.Features.Feature.Null)
    
    expression33 = cylinderBuilder17.Diameter
    
    expression33.RightHandSide = "12.2"
    
    expression34 = cylinderBuilder17.Height
    
    expression34.RightHandSide = "121.99999999999999"
    
    origin17 = NXOpen.Point3d(-59.827902104597051, 11.900509642983844, 0.0)
    cylinderBuilder17.Origin = origin17
    
    vector17 = NXOpen.Vector3d(0.0, 0.0, 1.0)
    cylinderBuilder17.Direction = vector17
    
    booleanOperation17 = cylinderBuilder17.BooleanOption
    
    booleanOperation17.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Create
    
    nXObject32 = cylinderBuilder17.Commit()
    
    cylinder17 = nXObject32
    bodies17 = cylinder17.GetBodies()
    
    cylinderBuilder17.Destroy()
    
    part33 = theSession.Parts.Work
    
    booleanBuilder16 = workPart.Features.CreateBooleanBuilderUsingCollector(NXOpen.Features.BooleanFeature.Null)
    
    booleanBuilder16.Target = bodies1[0]
    
    booleanBuilder16.Tool = bodies17[0]
    
    booleanBuilder16.Operation = NXOpen.Features.Feature.BooleanType.Unite
    
    nXObject33 = booleanBuilder16.Commit()
    
    booleanBuilder16.Destroy()
    
    part34 = theSession.Parts.Work
    
    cylinderBuilder18 = workPart.Features.CreateCylinderBuilder(NXOpen.Features.Feature.Null)
    
    expression35 = cylinderBuilder18.Diameter
    
    expression35.RightHandSide = "12.2"
    
    expression36 = cylinderBuilder18.Height
    
    expression36.RightHandSide = "121.99999999999999"
    
    origin18 = NXOpen.Point3d(-60.999999999999993, 7.4703454747988535e-15, 0.0)
    cylinderBuilder18.Origin = origin18
    
    vector18 = NXOpen.Vector3d(0.0, 0.0, 1.0)
    cylinderBuilder18.Direction = vector18
    
    booleanOperation18 = cylinderBuilder18.BooleanOption
    
    booleanOperation18.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Create
    
    nXObject34 = cylinderBuilder18.Commit()
    
    cylinder18 = nXObject34
    bodies18 = cylinder18.GetBodies()
    
    cylinderBuilder18.Destroy()
    
    part35 = theSession.Parts.Work
    
    booleanBuilder17 = workPart.Features.CreateBooleanBuilder(NXOpen.Features.BooleanFeature.Null)
    
    booleanBuilder17.Target = bodies1[0]
    
    booleanBuilder17.Tool = bodies18[0]
    
    booleanBuilder17.Operation = NXOpen.Features.Feature.BooleanType.Subtract
    
    nXObject35 = booleanBuilder17.Commit()
    
    booleanBuilder17.Destroy()
    
    part36 = theSession.Parts.Work
    
    cylinderBuilder19 = workPart.Features.CreateCylinderBuilder(NXOpen.Features.Feature.Null)
    
    expression37 = cylinderBuilder19.Diameter
    
    expression37.RightHandSide = "12.2"
    
    expression38 = cylinderBuilder19.Height
    
    expression38.RightHandSide = "121.99999999999999"
    
    origin19 = NXOpen.Point3d(-59.827902104597051, -11.900509642983829, 0.0)
    cylinderBuilder19.Origin = origin19
    
    vector19 = NXOpen.Vector3d(0.0, 0.0, 1.0)
    cylinderBuilder19.Direction = vector19
    
    booleanOperation19 = cylinderBuilder19.BooleanOption
    
    booleanOperation19.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Create
    
    nXObject36 = cylinderBuilder19.Commit()
    
    cylinder19 = nXObject36
    bodies19 = cylinder19.GetBodies()
    
    cylinderBuilder19.Destroy()
    
    part37 = theSession.Parts.Work
    
    booleanBuilder18 = workPart.Features.CreateBooleanBuilderUsingCollector(NXOpen.Features.BooleanFeature.Null)
    
    booleanBuilder18.Target = bodies1[0]
    
    booleanBuilder18.Tool = bodies19[0]
    
    booleanBuilder18.Operation = NXOpen.Features.Feature.BooleanType.Unite
    
    nXObject37 = booleanBuilder18.Commit()
    
    booleanBuilder18.Destroy()
    
    part38 = theSession.Parts.Work
    
    cylinderBuilder20 = workPart.Features.CreateCylinderBuilder(NXOpen.Features.Feature.Null)
    
    expression39 = cylinderBuilder20.Diameter
    
    expression39.RightHandSide = "12.2"
    
    expression40 = cylinderBuilder20.Height
    
    expression40.RightHandSide = "121.99999999999999"
    
    origin20 = NXOpen.Point3d(-56.356651483188493, -23.343689374270465, 0.0)
    cylinderBuilder20.Origin = origin20
    
    vector20 = NXOpen.Vector3d(0.0, 0.0, 1.0)
    cylinderBuilder20.Direction = vector20
    
    booleanOperation20 = cylinderBuilder20.BooleanOption
    
    booleanOperation20.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Create
    
    nXObject38 = cylinderBuilder20.Commit()
    
    cylinder20 = nXObject38
    bodies20 = cylinder20.GetBodies()
    
    cylinderBuilder20.Destroy()
    
    part39 = theSession.Parts.Work
    
    booleanBuilder19 = workPart.Features.CreateBooleanBuilder(NXOpen.Features.BooleanFeature.Null)
    
    booleanBuilder19.Target = bodies1[0]
    
    booleanBuilder19.Tool = bodies20[0]
    
    booleanBuilder19.Operation = NXOpen.Features.Feature.BooleanType.Subtract
    
    nXObject39 = booleanBuilder19.Commit()
    
    booleanBuilder19.Destroy()
    
    part40 = theSession.Parts.Work
    
    cylinderBuilder21 = workPart.Features.CreateCylinderBuilder(NXOpen.Features.Feature.Null)
    
    expression41 = cylinderBuilder21.Diameter
    
    expression41.RightHandSide = "12.2"
    
    expression42 = cylinderBuilder21.Height
    
    expression42.RightHandSide = "121.99999999999999"
    
    origin21 = NXOpen.Point3d(-50.719646350455264, -33.889784214195714, 0.0)
    cylinderBuilder21.Origin = origin21
    
    vector21 = NXOpen.Vector3d(0.0, 0.0, 1.0)
    cylinderBuilder21.Direction = vector21
    
    booleanOperation21 = cylinderBuilder21.BooleanOption
    
    booleanOperation21.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Create
    
    nXObject40 = cylinderBuilder21.Commit()
    
    cylinder21 = nXObject40
    bodies21 = cylinder21.GetBodies()
    
    cylinderBuilder21.Destroy()
    
    part41 = theSession.Parts.Work
    
    booleanBuilder20 = workPart.Features.CreateBooleanBuilderUsingCollector(NXOpen.Features.BooleanFeature.Null)
    
    booleanBuilder20.Target = bodies1[0]
    
    booleanBuilder20.Tool = bodies21[0]
    
    booleanBuilder20.Operation = NXOpen.Features.Feature.BooleanType.Unite
    
    nXObject41 = booleanBuilder20.Commit()
    
    booleanBuilder20.Destroy()
    
    part42 = theSession.Parts.Work
    
    cylinderBuilder22 = workPart.Features.CreateCylinderBuilder(NXOpen.Features.Feature.Null)
    
    expression43 = cylinderBuilder22.Diameter
    
    expression43.RightHandSide = "12.2"
    
    expression44 = cylinderBuilder22.Height
    
    expression44.RightHandSide = "121.99999999999999"
    
    origin22 = NXOpen.Point3d(-43.133513652379406, -43.133513652379392, 0.0)
    cylinderBuilder22.Origin = origin22
    
    vector22 = NXOpen.Vector3d(0.0, 0.0, 1.0)
    cylinderBuilder22.Direction = vector22
    
    booleanOperation22 = cylinderBuilder22.BooleanOption
    
    booleanOperation22.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Create
    
    nXObject42 = cylinderBuilder22.Commit()
    
    cylinder22 = nXObject42
    bodies22 = cylinder22.GetBodies()
    
    cylinderBuilder22.Destroy()
    
    part43 = theSession.Parts.Work
    
    booleanBuilder21 = workPart.Features.CreateBooleanBuilder(NXOpen.Features.BooleanFeature.Null)
    
    booleanBuilder21.Target = bodies1[0]
    
    booleanBuilder21.Tool = bodies22[0]
    
    booleanBuilder21.Operation = NXOpen.Features.Feature.BooleanType.Subtract
    
    nXObject43 = booleanBuilder21.Commit()
    
    booleanBuilder21.Destroy()
    
    part44 = theSession.Parts.Work
    
    cylinderBuilder23 = workPart.Features.CreateCylinderBuilder(NXOpen.Features.Feature.Null)
    
    expression45 = cylinderBuilder23.Diameter
    
    expression45.RightHandSide = "12.2"
    
    expression46 = cylinderBuilder23.Height
    
    expression46.RightHandSide = "121.99999999999999"
    
    origin23 = NXOpen.Point3d(-33.889784214195728, -50.719646350455257, 0.0)
    cylinderBuilder23.Origin = origin23
    
    vector23 = NXOpen.Vector3d(0.0, 0.0, 1.0)
    cylinderBuilder23.Direction = vector23
    
    booleanOperation23 = cylinderBuilder23.BooleanOption
    
    booleanOperation23.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Create
    
    nXObject44 = cylinderBuilder23.Commit()
    
    cylinder23 = nXObject44
    bodies23 = cylinder23.GetBodies()
    
    cylinderBuilder23.Destroy()
    
    part45 = theSession.Parts.Work
    
    booleanBuilder22 = workPart.Features.CreateBooleanBuilderUsingCollector(NXOpen.Features.BooleanFeature.Null)
    
    booleanBuilder22.Target = bodies1[0]
    
    booleanBuilder22.Tool = bodies23[0]
    
    booleanBuilder22.Operation = NXOpen.Features.Feature.BooleanType.Unite
    
    nXObject45 = booleanBuilder22.Commit()
    
    booleanBuilder22.Destroy()
    
    part46 = theSession.Parts.Work
    
    cylinderBuilder24 = workPart.Features.CreateCylinderBuilder(NXOpen.Features.Feature.Null)
    
    expression47 = cylinderBuilder24.Diameter
    
    expression47.RightHandSide = "12.2"
    
    expression48 = cylinderBuilder24.Height
    
    expression48.RightHandSide = "121.99999999999999"
    
    origin24 = NXOpen.Point3d(-23.343689374270507, -56.356651483188472, 0.0)
    cylinderBuilder24.Origin = origin24
    
    vector24 = NXOpen.Vector3d(0.0, 0.0, 1.0)
    cylinderBuilder24.Direction = vector24
    
    booleanOperation24 = cylinderBuilder24.BooleanOption
    
    booleanOperation24.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Create
    
    nXObject46 = cylinderBuilder24.Commit()
    
    cylinder24 = nXObject46
    bodies24 = cylinder24.GetBodies()
    
    cylinderBuilder24.Destroy()
    
    part47 = theSession.Parts.Work
    
    booleanBuilder23 = workPart.Features.CreateBooleanBuilder(NXOpen.Features.BooleanFeature.Null)
    
    booleanBuilder23.Target = bodies1[0]
    
    booleanBuilder23.Tool = bodies24[0]
    
    booleanBuilder23.Operation = NXOpen.Features.Feature.BooleanType.Subtract
    
    nXObject47 = booleanBuilder23.Commit()
    
    booleanBuilder23.Destroy()
    
    part48 = theSession.Parts.Work
    
    cylinderBuilder25 = workPart.Features.CreateCylinderBuilder(NXOpen.Features.Feature.Null)
    
    expression49 = cylinderBuilder25.Diameter
    
    expression49.RightHandSide = "12.2"
    
    expression50 = cylinderBuilder25.Height
    
    expression50.RightHandSide = "121.99999999999999"
    
    origin25 = NXOpen.Point3d(-11.900509642983847, -59.827902104597044, 0.0)
    cylinderBuilder25.Origin = origin25
    
    vector25 = NXOpen.Vector3d(0.0, 0.0, 1.0)
    cylinderBuilder25.Direction = vector25
    
    booleanOperation25 = cylinderBuilder25.BooleanOption
    
    booleanOperation25.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Create
    
    nXObject48 = cylinderBuilder25.Commit()
    
    cylinder25 = nXObject48
    bodies25 = cylinder25.GetBodies()
    
    cylinderBuilder25.Destroy()
    
    part49 = theSession.Parts.Work
    
    booleanBuilder24 = workPart.Features.CreateBooleanBuilderUsingCollector(NXOpen.Features.BooleanFeature.Null)
    
    booleanBuilder24.Target = bodies1[0]
    
    booleanBuilder24.Tool = bodies25[0]
    
    booleanBuilder24.Operation = NXOpen.Features.Feature.BooleanType.Unite
    
    nXObject49 = booleanBuilder24.Commit()
    
    booleanBuilder24.Destroy()
    
    part50 = theSession.Parts.Work
    
    cylinderBuilder26 = workPart.Features.CreateCylinderBuilder(NXOpen.Features.Feature.Null)
    
    expression51 = cylinderBuilder26.Diameter
    
    expression51.RightHandSide = "12.2"
    
    expression52 = cylinderBuilder26.Height
    
    expression52.RightHandSide = "121.99999999999999"
    
    origin26 = NXOpen.Point3d(-1.120551821219828e-14, -60.999999999999993, 0.0)
    cylinderBuilder26.Origin = origin26
    
    vector26 = NXOpen.Vector3d(0.0, 0.0, 1.0)
    cylinderBuilder26.Direction = vector26
    
    booleanOperation26 = cylinderBuilder26.BooleanOption
    
    booleanOperation26.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Create
    
    nXObject50 = cylinderBuilder26.Commit()
    
    cylinder26 = nXObject50
    bodies26 = cylinder26.GetBodies()
    
    cylinderBuilder26.Destroy()
    
    part51 = theSession.Parts.Work
    
    booleanBuilder25 = workPart.Features.CreateBooleanBuilder(NXOpen.Features.BooleanFeature.Null)
    
    booleanBuilder25.Target = bodies1[0]
    
    booleanBuilder25.Tool = bodies26[0]
    
    booleanBuilder25.Operation = NXOpen.Features.Feature.BooleanType.Subtract
    
    nXObject51 = booleanBuilder25.Commit()
    
    booleanBuilder25.Destroy()
    
    part52 = theSession.Parts.Work
    
    cylinderBuilder27 = workPart.Features.CreateCylinderBuilder(NXOpen.Features.Feature.Null)
    
    expression53 = cylinderBuilder27.Diameter
    
    expression53.RightHandSide = "12.2"
    
    expression54 = cylinderBuilder27.Height
    
    expression54.RightHandSide = "121.99999999999999"
    
    origin27 = NXOpen.Point3d(11.900509642983826, -59.827902104597051, 0.0)
    cylinderBuilder27.Origin = origin27
    
    vector27 = NXOpen.Vector3d(0.0, 0.0, 1.0)
    cylinderBuilder27.Direction = vector27
    
    booleanOperation27 = cylinderBuilder27.BooleanOption
    
    booleanOperation27.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Create
    
    nXObject52 = cylinderBuilder27.Commit()
    
    cylinder27 = nXObject52
    bodies27 = cylinder27.GetBodies()
    
    cylinderBuilder27.Destroy()
    
    part53 = theSession.Parts.Work
    
    booleanBuilder26 = workPart.Features.CreateBooleanBuilderUsingCollector(NXOpen.Features.BooleanFeature.Null)
    
    booleanBuilder26.Target = bodies1[0]
    
    booleanBuilder26.Tool = bodies27[0]
    
    booleanBuilder26.Operation = NXOpen.Features.Feature.BooleanType.Unite
    
    nXObject53 = booleanBuilder26.Commit()
    
    booleanBuilder26.Destroy()
    
    part54 = theSession.Parts.Work
    
    cylinderBuilder28 = workPart.Features.CreateCylinderBuilder(NXOpen.Features.Feature.Null)
    
    expression55 = cylinderBuilder28.Diameter
    
    expression55.RightHandSide = "12.2"
    
    expression56 = cylinderBuilder28.Height
    
    expression56.RightHandSide = "121.99999999999999"
    
    origin28 = NXOpen.Point3d(23.343689374270486, -56.356651483188479, 0.0)
    cylinderBuilder28.Origin = origin28
    
    vector28 = NXOpen.Vector3d(0.0, 0.0, 1.0)
    cylinderBuilder28.Direction = vector28
    
    booleanOperation28 = cylinderBuilder28.BooleanOption
    
    booleanOperation28.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Create
    
    nXObject54 = cylinderBuilder28.Commit()
    
    cylinder28 = nXObject54
    bodies28 = cylinder28.GetBodies()
    
    cylinderBuilder28.Destroy()
    
    part55 = theSession.Parts.Work
    
    booleanBuilder27 = workPart.Features.CreateBooleanBuilder(NXOpen.Features.BooleanFeature.Null)
    
    booleanBuilder27.Target = bodies1[0]
    
    booleanBuilder27.Tool = bodies28[0]
    
    booleanBuilder27.Operation = NXOpen.Features.Feature.BooleanType.Subtract
    
    nXObject55 = booleanBuilder27.Commit()
    
    booleanBuilder27.Destroy()
    
    part56 = theSession.Parts.Work
    
    cylinderBuilder29 = workPart.Features.CreateCylinderBuilder(NXOpen.Features.Feature.Null)
    
    expression57 = cylinderBuilder29.Diameter
    
    expression57.RightHandSide = "12.2"
    
    expression58 = cylinderBuilder29.Height
    
    expression58.RightHandSide = "121.99999999999999"
    
    origin29 = NXOpen.Point3d(33.889784214195707, -50.719646350455264, 0.0)
    cylinderBuilder29.Origin = origin29
    
    vector29 = NXOpen.Vector3d(0.0, 0.0, 1.0)
    cylinderBuilder29.Direction = vector29
    
    booleanOperation29 = cylinderBuilder29.BooleanOption
    
    booleanOperation29.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Create
    
    nXObject56 = cylinderBuilder29.Commit()
    
    cylinder29 = nXObject56
    bodies29 = cylinder29.GetBodies()
    
    cylinderBuilder29.Destroy()
    
    part57 = theSession.Parts.Work
    
    booleanBuilder28 = workPart.Features.CreateBooleanBuilderUsingCollector(NXOpen.Features.BooleanFeature.Null)
    
    booleanBuilder28.Target = bodies1[0]
    
    booleanBuilder28.Tool = bodies29[0]
    
    booleanBuilder28.Operation = NXOpen.Features.Feature.BooleanType.Unite
    
    nXObject57 = booleanBuilder28.Commit()
    
    booleanBuilder28.Destroy()
    
    part58 = theSession.Parts.Work
    
    cylinderBuilder30 = workPart.Features.CreateCylinderBuilder(NXOpen.Features.Feature.Null)
    
    expression59 = cylinderBuilder30.Diameter
    
    expression59.RightHandSide = "12.2"
    
    expression60 = cylinderBuilder30.Height
    
    expression60.RightHandSide = "121.99999999999999"
    
    origin30 = NXOpen.Point3d(43.133513652379385, -43.133513652379406, 0.0)
    cylinderBuilder30.Origin = origin30
    
    vector30 = NXOpen.Vector3d(0.0, 0.0, 1.0)
    cylinderBuilder30.Direction = vector30
    
    booleanOperation30 = cylinderBuilder30.BooleanOption
    
    booleanOperation30.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Create
    
    nXObject58 = cylinderBuilder30.Commit()
    
    cylinder30 = nXObject58
    bodies30 = cylinder30.GetBodies()
    
    cylinderBuilder30.Destroy()
    
    part59 = theSession.Parts.Work
    
    booleanBuilder29 = workPart.Features.CreateBooleanBuilder(NXOpen.Features.BooleanFeature.Null)
    
    booleanBuilder29.Target = bodies1[0]
    
    booleanBuilder29.Tool = bodies30[0]
    
    booleanBuilder29.Operation = NXOpen.Features.Feature.BooleanType.Subtract
    
    nXObject59 = booleanBuilder29.Commit()
    
    booleanBuilder29.Destroy()
    
    part60 = theSession.Parts.Work
    
    cylinderBuilder31 = workPart.Features.CreateCylinderBuilder(NXOpen.Features.Feature.Null)
    
    expression61 = cylinderBuilder31.Diameter
    
    expression61.RightHandSide = "12.2"
    
    expression62 = cylinderBuilder31.Height
    
    expression62.RightHandSide = "121.99999999999999"
    
    origin31 = NXOpen.Point3d(50.719646350455257, -33.889784214195728, 0.0)
    cylinderBuilder31.Origin = origin31
    
    vector31 = NXOpen.Vector3d(0.0, 0.0, 1.0)
    cylinderBuilder31.Direction = vector31
    
    booleanOperation31 = cylinderBuilder31.BooleanOption
    
    booleanOperation31.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Create
    
    nXObject60 = cylinderBuilder31.Commit()
    
    cylinder31 = nXObject60
    bodies31 = cylinder31.GetBodies()
    
    cylinderBuilder31.Destroy()
    
    part61 = theSession.Parts.Work
    
    booleanBuilder30 = workPart.Features.CreateBooleanBuilderUsingCollector(NXOpen.Features.BooleanFeature.Null)
    
    booleanBuilder30.Target = bodies1[0]
    
    booleanBuilder30.Tool = bodies31[0]
    
    booleanBuilder30.Operation = NXOpen.Features.Feature.BooleanType.Unite
    
    nXObject61 = booleanBuilder30.Commit()
    
    booleanBuilder30.Destroy()
    
    part62 = theSession.Parts.Work
    
    cylinderBuilder32 = workPart.Features.CreateCylinderBuilder(NXOpen.Features.Feature.Null)
    
    expression63 = cylinderBuilder32.Diameter
    
    expression63.RightHandSide = "12.2"
    
    expression64 = cylinderBuilder32.Height
    
    expression64.RightHandSide = "121.99999999999999"
    
    origin32 = NXOpen.Point3d(56.356651483188472, -23.343689374270511, 0.0)
    cylinderBuilder32.Origin = origin32
    
    vector32 = NXOpen.Vector3d(0.0, 0.0, 1.0)
    cylinderBuilder32.Direction = vector32
    
    booleanOperation32 = cylinderBuilder32.BooleanOption
    
    booleanOperation32.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Create
    
    nXObject62 = cylinderBuilder32.Commit()
    
    cylinder32 = nXObject62
    bodies32 = cylinder32.GetBodies()
    
    cylinderBuilder32.Destroy()
    
    part63 = theSession.Parts.Work
    
    booleanBuilder31 = workPart.Features.CreateBooleanBuilder(NXOpen.Features.BooleanFeature.Null)
    
    booleanBuilder31.Target = bodies1[0]
    
    booleanBuilder31.Tool = bodies32[0]
    
    booleanBuilder31.Operation = NXOpen.Features.Feature.BooleanType.Subtract
    
    nXObject63 = booleanBuilder31.Commit()
    
    booleanBuilder31.Destroy()
    
    part64 = theSession.Parts.Work
    
    cylinderBuilder33 = workPart.Features.CreateCylinderBuilder(NXOpen.Features.Feature.Null)
    
    expression65 = cylinderBuilder33.Diameter
    
    expression65.RightHandSide = "12.2"
    
    expression66 = cylinderBuilder33.Height
    
    expression66.RightHandSide = "121.99999999999999"
    
    origin33 = NXOpen.Point3d(59.827902104597044, -11.900509642983851, 0.0)
    cylinderBuilder33.Origin = origin33
    
    vector33 = NXOpen.Vector3d(0.0, 0.0, 1.0)
    cylinderBuilder33.Direction = vector33
    
    booleanOperation33 = cylinderBuilder33.BooleanOption
    
    booleanOperation33.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Create
    
    nXObject64 = cylinderBuilder33.Commit()
    
    cylinder33 = nXObject64
    bodies33 = cylinder33.GetBodies()
    
    cylinderBuilder33.Destroy()
    
    part65 = theSession.Parts.Work
    
    booleanBuilder32 = workPart.Features.CreateBooleanBuilderUsingCollector(NXOpen.Features.BooleanFeature.Null)
    
    booleanBuilder32.Target = bodies1[0]
    
    booleanBuilder32.Tool = bodies33[0]
    
    booleanBuilder32.Operation = NXOpen.Features.Feature.BooleanType.Unite
    
    nXObject65 = booleanBuilder32.Commit()
    
    booleanBuilder32.Destroy()
    
    part66 = theSession.Parts.Work
    
    cylinderBuilder34 = workPart.Features.CreateCylinderBuilder(NXOpen.Features.Feature.Null)
    
    expression67 = cylinderBuilder34.Diameter
    
    expression67.RightHandSide = "4.066666666666666"
    
    expression68 = cylinderBuilder34.Height
    
    expression68.RightHandSide = "121.99999999999999"
    
    origin34 = NXOpen.Point3d(0.0, 0.0, 0.0)
    cylinderBuilder34.Origin = origin34
    
    vector34 = NXOpen.Vector3d(0.0, 0.0, 1.0)
    cylinderBuilder34.Direction = vector34
    
    booleanOperation34 = cylinderBuilder34.BooleanOption
    
    booleanOperation34.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Create
    
    nXObject66 = cylinderBuilder34.Commit()
    
    cylinder34 = nXObject66
    bodies34 = cylinder34.GetBodies()
    
    cylinderBuilder34.Destroy()
    
    part67 = theSession.Parts.Work
    
    booleanBuilder33 = workPart.Features.CreateBooleanBuilder(NXOpen.Features.BooleanFeature.Null)
    
    booleanBuilder33.Target = bodies1[0]
    
    booleanBuilder33.Tool = bodies34[0]
    
    booleanBuilder33.Operation = NXOpen.Features.Feature.BooleanType.Subtract
    
    nXObject67 = booleanBuilder33.Commit()
    
    booleanBuilder33.Destroy()
    
    part68 = theSession.Parts.Work
    
    cylinderBuilder35 = workPart.Features.CreateCylinderBuilder(NXOpen.Features.Feature.Null)
    
    expression69 = cylinderBuilder35.Diameter
    
    expression69.RightHandSide = "121.99999999999999"
    
    expression70 = cylinderBuilder35.Height
    
    expression70.RightHandSide = "121.99999999999999"
    
    origin35 = NXOpen.Point3d(0.0, -121.99999999999999, 0.0)
    cylinderBuilder35.Origin = origin35
    
    vector35 = NXOpen.Vector3d(0.0, 0.0, 1.0)
    cylinderBuilder35.Direction = vector35
    
    booleanOperation35 = cylinderBuilder35.BooleanOption
    
    booleanOperation35.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Create
    
    nXObject68 = cylinderBuilder35.Commit()
    
    cylinder35 = nXObject68
    bodies35 = cylinder35.GetBodies()
    
    cylinderBuilder35.Destroy()
    
    part69 = theSession.Parts.Work
    
    cylinderBuilder36 = workPart.Features.CreateCylinderBuilder(NXOpen.Features.Feature.Null)
    
    expression71 = cylinderBuilder36.Diameter
    
    expression71.RightHandSide = "12.2"
    
    expression72 = cylinderBuilder36.Height
    
    expression72.RightHandSide = "121.99999999999999"
    
    origin36 = NXOpen.Point3d(59.827902104597051, -110.09949035701617, 0.0)
    cylinderBuilder36.Origin = origin36
    
    vector36 = NXOpen.Vector3d(0.0, 0.0, 1.0)
    cylinderBuilder36.Direction = vector36
    
    booleanOperation36 = cylinderBuilder36.BooleanOption
    
    booleanOperation36.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Create
    
    nXObject69 = cylinderBuilder36.Commit()
    
    cylinder36 = nXObject69
    bodies36 = cylinder36.GetBodies()
    
    cylinderBuilder36.Destroy()
    
    part70 = theSession.Parts.Work
    
    booleanBuilder34 = workPart.Features.CreateBooleanBuilder(NXOpen.Features.BooleanFeature.Null)
    
    booleanBuilder34.Target = bodies35[0]
    
    booleanBuilder34.Tool = bodies36[0]
    
    booleanBuilder34.Operation = NXOpen.Features.Feature.BooleanType.Subtract
    
    nXObject70 = booleanBuilder34.Commit()
    
    booleanBuilder34.Destroy()
    
    part71 = theSession.Parts.Work
    
    cylinderBuilder37 = workPart.Features.CreateCylinderBuilder(NXOpen.Features.Feature.Null)
    
    expression73 = cylinderBuilder37.Diameter
    
    expression73.RightHandSide = "12.2"
    
    expression74 = cylinderBuilder37.Height
    
    expression74.RightHandSide = "121.99999999999999"
    
    origin37 = NXOpen.Point3d(56.356651483188486, -98.656310625729503, 0.0)
    cylinderBuilder37.Origin = origin37
    
    vector37 = NXOpen.Vector3d(0.0, 0.0, 1.0)
    cylinderBuilder37.Direction = vector37
    
    booleanOperation37 = cylinderBuilder37.BooleanOption
    
    booleanOperation37.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Create
    
    nXObject71 = cylinderBuilder37.Commit()
    
    cylinder37 = nXObject71
    bodies37 = cylinder37.GetBodies()
    
    cylinderBuilder37.Destroy()
    
    part72 = theSession.Parts.Work
    
    booleanBuilder35 = workPart.Features.CreateBooleanBuilderUsingCollector(NXOpen.Features.BooleanFeature.Null)
    
    booleanBuilder35.Target = bodies35[0]
    
    booleanBuilder35.Tool = bodies37[0]
    
    booleanBuilder35.Operation = NXOpen.Features.Feature.BooleanType.Unite
    
    nXObject72 = booleanBuilder35.Commit()
    
    booleanBuilder35.Destroy()
    
    part73 = theSession.Parts.Work
    
    cylinderBuilder38 = workPart.Features.CreateCylinderBuilder(NXOpen.Features.Feature.Null)
    
    expression75 = cylinderBuilder38.Diameter
    
    expression75.RightHandSide = "12.2"
    
    expression76 = cylinderBuilder38.Height
    
    expression76.RightHandSide = "121.99999999999999"
    
    origin38 = NXOpen.Point3d(50.719646350455257, -88.110215785804257, 0.0)
    cylinderBuilder38.Origin = origin38
    
    vector38 = NXOpen.Vector3d(0.0, 0.0, 1.0)
    cylinderBuilder38.Direction = vector38
    
    booleanOperation38 = cylinderBuilder38.BooleanOption
    
    booleanOperation38.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Create
    
    nXObject73 = cylinderBuilder38.Commit()
    
    cylinder38 = nXObject73
    bodies38 = cylinder38.GetBodies()
    
    cylinderBuilder38.Destroy()
    
    part74 = theSession.Parts.Work
    
    booleanBuilder36 = workPart.Features.CreateBooleanBuilder(NXOpen.Features.BooleanFeature.Null)
    
    booleanBuilder36.Target = bodies35[0]
    
    booleanBuilder36.Tool = bodies38[0]
    
    booleanBuilder36.Operation = NXOpen.Features.Feature.BooleanType.Subtract
    
    nXObject74 = booleanBuilder36.Commit()
    
    booleanBuilder36.Destroy()
    
    part75 = theSession.Parts.Work
    
    cylinderBuilder39 = workPart.Features.CreateCylinderBuilder(NXOpen.Features.Feature.Null)
    
    expression77 = cylinderBuilder39.Diameter
    
    expression77.RightHandSide = "12.2"
    
    expression78 = cylinderBuilder39.Height
    
    expression78.RightHandSide = "121.99999999999999"
    
    origin39 = NXOpen.Point3d(43.133513652379399, -78.866486347620594, 0.0)
    cylinderBuilder39.Origin = origin39
    
    vector39 = NXOpen.Vector3d(0.0, 0.0, 1.0)
    cylinderBuilder39.Direction = vector39
    
    booleanOperation39 = cylinderBuilder39.BooleanOption
    
    booleanOperation39.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Create
    
    nXObject75 = cylinderBuilder39.Commit()
    
    cylinder39 = nXObject75
    bodies39 = cylinder39.GetBodies()
    
    cylinderBuilder39.Destroy()
    
    part76 = theSession.Parts.Work
    
    booleanBuilder37 = workPart.Features.CreateBooleanBuilderUsingCollector(NXOpen.Features.BooleanFeature.Null)
    
    booleanBuilder37.Target = bodies35[0]
    
    booleanBuilder37.Tool = bodies39[0]
    
    booleanBuilder37.Operation = NXOpen.Features.Feature.BooleanType.Unite
    
    nXObject76 = booleanBuilder37.Commit()
    
    booleanBuilder37.Destroy()
    
    part77 = theSession.Parts.Work
    
    cylinderBuilder40 = workPart.Features.CreateCylinderBuilder(NXOpen.Features.Feature.Null)
    
    expression79 = cylinderBuilder40.Diameter
    
    expression79.RightHandSide = "12.2"
    
    expression80 = cylinderBuilder40.Height
    
    expression80.RightHandSide = "121.99999999999999"
    
    origin40 = NXOpen.Point3d(33.889784214195736, -71.280353649544736, 0.0)
    cylinderBuilder40.Origin = origin40
    
    vector40 = NXOpen.Vector3d(0.0, 0.0, 1.0)
    cylinderBuilder40.Direction = vector40
    
    booleanOperation40 = cylinderBuilder40.BooleanOption
    
    booleanOperation40.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Create
    
    nXObject77 = cylinderBuilder40.Commit()
    
    cylinder40 = nXObject77
    bodies40 = cylinder40.GetBodies()
    
    cylinderBuilder40.Destroy()
    
    part78 = theSession.Parts.Work
    
    booleanBuilder38 = workPart.Features.CreateBooleanBuilder(NXOpen.Features.BooleanFeature.Null)
    
    booleanBuilder38.Target = bodies35[0]
    
    booleanBuilder38.Tool = bodies40[0]
    
    booleanBuilder38.Operation = NXOpen.Features.Feature.BooleanType.Subtract
    
    nXObject78 = booleanBuilder38.Commit()
    
    booleanBuilder38.Destroy()
    
    part79 = theSession.Parts.Work
    
    cylinderBuilder41 = workPart.Features.CreateCylinderBuilder(NXOpen.Features.Feature.Null)
    
    expression81 = cylinderBuilder41.Diameter
    
    expression81.RightHandSide = "12.2"
    
    expression82 = cylinderBuilder41.Height
    
    expression82.RightHandSide = "121.99999999999999"
    
    origin41 = NXOpen.Point3d(23.343689374270479, -65.6433485168115, 0.0)
    cylinderBuilder41.Origin = origin41
    
    vector41 = NXOpen.Vector3d(0.0, 0.0, 1.0)
    cylinderBuilder41.Direction = vector41
    
    booleanOperation41 = cylinderBuilder41.BooleanOption
    
    booleanOperation41.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Create
    
    nXObject79 = cylinderBuilder41.Commit()
    
    cylinder41 = nXObject79
    bodies41 = cylinder41.GetBodies()
    
    cylinderBuilder41.Destroy()
    
    part80 = theSession.Parts.Work
    
    booleanBuilder39 = workPart.Features.CreateBooleanBuilderUsingCollector(NXOpen.Features.BooleanFeature.Null)
    
    booleanBuilder39.Target = bodies35[0]
    
    booleanBuilder39.Tool = bodies41[0]
    
    booleanBuilder39.Operation = NXOpen.Features.Feature.BooleanType.Unite
    
    nXObject80 = booleanBuilder39.Commit()
    
    booleanBuilder39.Destroy()
    
    part81 = theSession.Parts.Work
    
    cylinderBuilder42 = workPart.Features.CreateCylinderBuilder(NXOpen.Features.Feature.Null)
    
    expression83 = cylinderBuilder42.Diameter
    
    expression83.RightHandSide = "12.2"
    
    expression84 = cylinderBuilder42.Height
    
    expression84.RightHandSide = "121.99999999999999"
    
    origin42 = NXOpen.Point3d(11.900509642983828, -62.172097895402935, 0.0)
    cylinderBuilder42.Origin = origin42
    
    vector42 = NXOpen.Vector3d(0.0, 0.0, 1.0)
    cylinderBuilder42.Direction = vector42
    
    booleanOperation42 = cylinderBuilder42.BooleanOption
    
    booleanOperation42.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Create
    
    nXObject81 = cylinderBuilder42.Commit()
    
    cylinder42 = nXObject81
    bodies42 = cylinder42.GetBodies()
    
    cylinderBuilder42.Destroy()
    
    part82 = theSession.Parts.Work
    
    booleanBuilder40 = workPart.Features.CreateBooleanBuilder(NXOpen.Features.BooleanFeature.Null)
    
    booleanBuilder40.Target = bodies35[0]
    
    booleanBuilder40.Tool = bodies42[0]
    
    booleanBuilder40.Operation = NXOpen.Features.Feature.BooleanType.Subtract
    
    nXObject82 = booleanBuilder40.Commit()
    
    booleanBuilder40.Destroy()
    
    part83 = theSession.Parts.Work
    
    cylinderBuilder43 = workPart.Features.CreateCylinderBuilder(NXOpen.Features.Feature.Null)
    
    expression85 = cylinderBuilder43.Diameter
    
    expression85.RightHandSide = "12.2"
    
    expression86 = cylinderBuilder43.Height
    
    expression86.RightHandSide = "121.99999999999999"
    
    origin43 = NXOpen.Point3d(3.7351727373994268e-15, -60.999999999999993, 0.0)
    cylinderBuilder43.Origin = origin43
    
    vector43 = NXOpen.Vector3d(0.0, 0.0, 1.0)
    cylinderBuilder43.Direction = vector43
    
    booleanOperation43 = cylinderBuilder43.BooleanOption
    
    booleanOperation43.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Create
    
    nXObject83 = cylinderBuilder43.Commit()
    
    cylinder43 = nXObject83
    bodies43 = cylinder43.GetBodies()
    
    cylinderBuilder43.Destroy()
    
    part84 = theSession.Parts.Work
    
    booleanBuilder41 = workPart.Features.CreateBooleanBuilderUsingCollector(NXOpen.Features.BooleanFeature.Null)
    
    booleanBuilder41.Target = bodies35[0]
    
    booleanBuilder41.Tool = bodies43[0]
    
    booleanBuilder41.Operation = NXOpen.Features.Feature.BooleanType.Unite
    
    nXObject84 = booleanBuilder41.Commit()
    
    booleanBuilder41.Destroy()
    
    part85 = theSession.Parts.Work
    
    cylinderBuilder44 = workPart.Features.CreateCylinderBuilder(NXOpen.Features.Feature.Null)
    
    expression87 = cylinderBuilder44.Diameter
    
    expression87.RightHandSide = "12.2"
    
    expression88 = cylinderBuilder44.Height
    
    expression88.RightHandSide = "121.99999999999999"
    
    origin44 = NXOpen.Point3d(-11.900509642983819, -62.172097895402935, 0.0)
    cylinderBuilder44.Origin = origin44
    
    vector44 = NXOpen.Vector3d(0.0, 0.0, 1.0)
    cylinderBuilder44.Direction = vector44
    
    booleanOperation44 = cylinderBuilder44.BooleanOption
    
    booleanOperation44.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Create
    
    nXObject85 = cylinderBuilder44.Commit()
    
    cylinder44 = nXObject85
    bodies44 = cylinder44.GetBodies()
    
    cylinderBuilder44.Destroy()
    
    part86 = theSession.Parts.Work
    
    booleanBuilder42 = workPart.Features.CreateBooleanBuilder(NXOpen.Features.BooleanFeature.Null)
    
    booleanBuilder42.Target = bodies35[0]
    
    booleanBuilder42.Tool = bodies44[0]
    
    booleanBuilder42.Operation = NXOpen.Features.Feature.BooleanType.Subtract
    
    nXObject86 = booleanBuilder42.Commit()
    
    booleanBuilder42.Destroy()
    
    part87 = theSession.Parts.Work
    
    cylinderBuilder45 = workPart.Features.CreateCylinderBuilder(NXOpen.Features.Feature.Null)
    
    expression89 = cylinderBuilder45.Diameter
    
    expression89.RightHandSide = "12.2"
    
    expression90 = cylinderBuilder45.Height
    
    expression90.RightHandSide = "121.99999999999999"
    
    origin45 = NXOpen.Point3d(-23.343689374270472, -65.6433485168115, 0.0)
    cylinderBuilder45.Origin = origin45
    
    vector45 = NXOpen.Vector3d(0.0, 0.0, 1.0)
    cylinderBuilder45.Direction = vector45
    
    booleanOperation45 = cylinderBuilder45.BooleanOption
    
    booleanOperation45.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Create
    
    nXObject87 = cylinderBuilder45.Commit()
    
    cylinder45 = nXObject87
    bodies45 = cylinder45.GetBodies()
    
    cylinderBuilder45.Destroy()
    
    part88 = theSession.Parts.Work
    
    booleanBuilder43 = workPart.Features.CreateBooleanBuilderUsingCollector(NXOpen.Features.BooleanFeature.Null)
    
    booleanBuilder43.Target = bodies35[0]
    
    booleanBuilder43.Tool = bodies45[0]
    
    booleanBuilder43.Operation = NXOpen.Features.Feature.BooleanType.Unite
    
    nXObject88 = booleanBuilder43.Commit()
    
    booleanBuilder43.Destroy()
    
    part89 = theSession.Parts.Work
    
    cylinderBuilder46 = workPart.Features.CreateCylinderBuilder(NXOpen.Features.Feature.Null)
    
    expression91 = cylinderBuilder46.Diameter
    
    expression91.RightHandSide = "12.2"
    
    expression92 = cylinderBuilder46.Height
    
    expression92.RightHandSide = "121.99999999999999"
    
    origin46 = NXOpen.Point3d(-33.889784214195714, -71.280353649544736, 0.0)
    cylinderBuilder46.Origin = origin46
    
    vector46 = NXOpen.Vector3d(0.0, 0.0, 1.0)
    cylinderBuilder46.Direction = vector46
    
    booleanOperation46 = cylinderBuilder46.BooleanOption
    
    booleanOperation46.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Create
    
    nXObject89 = cylinderBuilder46.Commit()
    
    cylinder46 = nXObject89
    bodies46 = cylinder46.GetBodies()
    
    cylinderBuilder46.Destroy()
    
    part90 = theSession.Parts.Work
    
    booleanBuilder44 = workPart.Features.CreateBooleanBuilder(NXOpen.Features.BooleanFeature.Null)
    
    booleanBuilder44.Target = bodies35[0]
    
    booleanBuilder44.Tool = bodies46[0]
    
    booleanBuilder44.Operation = NXOpen.Features.Feature.BooleanType.Subtract
    
    nXObject90 = booleanBuilder44.Commit()
    
    booleanBuilder44.Destroy()
    
    part91 = theSession.Parts.Work
    
    cylinderBuilder47 = workPart.Features.CreateCylinderBuilder(NXOpen.Features.Feature.Null)
    
    expression93 = cylinderBuilder47.Diameter
    
    expression93.RightHandSide = "12.2"
    
    expression94 = cylinderBuilder47.Height
    
    expression94.RightHandSide = "121.99999999999999"
    
    origin47 = NXOpen.Point3d(-43.133513652379392, -78.866486347620594, 0.0)
    cylinderBuilder47.Origin = origin47
    
    vector47 = NXOpen.Vector3d(0.0, 0.0, 1.0)
    cylinderBuilder47.Direction = vector47
    
    booleanOperation47 = cylinderBuilder47.BooleanOption
    
    booleanOperation47.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Create
    
    nXObject91 = cylinderBuilder47.Commit()
    
    cylinder47 = nXObject91
    bodies47 = cylinder47.GetBodies()
    
    cylinderBuilder47.Destroy()
    
    part92 = theSession.Parts.Work
    
    booleanBuilder45 = workPart.Features.CreateBooleanBuilderUsingCollector(NXOpen.Features.BooleanFeature.Null)
    
    booleanBuilder45.Target = bodies35[0]
    
    booleanBuilder45.Tool = bodies47[0]
    
    booleanBuilder45.Operation = NXOpen.Features.Feature.BooleanType.Unite
    
    nXObject92 = booleanBuilder45.Commit()
    
    booleanBuilder45.Destroy()
    
    part93 = theSession.Parts.Work
    
    cylinderBuilder48 = workPart.Features.CreateCylinderBuilder(NXOpen.Features.Feature.Null)
    
    expression95 = cylinderBuilder48.Diameter
    
    expression95.RightHandSide = "12.2"
    
    expression96 = cylinderBuilder48.Height
    
    expression96.RightHandSide = "121.99999999999999"
    
    origin48 = NXOpen.Point3d(-50.719646350455257, -88.110215785804257, 0.0)
    cylinderBuilder48.Origin = origin48
    
    vector48 = NXOpen.Vector3d(0.0, 0.0, 1.0)
    cylinderBuilder48.Direction = vector48
    
    booleanOperation48 = cylinderBuilder48.BooleanOption
    
    booleanOperation48.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Create
    
    nXObject93 = cylinderBuilder48.Commit()
    
    cylinder48 = nXObject93
    bodies48 = cylinder48.GetBodies()
    
    cylinderBuilder48.Destroy()
    
    part94 = theSession.Parts.Work
    
    booleanBuilder46 = workPart.Features.CreateBooleanBuilder(NXOpen.Features.BooleanFeature.Null)
    
    booleanBuilder46.Target = bodies35[0]
    
    booleanBuilder46.Tool = bodies48[0]
    
    booleanBuilder46.Operation = NXOpen.Features.Feature.BooleanType.Subtract
    
    nXObject94 = booleanBuilder46.Commit()
    
    booleanBuilder46.Destroy()
    
    part95 = theSession.Parts.Work
    
    cylinderBuilder49 = workPart.Features.CreateCylinderBuilder(NXOpen.Features.Feature.Null)
    
    expression97 = cylinderBuilder49.Diameter
    
    expression97.RightHandSide = "12.2"
    
    expression98 = cylinderBuilder49.Height
    
    expression98.RightHandSide = "121.99999999999999"
    
    origin49 = NXOpen.Point3d(-56.356651483188493, -98.656310625729532, 0.0)
    cylinderBuilder49.Origin = origin49
    
    vector49 = NXOpen.Vector3d(0.0, 0.0, 1.0)
    cylinderBuilder49.Direction = vector49
    
    booleanOperation49 = cylinderBuilder49.BooleanOption
    
    booleanOperation49.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Create
    
    nXObject95 = cylinderBuilder49.Commit()
    
    cylinder49 = nXObject95
    bodies49 = cylinder49.GetBodies()
    
    cylinderBuilder49.Destroy()
    
    part96 = theSession.Parts.Work
    
    booleanBuilder47 = workPart.Features.CreateBooleanBuilderUsingCollector(NXOpen.Features.BooleanFeature.Null)
    
    booleanBuilder47.Target = bodies35[0]
    
    booleanBuilder47.Tool = bodies49[0]
    
    booleanBuilder47.Operation = NXOpen.Features.Feature.BooleanType.Unite
    
    nXObject96 = booleanBuilder47.Commit()
    
    booleanBuilder47.Destroy()
    
    part97 = theSession.Parts.Work
    
    cylinderBuilder50 = workPart.Features.CreateCylinderBuilder(NXOpen.Features.Feature.Null)
    
    expression99 = cylinderBuilder50.Diameter
    
    expression99.RightHandSide = "12.2"
    
    expression100 = cylinderBuilder50.Height
    
    expression100.RightHandSide = "121.99999999999999"
    
    origin50 = NXOpen.Point3d(-59.827902104597051, -110.09949035701614, 0.0)
    cylinderBuilder50.Origin = origin50
    
    vector50 = NXOpen.Vector3d(0.0, 0.0, 1.0)
    cylinderBuilder50.Direction = vector50
    
    booleanOperation50 = cylinderBuilder50.BooleanOption
    
    booleanOperation50.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Create
    
    nXObject97 = cylinderBuilder50.Commit()
    
    cylinder50 = nXObject97
    bodies50 = cylinder50.GetBodies()
    
    cylinderBuilder50.Destroy()
    
    part98 = theSession.Parts.Work
    
    booleanBuilder48 = workPart.Features.CreateBooleanBuilder(NXOpen.Features.BooleanFeature.Null)
    
    booleanBuilder48.Target = bodies35[0]
    
    booleanBuilder48.Tool = bodies50[0]
    
    booleanBuilder48.Operation = NXOpen.Features.Feature.BooleanType.Subtract
    
    nXObject98 = booleanBuilder48.Commit()
    
    booleanBuilder48.Destroy()
    
    part99 = theSession.Parts.Work
    
    cylinderBuilder51 = workPart.Features.CreateCylinderBuilder(NXOpen.Features.Feature.Null)
    
    expression101 = cylinderBuilder51.Diameter
    
    expression101.RightHandSide = "12.2"
    
    expression102 = cylinderBuilder51.Height
    
    expression102.RightHandSide = "121.99999999999999"
    
    origin51 = NXOpen.Point3d(-60.999999999999993, -121.99999999999997, 0.0)
    cylinderBuilder51.Origin = origin51
    
    vector51 = NXOpen.Vector3d(0.0, 0.0, 1.0)
    cylinderBuilder51.Direction = vector51
    
    booleanOperation51 = cylinderBuilder51.BooleanOption
    
    booleanOperation51.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Create
    
    nXObject99 = cylinderBuilder51.Commit()
    
    cylinder51 = nXObject99
    bodies51 = cylinder51.GetBodies()
    
    cylinderBuilder51.Destroy()
    
    part100 = theSession.Parts.Work
    
    booleanBuilder49 = workPart.Features.CreateBooleanBuilderUsingCollector(NXOpen.Features.BooleanFeature.Null)
    
    booleanBuilder49.Target = bodies35[0]
    
    booleanBuilder49.Tool = bodies51[0]
    
    booleanBuilder49.Operation = NXOpen.Features.Feature.BooleanType.Unite
    
    nXObject100 = booleanBuilder49.Commit()
    
    booleanBuilder49.Destroy()
    
    part101 = theSession.Parts.Work
    
    cylinderBuilder52 = workPart.Features.CreateCylinderBuilder(NXOpen.Features.Feature.Null)
    
    expression103 = cylinderBuilder52.Diameter
    
    expression103.RightHandSide = "12.2"
    
    expression104 = cylinderBuilder52.Height
    
    expression104.RightHandSide = "121.99999999999999"
    
    origin52 = NXOpen.Point3d(-59.827902104597051, -133.90050964298382, 0.0)
    cylinderBuilder52.Origin = origin52
    
    vector52 = NXOpen.Vector3d(0.0, 0.0, 1.0)
    cylinderBuilder52.Direction = vector52
    
    booleanOperation52 = cylinderBuilder52.BooleanOption
    
    booleanOperation52.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Create
    
    nXObject101 = cylinderBuilder52.Commit()
    
    cylinder52 = nXObject101
    bodies52 = cylinder52.GetBodies()
    
    cylinderBuilder52.Destroy()
    
    part102 = theSession.Parts.Work
    
    booleanBuilder50 = workPart.Features.CreateBooleanBuilder(NXOpen.Features.BooleanFeature.Null)
    
    booleanBuilder50.Target = bodies35[0]
    
    booleanBuilder50.Tool = bodies52[0]
    
    booleanBuilder50.Operation = NXOpen.Features.Feature.BooleanType.Subtract
    
    nXObject102 = booleanBuilder50.Commit()
    
    booleanBuilder50.Destroy()
    
    part103 = theSession.Parts.Work
    
    cylinderBuilder53 = workPart.Features.CreateCylinderBuilder(NXOpen.Features.Feature.Null)
    
    expression105 = cylinderBuilder53.Diameter
    
    expression105.RightHandSide = "12.2"
    
    expression106 = cylinderBuilder53.Height
    
    expression106.RightHandSide = "121.99999999999999"
    
    origin53 = NXOpen.Point3d(-56.356651483188479, -145.34368937427047, 0.0)
    cylinderBuilder53.Origin = origin53
    
    vector53 = NXOpen.Vector3d(0.0, 0.0, 1.0)
    cylinderBuilder53.Direction = vector53
    
    booleanOperation53 = cylinderBuilder53.BooleanOption
    
    booleanOperation53.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Create
    
    nXObject103 = cylinderBuilder53.Commit()
    
    cylinder53 = nXObject103
    bodies53 = cylinder53.GetBodies()
    
    cylinderBuilder53.Destroy()
    
    part104 = theSession.Parts.Work
    
    booleanBuilder51 = workPart.Features.CreateBooleanBuilderUsingCollector(NXOpen.Features.BooleanFeature.Null)
    
    booleanBuilder51.Target = bodies35[0]
    
    booleanBuilder51.Tool = bodies53[0]
    
    booleanBuilder51.Operation = NXOpen.Features.Feature.BooleanType.Unite
    
    nXObject104 = booleanBuilder51.Commit()
    
    booleanBuilder51.Destroy()
    
    part105 = theSession.Parts.Work
    
    cylinderBuilder54 = workPart.Features.CreateCylinderBuilder(NXOpen.Features.Feature.Null)
    
    expression107 = cylinderBuilder54.Diameter
    
    expression107.RightHandSide = "12.2"
    
    expression108 = cylinderBuilder54.Height
    
    expression108.RightHandSide = "121.99999999999999"
    
    origin54 = NXOpen.Point3d(-50.719646350455264, -155.88978421419569, 0.0)
    cylinderBuilder54.Origin = origin54
    
    vector54 = NXOpen.Vector3d(0.0, 0.0, 1.0)
    cylinderBuilder54.Direction = vector54
    
    booleanOperation54 = cylinderBuilder54.BooleanOption
    
    booleanOperation54.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Create
    
    nXObject105 = cylinderBuilder54.Commit()
    
    cylinder54 = nXObject105
    bodies54 = cylinder54.GetBodies()
    
    cylinderBuilder54.Destroy()
    
    part106 = theSession.Parts.Work
    
    booleanBuilder52 = workPart.Features.CreateBooleanBuilder(NXOpen.Features.BooleanFeature.Null)
    
    booleanBuilder52.Target = bodies35[0]
    
    booleanBuilder52.Tool = bodies54[0]
    
    booleanBuilder52.Operation = NXOpen.Features.Feature.BooleanType.Subtract
    
    nXObject106 = booleanBuilder52.Commit()
    
    booleanBuilder52.Destroy()
    
    part107 = theSession.Parts.Work
    
    cylinderBuilder55 = workPart.Features.CreateCylinderBuilder(NXOpen.Features.Feature.Null)
    
    expression109 = cylinderBuilder55.Diameter
    
    expression109.RightHandSide = "12.2"
    
    expression110 = cylinderBuilder55.Height
    
    expression110.RightHandSide = "121.99999999999999"
    
    origin55 = NXOpen.Point3d(-43.133513652379406, -165.13351365237938, 0.0)
    cylinderBuilder55.Origin = origin55
    
    vector55 = NXOpen.Vector3d(0.0, 0.0, 1.0)
    cylinderBuilder55.Direction = vector55
    
    booleanOperation55 = cylinderBuilder55.BooleanOption
    
    booleanOperation55.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Create
    
    nXObject107 = cylinderBuilder55.Commit()
    
    cylinder55 = nXObject107
    bodies55 = cylinder55.GetBodies()
    
    cylinderBuilder55.Destroy()
    
    part108 = theSession.Parts.Work
    
    booleanBuilder53 = workPart.Features.CreateBooleanBuilderUsingCollector(NXOpen.Features.BooleanFeature.Null)
    
    booleanBuilder53.Target = bodies35[0]
    
    booleanBuilder53.Tool = bodies55[0]
    
    booleanBuilder53.Operation = NXOpen.Features.Feature.BooleanType.Unite
    
    nXObject108 = booleanBuilder53.Commit()
    
    booleanBuilder53.Destroy()
    
    part109 = theSession.Parts.Work
    
    cylinderBuilder56 = workPart.Features.CreateCylinderBuilder(NXOpen.Features.Feature.Null)
    
    expression111 = cylinderBuilder56.Diameter
    
    expression111.RightHandSide = "12.2"
    
    expression112 = cylinderBuilder56.Height
    
    expression112.RightHandSide = "121.99999999999999"
    
    origin56 = NXOpen.Point3d(-33.889784214195728, -172.71964635045524, 0.0)
    cylinderBuilder56.Origin = origin56
    
    vector56 = NXOpen.Vector3d(0.0, 0.0, 1.0)
    cylinderBuilder56.Direction = vector56
    
    booleanOperation56 = cylinderBuilder56.BooleanOption
    
    booleanOperation56.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Create
    
    nXObject109 = cylinderBuilder56.Commit()
    
    cylinder56 = nXObject109
    bodies56 = cylinder56.GetBodies()
    
    cylinderBuilder56.Destroy()
    
    part110 = theSession.Parts.Work
    
    booleanBuilder54 = workPart.Features.CreateBooleanBuilder(NXOpen.Features.BooleanFeature.Null)
    
    booleanBuilder54.Target = bodies35[0]
    
    booleanBuilder54.Tool = bodies56[0]
    
    booleanBuilder54.Operation = NXOpen.Features.Feature.BooleanType.Subtract
    
    nXObject110 = booleanBuilder54.Commit()
    
    booleanBuilder54.Destroy()
    
    part111 = theSession.Parts.Work
    
    cylinderBuilder57 = workPart.Features.CreateCylinderBuilder(NXOpen.Features.Feature.Null)
    
    expression113 = cylinderBuilder57.Diameter
    
    expression113.RightHandSide = "12.2"
    
    expression114 = cylinderBuilder57.Height
    
    expression114.RightHandSide = "121.99999999999999"
    
    origin57 = NXOpen.Point3d(-23.343689374270458, -178.35665148318847, 0.0)
    cylinderBuilder57.Origin = origin57
    
    vector57 = NXOpen.Vector3d(0.0, 0.0, 1.0)
    cylinderBuilder57.Direction = vector57
    
    booleanOperation57 = cylinderBuilder57.BooleanOption
    
    booleanOperation57.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Create
    
    nXObject111 = cylinderBuilder57.Commit()
    
    cylinder57 = nXObject111
    bodies57 = cylinder57.GetBodies()
    
    cylinderBuilder57.Destroy()
    
    part112 = theSession.Parts.Work
    
    booleanBuilder55 = workPart.Features.CreateBooleanBuilderUsingCollector(NXOpen.Features.BooleanFeature.Null)
    
    booleanBuilder55.Target = bodies35[0]
    
    booleanBuilder55.Tool = bodies57[0]
    
    booleanBuilder55.Operation = NXOpen.Features.Feature.BooleanType.Unite
    
    nXObject112 = booleanBuilder55.Commit()
    
    booleanBuilder55.Destroy()
    
    part113 = theSession.Parts.Work
    
    cylinderBuilder58 = workPart.Features.CreateCylinderBuilder(NXOpen.Features.Feature.Null)
    
    expression115 = cylinderBuilder58.Diameter
    
    expression115.RightHandSide = "12.2"
    
    expression116 = cylinderBuilder58.Height
    
    expression116.RightHandSide = "121.99999999999999"
    
    origin58 = NXOpen.Point3d(-11.900509642983847, -181.82790210459703, 0.0)
    cylinderBuilder58.Origin = origin58
    
    vector58 = NXOpen.Vector3d(0.0, 0.0, 1.0)
    cylinderBuilder58.Direction = vector58
    
    booleanOperation58 = cylinderBuilder58.BooleanOption
    
    booleanOperation58.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Create
    
    nXObject113 = cylinderBuilder58.Commit()
    
    cylinder58 = nXObject113
    bodies58 = cylinder58.GetBodies()
    
    cylinderBuilder58.Destroy()
    
    part114 = theSession.Parts.Work
    
    booleanBuilder56 = workPart.Features.CreateBooleanBuilder(NXOpen.Features.BooleanFeature.Null)
    
    booleanBuilder56.Target = bodies35[0]
    
    booleanBuilder56.Tool = bodies58[0]
    
    booleanBuilder56.Operation = NXOpen.Features.Feature.BooleanType.Subtract
    
    nXObject114 = booleanBuilder56.Commit()
    
    booleanBuilder56.Destroy()
    
    part115 = theSession.Parts.Work
    
    cylinderBuilder59 = workPart.Features.CreateCylinderBuilder(NXOpen.Features.Feature.Null)
    
    expression117 = cylinderBuilder59.Diameter
    
    expression117.RightHandSide = "12.2"
    
    expression118 = cylinderBuilder59.Height
    
    expression118.RightHandSide = "121.99999999999999"
    
    origin59 = NXOpen.Point3d(-1.120551821219828e-14, -182.99999999999997, 0.0)
    cylinderBuilder59.Origin = origin59
    
    vector59 = NXOpen.Vector3d(0.0, 0.0, 1.0)
    cylinderBuilder59.Direction = vector59
    
    booleanOperation59 = cylinderBuilder59.BooleanOption
    
    booleanOperation59.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Create
    
    nXObject115 = cylinderBuilder59.Commit()
    
    cylinder59 = nXObject115
    bodies59 = cylinder59.GetBodies()
    
    cylinderBuilder59.Destroy()
    
    part116 = theSession.Parts.Work
    
    booleanBuilder57 = workPart.Features.CreateBooleanBuilderUsingCollector(NXOpen.Features.BooleanFeature.Null)
    
    booleanBuilder57.Target = bodies35[0]
    
    booleanBuilder57.Tool = bodies59[0]
    
    booleanBuilder57.Operation = NXOpen.Features.Feature.BooleanType.Unite
    
    nXObject116 = booleanBuilder57.Commit()
    
    booleanBuilder57.Destroy()
    
    part117 = theSession.Parts.Work
    
    cylinderBuilder60 = workPart.Features.CreateCylinderBuilder(NXOpen.Features.Feature.Null)
    
    expression119 = cylinderBuilder60.Diameter
    
    expression119.RightHandSide = "12.2"
    
    expression120 = cylinderBuilder60.Height
    
    expression120.RightHandSide = "121.99999999999999"
    
    origin60 = NXOpen.Point3d(11.900509642983826, -181.82790210459703, 0.0)
    cylinderBuilder60.Origin = origin60
    
    vector60 = NXOpen.Vector3d(0.0, 0.0, 1.0)
    cylinderBuilder60.Direction = vector60
    
    booleanOperation60 = cylinderBuilder60.BooleanOption
    
    booleanOperation60.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Create
    
    nXObject117 = cylinderBuilder60.Commit()
    
    cylinder60 = nXObject117
    bodies60 = cylinder60.GetBodies()
    
    cylinderBuilder60.Destroy()
    
    part118 = theSession.Parts.Work
    
    booleanBuilder58 = workPart.Features.CreateBooleanBuilder(NXOpen.Features.BooleanFeature.Null)
    
    booleanBuilder58.Target = bodies35[0]
    
    booleanBuilder58.Tool = bodies60[0]
    
    booleanBuilder58.Operation = NXOpen.Features.Feature.BooleanType.Subtract
    
    nXObject118 = booleanBuilder58.Commit()
    
    booleanBuilder58.Destroy()
    
    part119 = theSession.Parts.Work
    
    cylinderBuilder61 = workPart.Features.CreateCylinderBuilder(NXOpen.Features.Feature.Null)
    
    expression121 = cylinderBuilder61.Diameter
    
    expression121.RightHandSide = "12.2"
    
    expression122 = cylinderBuilder61.Height
    
    expression122.RightHandSide = "121.99999999999999"
    
    origin61 = NXOpen.Point3d(23.343689374270486, -178.35665148318847, 0.0)
    cylinderBuilder61.Origin = origin61
    
    vector61 = NXOpen.Vector3d(0.0, 0.0, 1.0)
    cylinderBuilder61.Direction = vector61
    
    booleanOperation61 = cylinderBuilder61.BooleanOption
    
    booleanOperation61.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Create
    
    nXObject119 = cylinderBuilder61.Commit()
    
    cylinder61 = nXObject119
    bodies61 = cylinder61.GetBodies()
    
    cylinderBuilder61.Destroy()
    
    part120 = theSession.Parts.Work
    
    booleanBuilder59 = workPart.Features.CreateBooleanBuilderUsingCollector(NXOpen.Features.BooleanFeature.Null)
    
    booleanBuilder59.Target = bodies35[0]
    
    booleanBuilder59.Tool = bodies61[0]
    
    booleanBuilder59.Operation = NXOpen.Features.Feature.BooleanType.Unite
    
    nXObject120 = booleanBuilder59.Commit()
    
    booleanBuilder59.Destroy()
    
    part121 = theSession.Parts.Work
    
    cylinderBuilder62 = workPart.Features.CreateCylinderBuilder(NXOpen.Features.Feature.Null)
    
    expression123 = cylinderBuilder62.Diameter
    
    expression123.RightHandSide = "12.2"
    
    expression124 = cylinderBuilder62.Height
    
    expression124.RightHandSide = "121.99999999999999"
    
    origin62 = NXOpen.Point3d(33.889784214195757, -172.71964635045524, 0.0)
    cylinderBuilder62.Origin = origin62
    
    vector62 = NXOpen.Vector3d(0.0, 0.0, 1.0)
    cylinderBuilder62.Direction = vector62
    
    booleanOperation62 = cylinderBuilder62.BooleanOption
    
    booleanOperation62.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Create
    
    nXObject121 = cylinderBuilder62.Commit()
    
    cylinder62 = nXObject121
    bodies62 = cylinder62.GetBodies()
    
    cylinderBuilder62.Destroy()
    
    part122 = theSession.Parts.Work
    
    booleanBuilder60 = workPart.Features.CreateBooleanBuilder(NXOpen.Features.BooleanFeature.Null)
    
    booleanBuilder60.Target = bodies35[0]
    
    booleanBuilder60.Tool = bodies62[0]
    
    booleanBuilder60.Operation = NXOpen.Features.Feature.BooleanType.Subtract
    
    nXObject122 = booleanBuilder60.Commit()
    
    booleanBuilder60.Destroy()
    
    part123 = theSession.Parts.Work
    
    cylinderBuilder63 = workPart.Features.CreateCylinderBuilder(NXOpen.Features.Feature.Null)
    
    expression125 = cylinderBuilder63.Diameter
    
    expression125.RightHandSide = "12.2"
    
    expression126 = cylinderBuilder63.Height
    
    expression126.RightHandSide = "121.99999999999999"
    
    origin63 = NXOpen.Point3d(43.133513652379385, -165.13351365237941, 0.0)
    cylinderBuilder63.Origin = origin63
    
    vector63 = NXOpen.Vector3d(0.0, 0.0, 1.0)
    cylinderBuilder63.Direction = vector63
    
    booleanOperation63 = cylinderBuilder63.BooleanOption
    
    booleanOperation63.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Create
    
    nXObject123 = cylinderBuilder63.Commit()
    
    cylinder63 = nXObject123
    bodies63 = cylinder63.GetBodies()
    
    cylinderBuilder63.Destroy()
    
    part124 = theSession.Parts.Work
    
    booleanBuilder61 = workPart.Features.CreateBooleanBuilderUsingCollector(NXOpen.Features.BooleanFeature.Null)
    
    booleanBuilder61.Target = bodies35[0]
    
    booleanBuilder61.Tool = bodies63[0]
    
    booleanBuilder61.Operation = NXOpen.Features.Feature.BooleanType.Unite
    
    nXObject124 = booleanBuilder61.Commit()
    
    booleanBuilder61.Destroy()
    
    part125 = theSession.Parts.Work
    
    cylinderBuilder64 = workPart.Features.CreateCylinderBuilder(NXOpen.Features.Feature.Null)
    
    expression127 = cylinderBuilder64.Diameter
    
    expression127.RightHandSide = "12.2"
    
    expression128 = cylinderBuilder64.Height
    
    expression128.RightHandSide = "121.99999999999999"
    
    origin64 = NXOpen.Point3d(50.719646350455257, -155.88978421419571, 0.0)
    cylinderBuilder64.Origin = origin64
    
    vector64 = NXOpen.Vector3d(0.0, 0.0, 1.0)
    cylinderBuilder64.Direction = vector64
    
    booleanOperation64 = cylinderBuilder64.BooleanOption
    
    booleanOperation64.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Create
    
    nXObject125 = cylinderBuilder64.Commit()
    
    cylinder64 = nXObject125
    bodies64 = cylinder64.GetBodies()
    
    cylinderBuilder64.Destroy()
    
    part126 = theSession.Parts.Work
    
    booleanBuilder62 = workPart.Features.CreateBooleanBuilder(NXOpen.Features.BooleanFeature.Null)
    
    booleanBuilder62.Target = bodies35[0]
    
    booleanBuilder62.Tool = bodies64[0]
    
    booleanBuilder62.Operation = NXOpen.Features.Feature.BooleanType.Subtract
    
    nXObject126 = booleanBuilder62.Commit()
    
    booleanBuilder62.Destroy()
    
    part127 = theSession.Parts.Work
    
    cylinderBuilder65 = workPart.Features.CreateCylinderBuilder(NXOpen.Features.Feature.Null)
    
    expression129 = cylinderBuilder65.Diameter
    
    expression129.RightHandSide = "12.2"
    
    expression130 = cylinderBuilder65.Height
    
    expression130.RightHandSide = "121.99999999999999"
    
    origin65 = NXOpen.Point3d(56.356651483188493, -145.34368937427044, 0.0)
    cylinderBuilder65.Origin = origin65
    
    vector65 = NXOpen.Vector3d(0.0, 0.0, 1.0)
    cylinderBuilder65.Direction = vector65
    
    booleanOperation65 = cylinderBuilder65.BooleanOption
    
    booleanOperation65.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Create
    
    nXObject127 = cylinderBuilder65.Commit()
    
    cylinder65 = nXObject127
    bodies65 = cylinder65.GetBodies()
    
    cylinderBuilder65.Destroy()
    
    part128 = theSession.Parts.Work
    
    booleanBuilder63 = workPart.Features.CreateBooleanBuilderUsingCollector(NXOpen.Features.BooleanFeature.Null)
    
    booleanBuilder63.Target = bodies35[0]
    
    booleanBuilder63.Tool = bodies65[0]
    
    booleanBuilder63.Operation = NXOpen.Features.Feature.BooleanType.Unite
    
    nXObject128 = booleanBuilder63.Commit()
    
    booleanBuilder63.Destroy()
    
    part129 = theSession.Parts.Work
    
    cylinderBuilder66 = workPart.Features.CreateCylinderBuilder(NXOpen.Features.Feature.Null)
    
    expression131 = cylinderBuilder66.Diameter
    
    expression131.RightHandSide = "12.2"
    
    expression132 = cylinderBuilder66.Height
    
    expression132.RightHandSide = "121.99999999999999"
    
    origin66 = NXOpen.Point3d(59.827902104597044, -133.90050964298385, 0.0)
    cylinderBuilder66.Origin = origin66
    
    vector66 = NXOpen.Vector3d(0.0, 0.0, 1.0)
    cylinderBuilder66.Direction = vector66
    
    booleanOperation66 = cylinderBuilder66.BooleanOption
    
    booleanOperation66.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Create
    
    nXObject129 = cylinderBuilder66.Commit()
    
    cylinder66 = nXObject129
    bodies66 = cylinder66.GetBodies()
    
    cylinderBuilder66.Destroy()
    
    part130 = theSession.Parts.Work
    
    booleanBuilder64 = workPart.Features.CreateBooleanBuilder(NXOpen.Features.BooleanFeature.Null)
    
    booleanBuilder64.Target = bodies35[0]
    
    booleanBuilder64.Tool = bodies66[0]
    
    booleanBuilder64.Operation = NXOpen.Features.Feature.BooleanType.Subtract
    
    nXObject130 = booleanBuilder64.Commit()
    
    booleanBuilder64.Destroy()
    
    part131 = theSession.Parts.Work
    
    cylinderBuilder67 = workPart.Features.CreateCylinderBuilder(NXOpen.Features.Feature.Null)
    
    expression133 = cylinderBuilder67.Diameter
    
    expression133.RightHandSide = "12.2"
    
    expression134 = cylinderBuilder67.Height
    
    expression134.RightHandSide = "121.99999999999999"
    
    origin67 = NXOpen.Point3d(60.999999999999993, -122.0, 0.0)
    cylinderBuilder67.Origin = origin67
    
    vector67 = NXOpen.Vector3d(0.0, 0.0, 1.0)
    cylinderBuilder67.Direction = vector67
    
    booleanOperation67 = cylinderBuilder67.BooleanOption
    
    booleanOperation67.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Create
    
    nXObject131 = cylinderBuilder67.Commit()
    
    cylinder67 = nXObject131
    bodies67 = cylinder67.GetBodies()
    
    cylinderBuilder67.Destroy()
    
    part132 = theSession.Parts.Work
    
    booleanBuilder65 = workPart.Features.CreateBooleanBuilderUsingCollector(NXOpen.Features.BooleanFeature.Null)
    
    booleanBuilder65.Target = bodies35[0]
    
    booleanBuilder65.Tool = bodies67[0]
    
    booleanBuilder65.Operation = NXOpen.Features.Feature.BooleanType.Unite
    
    nXObject132 = booleanBuilder65.Commit()
    
    booleanBuilder65.Destroy()
    
    part133 = theSession.Parts.Work
    
    cylinderBuilder68 = workPart.Features.CreateCylinderBuilder(NXOpen.Features.Feature.Null)
    
    expression135 = cylinderBuilder68.Diameter
    
    expression135.RightHandSide = "4.066666666666666"
    
    expression136 = cylinderBuilder68.Height
    
    expression136.RightHandSide = "121.99999999999999"
    
    origin68 = NXOpen.Point3d(0.0, -121.99999999999999, 0.0)
    cylinderBuilder68.Origin = origin68
    
    vector68 = NXOpen.Vector3d(0.0, 0.0, 1.0)
    cylinderBuilder68.Direction = vector68
    
    booleanOperation68 = cylinderBuilder68.BooleanOption
    
    booleanOperation68.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Create
    
    nXObject133 = cylinderBuilder68.Commit()
    
    cylinder68 = nXObject133
    bodies68 = cylinder68.GetBodies()
    
    cylinderBuilder68.Destroy()
    
    part134 = theSession.Parts.Work
    
    booleanBuilder66 = workPart.Features.CreateBooleanBuilder(NXOpen.Features.BooleanFeature.Null)
    
    booleanBuilder66.Target = bodies35[0]
    
    booleanBuilder66.Tool = bodies68[0]
    
    booleanBuilder66.Operation = NXOpen.Features.Feature.BooleanType.Subtract
    
    nXObject134 = booleanBuilder66.Commit()
    
    booleanBuilder66.Destroy()
    
    part135 = theSession.Parts.Work
    
    cylinderBuilder69 = workPart.Features.CreateCylinderBuilder(NXOpen.Features.Feature.Null)
    
    expression137 = cylinderBuilder69.Diameter
    
    expression137.RightHandSide = "154.2"
    
    expression138 = cylinderBuilder69.Height
    
    expression138.RightHandSide = "142.0"
    
    origin69 = NXOpen.Point3d(0.0, 0.0, -10.0)
    cylinderBuilder69.Origin = origin69
    
    vector69 = NXOpen.Vector3d(0.0, 0.0, 1.0)
    cylinderBuilder69.Direction = vector69
    
    booleanOperation69 = cylinderBuilder69.BooleanOption
    
    booleanOperation69.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Create
    
    nXObject135 = cylinderBuilder69.Commit()
    
    cylinder69 = nXObject135
    bodies69 = cylinder69.GetBodies()
    
    cylinderBuilder69.Destroy()
    
    part136 = theSession.Parts.Work
    
    blockFeatureBuilder1 = workPart.Features.CreateBlockFeatureBuilder(NXOpen.Features.Feature.Null)
    
    blockFeatureBuilder1.Type = NXOpen.Features.BlockFeatureBuilder.Types.OriginAndEdgeLengths
    
    originPoint1 = NXOpen.Point3d(-166.39999999999998, -60.999999999999993, -10.0)
    blockFeatureBuilder1.SetOriginAndLengths(originPoint1, "332.79999999999995", "60.99999999999999", "142.0")
    
    booleanOperation70 = blockFeatureBuilder1.BooleanOption
    
    booleanOperation70.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Create
    
    xAxis1 = NXOpen.Vector3d(1.0, 0.0, 0.0)
    yAxis1 = NXOpen.Vector3d(0.0, 1.0, 0.0)
    blockFeatureBuilder1.SetOrientation(xAxis1, yAxis1)
    
    nXObject136 = blockFeatureBuilder1.Commit()
    
    block1 = nXObject136
    bodies70 = block1.GetBodies()
    
    blockFeatureBuilder1.Destroy()
    
    part137 = theSession.Parts.Work
    
    booleanBuilder67 = workPart.Features.CreateBooleanBuilderUsingCollector(NXOpen.Features.BooleanFeature.Null)
    
    booleanBuilder67.Target = bodies69[0]
    
    booleanBuilder67.Tool = bodies70[0]
    
    booleanBuilder67.Operation = NXOpen.Features.Feature.BooleanType.Unite
    
    nXObject137 = booleanBuilder67.Commit()
    
    booleanBuilder67.Destroy()
    
    part138 = theSession.Parts.Work
    
    cylinderBuilder70 = workPart.Features.CreateCylinderBuilder(NXOpen.Features.Feature.Null)
    
    expression139 = cylinderBuilder70.Diameter
    
    expression139.RightHandSide = "134.2"
    
    expression140 = cylinderBuilder70.Height
    
    expression140.RightHandSide = "121.99999999999999"
    
    origin70 = NXOpen.Point3d(0.0, 0.0, 0.0)
    cylinderBuilder70.Origin = origin70
    
    vector70 = NXOpen.Vector3d(0.0, 0.0, 1.0)
    cylinderBuilder70.Direction = vector70
    
    booleanOperation71 = cylinderBuilder70.BooleanOption
    
    booleanOperation71.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Create
    
    nXObject138 = cylinderBuilder70.Commit()
    
    cylinder70 = nXObject138
    bodies71 = cylinder70.GetBodies()
    
    cylinderBuilder70.Destroy()
    
    part139 = theSession.Parts.Work
    
    booleanBuilder68 = workPart.Features.CreateBooleanBuilder(NXOpen.Features.BooleanFeature.Null)
    
    booleanBuilder68.Target = bodies69[0]
    
    booleanBuilder68.Tool = bodies71[0]
    
    booleanBuilder68.Operation = NXOpen.Features.Feature.BooleanType.Subtract
    
    nXObject139 = booleanBuilder68.Commit()
    
    booleanBuilder68.Destroy()
    
    part140 = theSession.Parts.Work
    
    blockFeatureBuilder2 = workPart.Features.CreateBlockFeatureBuilder(NXOpen.Features.Feature.Null)
    
    blockFeatureBuilder2.Type = NXOpen.Features.BlockFeatureBuilder.Types.OriginAndEdgeLengths
    
    originPoint2 = NXOpen.Point3d(-166.39999999999998, -60.999999999999993, 0.0)
    blockFeatureBuilder2.SetOriginAndLengths(originPoint2, "332.79999999999995", "50.99999999999999", "122.0")
    
    booleanOperation72 = blockFeatureBuilder2.BooleanOption
    
    booleanOperation72.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Create
    
    xAxis2 = NXOpen.Vector3d(1.0, 0.0, 0.0)
    yAxis2 = NXOpen.Vector3d(0.0, 1.0, 0.0)
    blockFeatureBuilder2.SetOrientation(xAxis2, yAxis2)
    
    nXObject140 = blockFeatureBuilder2.Commit()
    
    block2 = nXObject140
    bodies72 = block2.GetBodies()
    
    blockFeatureBuilder2.Destroy()
    
    part141 = theSession.Parts.Work
    
    booleanBuilder69 = workPart.Features.CreateBooleanBuilder(NXOpen.Features.BooleanFeature.Null)
    
    booleanBuilder69.Target = bodies69[0]
    
    booleanBuilder69.Tool = bodies72[0]
    
    booleanBuilder69.Operation = NXOpen.Features.Feature.BooleanType.Subtract
    
    nXObject141 = booleanBuilder69.Commit()
    
    booleanBuilder69.Destroy()
    
    part142 = theSession.Parts.Work
    
    blockFeatureBuilder3 = workPart.Features.CreateBlockFeatureBuilder(NXOpen.Features.Feature.Null)
    
    blockFeatureBuilder3.Type = NXOpen.Features.BlockFeatureBuilder.Types.OriginAndEdgeLengths
    
    originPoint3 = NXOpen.Point3d(-166.39999999999998, -121.99999999999999, -10.0)
    blockFeatureBuilder3.SetOriginAndLengths(originPoint3, "332.79999999999995", "60.99999999999999", "142.0")
    
    booleanOperation73 = blockFeatureBuilder3.BooleanOption
    
    booleanOperation73.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Create
    
    xAxis3 = NXOpen.Vector3d(1.0, 0.0, 0.0)
    yAxis3 = NXOpen.Vector3d(0.0, 1.0, 0.0)
    blockFeatureBuilder3.SetOrientation(xAxis3, yAxis3)
    
    nXObject142 = blockFeatureBuilder3.Commit()
    
    block3 = nXObject142
    bodies73 = block3.GetBodies()
    
    blockFeatureBuilder3.Destroy()
    
    part143 = theSession.Parts.Work
    
    booleanBuilder70 = workPart.Features.CreateBooleanBuilder(NXOpen.Features.BooleanFeature.Null)
    
    booleanBuilder70.Target = bodies69[0]
    
    booleanBuilder70.Tool = bodies73[0]
    
    booleanBuilder70.Operation = NXOpen.Features.Feature.BooleanType.Subtract
    
    nXObject143 = booleanBuilder70.Commit()
    
    booleanBuilder70.Destroy()
    
    part144 = theSession.Parts.Work
    
    cylinderBuilder71 = workPart.Features.CreateCylinderBuilder(NXOpen.Features.Feature.Null)
    
    expression141 = cylinderBuilder71.Diameter
    
    expression141.RightHandSide = "154.2"
    
    expression142 = cylinderBuilder71.Height
    
    expression142.RightHandSide = "142.0"
    
    origin71 = NXOpen.Point3d(0.0, -121.99999999999999, -10.0)
    cylinderBuilder71.Origin = origin71
    
    vector71 = NXOpen.Vector3d(0.0, 0.0, 1.0)
    cylinderBuilder71.Direction = vector71
    
    booleanOperation74 = cylinderBuilder71.BooleanOption
    
    booleanOperation74.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Create
    
    nXObject144 = cylinderBuilder71.Commit()
    
    cylinder71 = nXObject144
    bodies74 = cylinder71.GetBodies()
    
    cylinderBuilder71.Destroy()
    
    part145 = theSession.Parts.Work
    
    blockFeatureBuilder4 = workPart.Features.CreateBlockFeatureBuilder(NXOpen.Features.Feature.Null)
    
    blockFeatureBuilder4.Type = NXOpen.Features.BlockFeatureBuilder.Types.OriginAndEdgeLengths
    
    originPoint4 = NXOpen.Point3d(-166.39999999999998, -121.99999999999999, -10.0)
    blockFeatureBuilder4.SetOriginAndLengths(originPoint4, "332.79999999999995", "60.99999999999999", "142.0")
    
    booleanOperation75 = blockFeatureBuilder4.BooleanOption
    
    booleanOperation75.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Create
    
    xAxis4 = NXOpen.Vector3d(1.0, 0.0, 0.0)
    yAxis4 = NXOpen.Vector3d(0.0, 1.0, 0.0)
    blockFeatureBuilder4.SetOrientation(xAxis4, yAxis4)
    
    nXObject145 = blockFeatureBuilder4.Commit()
    
    block4 = nXObject145
    bodies75 = block4.GetBodies()
    
    blockFeatureBuilder4.Destroy()
    
    part146 = theSession.Parts.Work
    
    booleanBuilder71 = workPart.Features.CreateBooleanBuilderUsingCollector(NXOpen.Features.BooleanFeature.Null)
    
    booleanBuilder71.Target = bodies74[0]
    
    booleanBuilder71.Tool = bodies75[0]
    
    booleanBuilder71.Operation = NXOpen.Features.Feature.BooleanType.Unite
    
    nXObject146 = booleanBuilder71.Commit()
    
    booleanBuilder71.Destroy()
    
    part147 = theSession.Parts.Work
    
    cylinderBuilder72 = workPart.Features.CreateCylinderBuilder(NXOpen.Features.Feature.Null)
    
    expression143 = cylinderBuilder72.Diameter
    
    expression143.RightHandSide = "134.2"
    
    expression144 = cylinderBuilder72.Height
    
    expression144.RightHandSide = "121.99999999999999"
    
    origin72 = NXOpen.Point3d(0.0, -121.99999999999999, 0.0)
    cylinderBuilder72.Origin = origin72
    
    vector72 = NXOpen.Vector3d(0.0, 0.0, 1.0)
    cylinderBuilder72.Direction = vector72
    
    booleanOperation76 = cylinderBuilder72.BooleanOption
    
    booleanOperation76.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Create
    
    nXObject147 = cylinderBuilder72.Commit()
    
    cylinder72 = nXObject147
    bodies76 = cylinder72.GetBodies()
    
    cylinderBuilder72.Destroy()
    
    part148 = theSession.Parts.Work
    
    booleanBuilder72 = workPart.Features.CreateBooleanBuilder(NXOpen.Features.BooleanFeature.Null)
    
    booleanBuilder72.Target = bodies74[0]
    
    booleanBuilder72.Tool = bodies76[0]
    
    booleanBuilder72.Operation = NXOpen.Features.Feature.BooleanType.Subtract
    
    nXObject148 = booleanBuilder72.Commit()
    
    booleanBuilder72.Destroy()
    
    part149 = theSession.Parts.Work
    
    blockFeatureBuilder5 = workPart.Features.CreateBlockFeatureBuilder(NXOpen.Features.Feature.Null)
    
    blockFeatureBuilder5.Type = NXOpen.Features.BlockFeatureBuilder.Types.OriginAndEdgeLengths
    
    originPoint5 = NXOpen.Point3d(-166.39999999999998, -111.99999999999999, 0.0)
    blockFeatureBuilder5.SetOriginAndLengths(originPoint5, "332.79999999999995", "50.99999999999999", "122.0")
    
    booleanOperation77 = blockFeatureBuilder5.BooleanOption
    
    booleanOperation77.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Create
    
    xAxis5 = NXOpen.Vector3d(1.0, 0.0, 0.0)
    yAxis5 = NXOpen.Vector3d(0.0, 1.0, 0.0)
    blockFeatureBuilder5.SetOrientation(xAxis5, yAxis5)
    
    nXObject149 = blockFeatureBuilder5.Commit()
    
    block5 = nXObject149
    bodies77 = block5.GetBodies()
    
    blockFeatureBuilder5.Destroy()
    
    part150 = theSession.Parts.Work
    
    booleanBuilder73 = workPart.Features.CreateBooleanBuilder(NXOpen.Features.BooleanFeature.Null)
    
    booleanBuilder73.Target = bodies74[0]
    
    booleanBuilder73.Tool = bodies77[0]
    
    booleanBuilder73.Operation = NXOpen.Features.Feature.BooleanType.Subtract
    
    nXObject150 = booleanBuilder73.Commit()
    
    booleanBuilder73.Destroy()
    
    part151 = theSession.Parts.Work
    
    blockFeatureBuilder6 = workPart.Features.CreateBlockFeatureBuilder(NXOpen.Features.Feature.Null)
    
    blockFeatureBuilder6.Type = NXOpen.Features.BlockFeatureBuilder.Types.OriginAndEdgeLengths
    
    originPoint6 = NXOpen.Point3d(-166.39999999999998, -60.999999999999993, -10.0)
    blockFeatureBuilder6.SetOriginAndLengths(originPoint6, "332.79999999999995", "60.99999999999999", "142.0")
    
    booleanOperation78 = blockFeatureBuilder6.BooleanOption
    
    booleanOperation78.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Create
    
    xAxis6 = NXOpen.Vector3d(1.0, 0.0, 0.0)
    yAxis6 = NXOpen.Vector3d(0.0, 1.0, 0.0)
    blockFeatureBuilder6.SetOrientation(xAxis6, yAxis6)
    
    nXObject151 = blockFeatureBuilder6.Commit()
    
    block6 = nXObject151
    bodies78 = block6.GetBodies()
    
    blockFeatureBuilder6.Destroy()
    
    part152 = theSession.Parts.Work
    
    booleanBuilder74 = workPart.Features.CreateBooleanBuilder(NXOpen.Features.BooleanFeature.Null)
    
    booleanBuilder74.Target = bodies74[0]
    
    booleanBuilder74.Tool = bodies78[0]
    
    booleanBuilder74.Operation = NXOpen.Features.Feature.BooleanType.Subtract
    
    nXObject152 = booleanBuilder74.Commit()
    
    booleanBuilder74.Destroy()
    
    # ----------------------------------------------
    #   Menu: Edit->Show and Hide->Hide...
    # ----------------------------------------------
    markId1 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Hide")
    
    objects1 = [NXOpen.DisplayableObject.Null] * 1 
    objects1[0] = bodies69[0]
    theSession.DisplayManager.BlankObjects(objects1)
    
    workPart.ModelingViews.WorkView.FitAfterShowOrHide(NXOpen.View.ShowOrHideType.HideOnly)
    
    # ----------------------------------------------
    #   Menu: Edit->Show and Hide->Hide...
    # ----------------------------------------------
    markId2 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Hide")
    
    objects2 = [NXOpen.DisplayableObject.Null] * 1 
    objects2[0] = bodies74[0]
    theSession.DisplayManager.BlankObjects(objects2)
    
    workPart.ModelingViews.WorkView.FitAfterShowOrHide(NXOpen.View.ShowOrHideType.HideOnly)
    
    # ----------------------------------------------
    #   Menu: Application->Simulation->Motion
    # ----------------------------------------------
    markId3 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Enter Motion")
    
    theSession.ApplicationSwitchImmediate("UG_APP_MECHANISMS")
    
    globalSelectionBuilder1 = theSession.MotionSession.MotionMethods.GetGlobalSelectionBuilder(workPart)
    
    baseTemplateManager1 = theSession.XYPlotManager.TemplateManager
    
    # ----------------------------------------------
    #   Menu: File->Utilities->New Simulation...
    # ----------------------------------------------
    markId4 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")
    
    fileNew1 = theSession.Parts.FileNew()
    
    theSession.SetUndoMarkName(markId4, "New Simulation Dialog")
    
    markId5 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "New Simulation")
    
    theSession.DeleteUndoMark(markId5, None)
    
    markId6 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "New Simulation")
    
    fileNew1.TemplateFileName = "Simcenter 3D Motion"
    
    fileNew1.UseBlankTemplate = True
    
    fileNew1.ApplicationName = "MotionTemplate"
    
    fileNew1.Units = NXOpen.Part.Units.Millimeters
    
    fileNew1.RelationType = ""
    
    fileNew1.UsesMasterModel = "Yes"
    
    fileNew1.TemplateType = NXOpen.FileNewTemplateType.Item
    
    fileNew1.TemplatePresentationName = ""
    
    fileNew1.ItemType = ""
    
    fileNew1.Specialization = ""
    
    fileNew1.SetCanCreateAltrep(False)
    
    fileNew1.NewFileName = "M:\\Desktop\\TMM4270\\TMM4270-Automatisering\\KBE\\Python\\Animation\\model1_motion2.sim"
    
    fileNew1.MasterFileName = "model1"
    
    fileNew1.MakeDisplayedPart = True
    
    fileNew1.DisplayPartOption = NXOpen.DisplayPartOption.AllowAdditional
    
    theSession.DeleteUndoMark(markId6, None)
    
    theSession.SetUndoMarkName(markId4, "New Simulation")
    
    baseTemplateManager2 = theSession.XYPlotManager.TemplateManager
    
    nXObject153 = fileNew1.Commit()
    
    workPart = theSession.Parts.Work # model1_motion2
    displayPart = theSession.Parts.Display # model1_motion2
    markId7 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Start")
    
    theSession.SetUndoMarkName(markId7, "Environment Dialog")
    
    # ----------------------------------------------
    #   Dialog Begin Environment
    # ----------------------------------------------
    markId8 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Environment")
    
    theSession.DeleteUndoMark(markId8, None)
    
    markId9 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Environment")
    
    theSession.MotionSession.Environments.SetSolver(NXOpen.Motion.MotionEnvironment.Solver.Simcenter)
    
    theSession.MotionSession.Environments.SetAnalysisType(NXOpen.Motion.MotionEnvironment.Analysis.Dynamics)
    
    theSession.MotionSession.Environments.SetComponentBasedMechanism(False)
    
    theSession.MotionSession.Environments.SetJointWizardStatus(NXOpen.Motion.MotionEnvironment.JointWizardStatus.On)
    
    nErrs1 = theSession.UpdateManager.DoUpdate(markId7)
    
    theSession.DeleteUndoMark(markId9, None)
    
    theSession.SetUndoMarkName(markId7, "Environment")
    
    theSession.DeleteUndoMark(markId7, None)
    
    theSession.MotionSession.InitializeSimulation(workPart)
    
    physicsConversionBuilder1 = theSession.MotionSession.CreatePhysicsConversionBuilder(workPart)
    
    animationConversionBuilder1 = theSession.MotionSession.CreateAnimationConversionBuilder(workPart)
    
    physicsConversionBuilder1.Destroy()
    
    animationConversionBuilder1.Destroy()
    
    fileNew1.Destroy()
    
    # ----------------------------------------------
    #   Menu: Insert->Motion Body...
    # ----------------------------------------------
    markId10 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")
    
    linkBuilder1 = workPart.MotionManager.Links.CreateLinkBuilder(NXOpen.Motion.Link.Null)
    
    linkBuilder1.MassProperty.MassType = NXOpen.Motion.LinkMassProperty.MassPropertyType.UserDefined
    
    linkBuilder1.MassProperty.MassExpression.SetFormula("1")
    
    linkBuilder1.MassProperty.IxxExpression.SetFormula("1")
    
    linkBuilder1.MassProperty.IyyExpression.SetFormula("1")
    
    linkBuilder1.MassProperty.IzzExpression.SetFormula("1")
    
    linkBuilder1.MassProperty.IxyExpression.SetFormula("0")
    
    linkBuilder1.MassProperty.IxzExpression.SetFormula("0")
    
    linkBuilder1.MassProperty.IyzExpression.SetFormula("0")
    
    try:
        # This expression cannot be modified because it is locked.
        linkBuilder1.MassProperty.AutoMassExpression.SetFormula("0")
    except NXOpen.NXException as ex:
        ex.AssertErrorCode(1050049)
        
    try:
        # This expression cannot be modified because it is locked.
        linkBuilder1.MassProperty.AutoIxxExpression.SetFormula("0")
    except NXOpen.NXException as ex:
        ex.AssertErrorCode(1050049)
        
    try:
        # This expression cannot be modified because it is locked.
        linkBuilder1.MassProperty.AutoIyyExpression.SetFormula("0")
    except NXOpen.NXException as ex:
        ex.AssertErrorCode(1050049)
        
    try:
        # This expression cannot be modified because it is locked.
        linkBuilder1.MassProperty.AutoIzzExpression.SetFormula("0")
    except NXOpen.NXException as ex:
        ex.AssertErrorCode(1050049)
        
    try:
        # This expression cannot be modified because it is locked.
        linkBuilder1.MassProperty.AutoIxyExpression.SetFormula("0")
    except NXOpen.NXException as ex:
        ex.AssertErrorCode(1050049)
        
    try:
        # This expression cannot be modified because it is locked.
        linkBuilder1.MassProperty.AutoIxzExpression.SetFormula("0")
    except NXOpen.NXException as ex:
        ex.AssertErrorCode(1050049)
        
    try:
        # This expression cannot be modified because it is locked.
        linkBuilder1.MassProperty.AutoIyzExpression.SetFormula("0")
    except NXOpen.NXException as ex:
        ex.AssertErrorCode(1050049)
        
    linkBuilder1.InitialVelocity.TranslateExpression.SetFormula("0")
    
    linkBuilder1.InitialVelocity.RotateExpression.SetFormula("0")
    
    linkBuilder1.InitialVelocity.WxExpression.SetFormula("0")
    
    linkBuilder1.InitialVelocity.WyExpression.SetFormula("0")
    
    linkBuilder1.InitialVelocity.WzExpression.SetFormula("0")
    
    theSession.SetUndoMarkName(markId10, "Motion Body Dialog")
    
    unit1 = workPart.UnitCollection.FindObject("MilliMeter")
    expression145 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    expression146 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    expression147 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    globalSelectionBuilder2 = theSession.MotionSession.MotionMethods.GetGlobalSelectionBuilder(workPart)
    
    selectTaggedObjectList1 = globalSelectionBuilder2.Selection
    
    component1 = workPart.ComponentAssembly.RootComponent.FindObject("COMPONENT model1 1")
    body1 = component1.FindObject("PROTO#.Bodies|CYLINDER(68)")
    added1 = linkBuilder1.Geometries.Add(body1)
    
    globalSelectionBuilder3 = theSession.MotionSession.MotionMethods.GetGlobalSelectionBuilder(workPart)
    
    selectTaggedObjectList2 = globalSelectionBuilder3.Selection
    
    linkBuilder1.MassProperty.CopyGeometryMassToUserDefinedMassProperty()
    
    linkBuilder1.MassProperty.MassExpression.SetFormula("11.19579609901")
    
    linkBuilder1.MassProperty.IxxExpression.SetFormula("24633.44382")
    
    linkBuilder1.MassProperty.IyyExpression.SetFormula("24632.06842")
    
    linkBuilder1.MassProperty.IzzExpression.SetFormula("21492.47405")
    
    markId11 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Motion Body")
    
    theSession.DeleteUndoMark(markId11, None)
    
    markId12 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Motion Body")
    
    linkBuilder1.InitialVelocity.TranslateVector = NXOpen.Direction.Null
    
    linkBuilder1.InitialVelocity.RotateVector = NXOpen.Direction.Null
    
    nXObject154 = linkBuilder1.Commit()
    
    theSession.DeleteUndoMark(markId12, None)
    
    theSession.SetUndoMarkName(markId10, "Motion Body")
    
    linkBuilder1.Destroy()
    
    workPart.MeasureManager.SetPartTransientModification()
    
    workPart.Expressions.Delete(expression147)
    
    workPart.MeasureManager.ClearPartTransientModification()
    
    workPart.MeasureManager.SetPartTransientModification()
    
    workPart.Expressions.Delete(expression145)
    
    workPart.MeasureManager.ClearPartTransientModification()
    
    workPart.MeasureManager.SetPartTransientModification()
    
    workPart.Expressions.Delete(expression146)
    
    workPart.MeasureManager.ClearPartTransientModification()
    
    # ----------------------------------------------
    #   Menu: Insert->Motion Body...
    # ----------------------------------------------
    markId13 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")
    
    linkBuilder2 = workPart.MotionManager.Links.CreateLinkBuilder(NXOpen.Motion.Link.Null)
    
    linkBuilder2.MassProperty.MassType = NXOpen.Motion.LinkMassProperty.MassPropertyType.UserDefined
    
    linkBuilder2.MassProperty.MassExpression.SetFormula("11.19579609901")
    
    linkBuilder2.MassProperty.IxxExpression.SetFormula("24633.44382")
    
    linkBuilder2.MassProperty.IyyExpression.SetFormula("24632.06842")
    
    linkBuilder2.MassProperty.IzzExpression.SetFormula("21492.47405")
    
    linkBuilder2.MassProperty.IxyExpression.SetFormula("0")
    
    linkBuilder2.MassProperty.IxzExpression.SetFormula("0")
    
    linkBuilder2.MassProperty.IyzExpression.SetFormula("0")
    
    try:
        # This expression cannot be modified because it is locked.
        linkBuilder2.MassProperty.AutoMassExpression.SetFormula("0")
    except NXOpen.NXException as ex:
        ex.AssertErrorCode(1050049)
        
    try:
        # This expression cannot be modified because it is locked.
        linkBuilder2.MassProperty.AutoIxxExpression.SetFormula("0")
    except NXOpen.NXException as ex:
        ex.AssertErrorCode(1050049)
        
    try:
        # This expression cannot be modified because it is locked.
        linkBuilder2.MassProperty.AutoIyyExpression.SetFormula("0")
    except NXOpen.NXException as ex:
        ex.AssertErrorCode(1050049)
        
    try:
        # This expression cannot be modified because it is locked.
        linkBuilder2.MassProperty.AutoIzzExpression.SetFormula("0")
    except NXOpen.NXException as ex:
        ex.AssertErrorCode(1050049)
        
    try:
        # This expression cannot be modified because it is locked.
        linkBuilder2.MassProperty.AutoIxyExpression.SetFormula("0")
    except NXOpen.NXException as ex:
        ex.AssertErrorCode(1050049)
        
    try:
        # This expression cannot be modified because it is locked.
        linkBuilder2.MassProperty.AutoIxzExpression.SetFormula("0")
    except NXOpen.NXException as ex:
        ex.AssertErrorCode(1050049)
        
    try:
        # This expression cannot be modified because it is locked.
        linkBuilder2.MassProperty.AutoIyzExpression.SetFormula("0")
    except NXOpen.NXException as ex:
        ex.AssertErrorCode(1050049)
        
    linkBuilder2.InitialVelocity.TranslateExpression.SetFormula("0")
    
    linkBuilder2.InitialVelocity.RotateExpression.SetFormula("0")
    
    linkBuilder2.InitialVelocity.WxExpression.SetFormula("0")
    
    linkBuilder2.InitialVelocity.WyExpression.SetFormula("0")
    
    linkBuilder2.InitialVelocity.WzExpression.SetFormula("0")
    
    theSession.SetUndoMarkName(markId13, "Motion Body Dialog")
    
    expression148 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    expression149 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    expression150 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    globalSelectionBuilder4 = theSession.MotionSession.MotionMethods.GetGlobalSelectionBuilder(workPart)
    
    selectTaggedObjectList3 = globalSelectionBuilder4.Selection
    
    body2 = component1.FindObject("PROTO#.Bodies|CYLINDER(1)")
    added2 = linkBuilder2.Geometries.Add(body2)
    
    linkBuilder2.MassProperty.CopyGeometryMassToUserDefinedMassProperty()
    
    markId14 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Motion Body")
    
    globalSelectionBuilder5 = theSession.MotionSession.MotionMethods.GetGlobalSelectionBuilder(workPart)
    
    selectTaggedObjectList4 = globalSelectionBuilder5.Selection
    
    theSession.DeleteUndoMark(markId14, None)
    
    markId15 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Motion Body")
    
    linkBuilder2.InitialVelocity.TranslateVector = NXOpen.Direction.Null
    
    linkBuilder2.InitialVelocity.RotateVector = NXOpen.Direction.Null
    
    nXObject155 = linkBuilder2.Commit()
    
    theSession.DeleteUndoMark(markId15, None)
    
    theSession.SetUndoMarkName(markId13, "Motion Body")
    
    linkBuilder2.Destroy()
    
    workPart.MeasureManager.SetPartTransientModification()
    
    workPart.Expressions.Delete(expression150)
    
    workPart.MeasureManager.ClearPartTransientModification()
    
    workPart.MeasureManager.SetPartTransientModification()
    
    workPart.Expressions.Delete(expression148)
    
    workPart.MeasureManager.ClearPartTransientModification()
    
    workPart.MeasureManager.SetPartTransientModification()
    
    workPart.Expressions.Delete(expression149)
    
    workPart.MeasureManager.ClearPartTransientModification()
    
    # ----------------------------------------------
    #   Menu: Insert->Joint...
    # ----------------------------------------------
    markId16 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")
    
    jointBuilder1 = workPart.MotionManager.Joints.CreateJointBuilder(NXOpen.Motion.Joint.Null)
    
    jointBuilder1.JointDefine.UpperLimitExpression.SetFormula("0")
    
    jointBuilder1.JointDefine.LowerLimitExpression.SetFormula("0")
    
    jointBuilder1.JointDefine.UpperLimitAngleExpression.SetFormula("0")
    
    jointBuilder1.JointDefine.LowerLimitAngleExpression.SetFormula("0")
    
    jointBuilder1.JointDefine.ScrewRatioExpression.SetFormula("1")
    
    jointBuilder1.JointFriction.AdamsFriction.MuStaticExpression.SetFormula("0")
    
    jointBuilder1.JointFriction.AdamsFriction.MuDynamicExpression.SetFormula("0.1")
    
    jointBuilder1.JointFriction.AdamsFriction.StictionTransitionVelocityExpression.SetFormula("0.1")
    
    jointBuilder1.JointFriction.AdamsFriction.MaxStictionDeformationExpression.SetFormula("0.01")
    
    jointBuilder1.JointFriction.AdamsFriction.BallRadiusExpression.SetFormula("1")
    
    jointBuilder1.JointFriction.AdamsFriction.PinRadiusExpression.SetFormula("1")
    
    jointBuilder1.JointFriction.AdamsFriction.BendingArmExpression.SetFormula("1")
    
    jointBuilder1.JointFriction.AdamsFriction.FrictionArmExpression.SetFormula("1")
    
    jointBuilder1.JointFriction.AdamsFriction.ReactionArmExpression.SetFormula("1")
    
    jointBuilder1.JointFriction.AdamsFriction.InitialOverlapExpression.SetFormula("1000")
    
    jointBuilder1.JointFriction.AdamsFriction.ForcePreloadExpression.SetFormula("0")
    
    jointBuilder1.JointFriction.AdamsFriction.TorquePreloadExpression.SetFormula("0")
    
    jointBuilder1.JointFriction.RecurDynFriction.MuStaticExpression.SetFormula("0")
    
    jointBuilder1.JointFriction.RecurDynFriction.MuDynamicExpression.SetFormula("0.1")
    
    jointBuilder1.JointFriction.RecurDynFriction.StictionTransitionVelocityExpression.SetFormula("0.1")
    
    jointBuilder1.JointFriction.RecurDynFriction.MaxStictionDeformationExpression.SetFormula("0.01")
    
    jointBuilder1.JointFriction.RecurDynFriction.BallRadiusExpression.SetFormula("1")
    
    jointBuilder1.JointFriction.RecurDynFriction.PinRadiusExpression.SetFormula("1")
    
    jointBuilder1.JointFriction.RecurDynFriction.BendingArmExpression.SetFormula("1")
    
    jointBuilder1.JointFriction.RecurDynFriction.FrictionArmExpression.SetFormula("1")
    
    jointBuilder1.JointFriction.RecurDynFriction.ReactionArmExpression.SetFormula("10")
    
    jointBuilder1.JointFriction.RecurDynFriction.InitialOverlapExpression.SetFormula("1000")
    
    jointBuilder1.JointFriction.RecurDynFriction.ForcePreloadExpression.SetFormula("0")
    
    jointBuilder1.JointFriction.RecurDynFriction.TorquePreloadExpression.SetFormula("0")
    
    jointBuilder1.JointFriction.RecurDynFriction.MaxFrictionForceExpression.SetFormula("0")
    
    jointBuilder1.JointFriction.RecurDynFriction.MaxFrictionTorqueExpression.SetFormula("0")
    
    jointBuilder1.JointFriction.LmsFriction.MuStatic.SetFormula("0")
    
    jointBuilder1.JointFriction.LmsFriction.MuDynamic.SetFormula("0.1")
    
    jointBuilder1.JointFriction.LmsFriction.TranslationalStictionTransitionVelocity.SetFormula("0.1")
    
    jointBuilder1.JointFriction.LmsFriction.RotationalStictionTransitionVelocity.SetFormula("0.0572957795130824")
    
    jointBuilder1.JointFriction.LmsFriction.PinRadius.SetFormula("1")
    
    jointBuilder1.JointFriction.LmsFriction.BendingReactionArm.SetFormula("1")
    
    jointBuilder1.JointFriction.LmsFriction.FrictionArm.SetFormula("1")
    
    jointBuilder1.JointFriction.LmsFriction.ReactionArm.SetFormula("10")
    
    jointBuilder1.JointFriction.LmsFriction.InitialOverlap.SetFormula("1000")
    
    jointBuilder1.JointFriction.LmsFriction.BallRadius.SetFormula("1")
    
    jointBuilder1.JointMultiDrivers.MotionEulerAngle1.DisplacementExpression.SetFormula("0")
    
    jointBuilder1.JointMultiDrivers.MotionEulerAngle1.VelocityExpression.SetFormula("0")
    
    jointBuilder1.JointMultiDrivers.MotionEulerAngle1.AccelerationExpression.SetFormula("0")
    
    jointBuilder1.JointMultiDrivers.MotionEulerAngle1.JerkExpression.SetFormula("0")
    
    jointBuilder1.JointMultiDrivers.MotionEulerAngle1.AmplitudeExpression.SetFormula("0")
    
    jointBuilder1.JointMultiDrivers.MotionEulerAngle1.FrequencyExpression.SetFormula("0")
    
    jointBuilder1.JointMultiDrivers.MotionEulerAngle1.PhaseAngleExpression.SetFormula("0")
    
    jointBuilder1.JointMultiDrivers.MotionEulerAngle1.HarmonicDisplacementExpression.SetFormula("0")
    
    jointBuilder1.JointMultiDrivers.MotionEulerAngle1.InitialDisplacementExpression.SetFormula("0")
    
    jointBuilder1.JointMultiDrivers.MotionEulerAngle1.InitialVelocityExpression.SetFormula("0")
    
    jointBuilder1.JointMultiDrivers.MotionEulerAngle1.ControlInitialVelocityExpression.SetFormula("0")
    
    jointBuilder1.JointMultiDrivers.MotionEulerAngle1.ControlInitialAccelerationExpression.SetFormula("0")
    
    jointBuilder1.JointMultiDrivers.MotionTranslationZ.DisplacementExpression.SetFormula("0")
    
    jointBuilder1.JointMultiDrivers.MotionTranslationZ.VelocityExpression.SetFormula("0")
    
    jointBuilder1.JointMultiDrivers.MotionTranslationZ.AccelerationExpression.SetFormula("0")
    
    jointBuilder1.JointMultiDrivers.MotionTranslationZ.JerkExpression.SetFormula("0")
    
    jointBuilder1.JointMultiDrivers.MotionTranslationZ.AmplitudeExpression.SetFormula("0")
    
    jointBuilder1.JointMultiDrivers.MotionTranslationZ.FrequencyExpression.SetFormula("0")
    
    jointBuilder1.JointMultiDrivers.MotionTranslationZ.PhaseAngleExpression.SetFormula("0")
    
    jointBuilder1.JointMultiDrivers.MotionTranslationZ.HarmonicDisplacementExpression.SetFormula("0")
    
    jointBuilder1.JointMultiDrivers.MotionTranslationZ.InitialDisplacementExpression.SetFormula("0")
    
    jointBuilder1.JointMultiDrivers.MotionTranslationZ.InitialVelocityExpression.SetFormula("0")
    
    jointBuilder1.JointMultiDrivers.MotionTranslationZ.ControlInitialVelocityExpression.SetFormula("0")
    
    jointBuilder1.JointMultiDrivers.MotionTranslationZ.ControlInitialAccelerationExpression.SetFormula("0")
    
    jointBuilder1.JointMultiDrivers.MotionPointOnCurve.DisplacementExpression.SetFormula("0")
    
    jointBuilder1.JointMultiDrivers.MotionPointOnCurve.VelocityExpression.SetFormula("0")
    
    jointBuilder1.JointMultiDrivers.MotionPointOnCurve.AccelerationExpression.SetFormula("0")
    
    jointBuilder1.JointMultiDrivers.MotionPointOnCurve.JerkExpression.SetFormula("0")
    
    jointBuilder1.JointMultiDrivers.MotionPointOnCurve.AmplitudeExpression.SetFormula("0")
    
    jointBuilder1.JointMultiDrivers.MotionPointOnCurve.FrequencyExpression.SetFormula("0")
    
    jointBuilder1.JointMultiDrivers.MotionPointOnCurve.PhaseAngleExpression.SetFormula("0")
    
    jointBuilder1.JointMultiDrivers.MotionPointOnCurve.HarmonicDisplacementExpression.SetFormula("0")
    
    jointBuilder1.JointMultiDrivers.MotionPointOnCurve.InitialDisplacementExpression.SetFormula("0")
    
    jointBuilder1.JointMultiDrivers.MotionPointOnCurve.InitialVelocityExpression.SetFormula("0")
    
    jointBuilder1.JointMultiDrivers.MotionPointOnCurve.ControlInitialVelocityExpression.SetFormula("0")
    
    jointBuilder1.JointMultiDrivers.MotionPointOnCurve.ControlInitialAccelerationExpression.SetFormula("0")
    
    theSession.SetUndoMarkName(markId16, "Joint Dialog")
    
    expression151 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    expression152 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    expression153 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    expression154 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    expression155 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    expression156 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    jointBuilder1.JointDefine.ScrewSplineFunction = NXOpen.CAE.Function.Null
    
    jointBuilder1.JointDefine.ScrewDisplCurveFunction = NXOpen.CAE.Function.Null
    
    jointBuilder1.JointMultiDrivers.MotionEulerAngle1.Function = NXOpen.NXObject.Null
    
    jointBuilder1.JointMultiDrivers.MotionEulerAngle1.Function = NXOpen.NXObject.Null
    
    jointBuilder1.JointMultiDrivers.MotionTranslationZ.Function = NXOpen.NXObject.Null
    
    jointBuilder1.JointMultiDrivers.MotionTranslationZ.Function = NXOpen.NXObject.Null
    
    jointBuilder1.JointMultiDrivers.MotionPointOnCurve.Function = NXOpen.NXObject.Null
    
    jointBuilder1.JointMultiDrivers.MotionPointOnCurve.Function = NXOpen.NXObject.Null
    
    jointBuilder1.JointMultiDrivers.MotionEulerAngle1.Function = NXOpen.NXObject.Null
    
    jointBuilder1.JointMultiDrivers.MotionTranslationZ.Function = NXOpen.NXObject.Null
    
    jointBuilder1.JointMultiDrivers.MotionPointOnCurve.Function = NXOpen.NXObject.Null
    
    globalSelectionBuilder6 = theSession.MotionSession.MotionMethods.GetGlobalSelectionBuilder(workPart)
    
    selectTaggedObjectList5 = globalSelectionBuilder6.Selection
    
    globalSelectionBuilder7 = theSession.MotionSession.MotionMethods.GetGlobalSelectionBuilder(workPart)
    
    selectTaggedObjectList6 = globalSelectionBuilder7.Selection
    
    globalSelectionBuilder8 = theSession.MotionSession.MotionMethods.GetGlobalSelectionBuilder(workPart)
    
    selectTaggedObjectList7 = globalSelectionBuilder8.Selection
    
    link1 = nXObject154
    jointBuilder1.JointDefine.FirstLinkSelection.Value = link1
    
    globalSelectionBuilder9 = theSession.MotionSession.MotionMethods.GetGlobalSelectionBuilder(workPart)
    
    selectTaggedObjectList8 = globalSelectionBuilder9.Selection
    
    expression157 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    edge1 = cylinder35.FindObject("EDGE * 1 CYLINDER(133) 3 {(-1.0166666666667,-123.7609183210284,122)(2.0333333333333,-122,122)(-1.0166666666667,-120.2390816789716,122) CYLINDER(68)}")
    point1 = workPart.Points.CreatePoint(edge1, NXOpen.SmartObject.UpdateOption.AfterModeling)
    
    edge2 = component1.FindObject("PROTO#.Features|CYLINDER(68)|EDGE * 1 CYLINDER(133) 3 {(-1.0166666666667,-123.7609183210284,122)(2.0333333333333,-122,122)(-1.0166666666667,-120.2390816789716,122) CYLINDER(68)}")
    xform1, nXObject156 = workPart.Xforms.CreateExtractXform(edge2, NXOpen.SmartObject.UpdateOption.AfterModeling, False)
    
    point2 = workPart.Points.CreatePoint(point1, xform1, NXOpen.SmartObject.UpdateOption.AfterModeling)
    
    globalSelectionBuilder10 = theSession.MotionSession.MotionMethods.GetGlobalSelectionBuilder(workPart)
    
    selectTaggedObjectList9 = globalSelectionBuilder10.Selection
    
    partLoadStatus1 = part152.LoadFeatureDataForSelection()
    
    partLoadStatus1.Dispose()
    edge3 = nXObject156
    point3 = workPart.Points.CreatePoint(edge3, NXOpen.SmartObject.UpdateOption.AfterModeling)
    
    xform2, nXObject157 = workPart.Xforms.CreateExtractXform(edge2, NXOpen.SmartObject.UpdateOption.AfterModeling, False)
    
    point4 = workPart.Points.CreatePoint(point3, xform2, NXOpen.SmartObject.UpdateOption.AfterModeling)
    
    jointBuilder1.JointDefine.FirstOrigin = point4
    
    origin73 = NXOpen.Point3d(0.0, -122.0, 121.99999999999999)
    xDirection1 = NXOpen.Vector3d(1.0, 0.0, 0.0)
    yDirection1 = NXOpen.Vector3d(0.0, 1.0, 0.0)
    xform3 = workPart.Xforms.CreateXform(origin73, xDirection1, yDirection1, NXOpen.SmartObject.UpdateOption.AfterModeling, 1.0)
    
    cartesianCoordinateSystem1 = workPart.CoordinateSystems.CreateCoordinateSystem(xform3, NXOpen.SmartObject.UpdateOption.AfterModeling)
    
    jointBuilder1.JointDefine.FirstCsys = cartesianCoordinateSystem1
    
    globalSelectionBuilder11 = theSession.MotionSession.MotionMethods.GetGlobalSelectionBuilder(workPart)
    
    selectTaggedObjectList10 = globalSelectionBuilder11.Selection
    
    workPart.Points.DeletePoint(point2)
    
    point5 = workPart.Points.CreatePoint(point3, xform2, NXOpen.SmartObject.UpdateOption.AfterModeling)
    
    markId17 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Start")
    
    expression158 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    expression159 = workPart.Expressions.CreateSystemExpressionWithUnits("p90_x=0.00000000000", unit1)
    
    expression160 = workPart.Expressions.CreateSystemExpressionWithUnits("p91_y=-122.00000000000", unit1)
    
    expression161 = workPart.Expressions.CreateSystemExpressionWithUnits("p92_z=122.00000000000", unit1)
    
    expression162 = workPart.Expressions.CreateSystemExpressionWithUnits("p93_xdelta=0", unit1)
    
    expression163 = workPart.Expressions.CreateSystemExpressionWithUnits("p94_ydelta=0", unit1)
    
    expression164 = workPart.Expressions.CreateSystemExpressionWithUnits("p95_zdelta=0", unit1)
    
    expression165 = workPart.Expressions.CreateSystemExpressionWithUnits("p96_radius=0", unit1)
    
    unit2 = jointBuilder1.JointMultiDrivers.MotionTranslationZ.PhaseAngleExpression.Units
    
    expression166 = workPart.Expressions.CreateSystemExpressionWithUnits("p97_angle=0", unit2)
    
    expression167 = workPart.Expressions.CreateSystemExpressionWithUnits("p98_zdelta=0", unit1)
    
    expression168 = workPart.Expressions.CreateSystemExpressionWithUnits("p99_radius=0", unit1)
    
    expression169 = workPart.Expressions.CreateSystemExpressionWithUnits("p100_angle1=0", unit2)
    
    expression170 = workPart.Expressions.CreateSystemExpressionWithUnits("p101_angle2=0", unit2)
    
    expression171 = workPart.Expressions.CreateSystemExpressionWithUnits("p102_distance=0", unit1)
    
    expression172 = workPart.Expressions.CreateSystemExpressionWithUnits("p103_arclen=0", unit1)
    
    expression173 = workPart.Expressions.CreateSystemExpressionWithUnits("p104_percent=0", NXOpen.Unit.Null)
    
    theSession.SetUndoMarkName(markId17, "Point Dialog")
    
    expression159.SetFormula("0")
    
    expression160.SetFormula("-122")
    
    expression161.SetFormula("122")
    
    expression159.SetFormula("0.00000000000")
    
    expression160.SetFormula("-122.00000000000")
    
    expression161.SetFormula("122.00000000000")
    
    # ----------------------------------------------
    #   Dialog Begin Point
    # ----------------------------------------------
    globalSelectionBuilder12 = theSession.MotionSession.MotionMethods.GetGlobalSelectionBuilder(workPart)
    
    selectTaggedObjectList11 = globalSelectionBuilder12.Selection
    
    expression161.SetFormula("61.00000000000")
    
    nErrs2 = theSession.UpdateManager.AddToDeleteList(point5)
    
    globalSelectionBuilder13 = theSession.MotionSession.MotionMethods.GetGlobalSelectionBuilder(workPart)
    
    selectTaggedObjectList12 = globalSelectionBuilder13.Selection
    
    globalSelectionBuilder14 = theSession.MotionSession.MotionMethods.GetGlobalSelectionBuilder(workPart)
    
    selectTaggedObjectList13 = globalSelectionBuilder14.Selection
    
    scalar1 = workPart.Scalars.CreateScalarExpression(expression159, NXOpen.Scalar.DimensionalityType.NotSet, NXOpen.SmartObject.UpdateOption.AfterModeling)
    
    scalar2 = workPart.Scalars.CreateScalarExpression(expression160, NXOpen.Scalar.DimensionalityType.NotSet, NXOpen.SmartObject.UpdateOption.AfterModeling)
    
    scalar3 = workPart.Scalars.CreateScalarExpression(expression161, NXOpen.Scalar.DimensionalityType.NotSet, NXOpen.SmartObject.UpdateOption.AfterModeling)
    
    point6 = workPart.Points.CreatePoint(scalar1, scalar2, scalar3, NXOpen.SmartObject.UpdateOption.AfterModeling)
    
    expression159.RightHandSide = "0.00000000000"
    
    expression160.RightHandSide = "-122.00000000000"
    
    expression161.RightHandSide = "61.00000000000"
    
    nErrs3 = theSession.UpdateManager.AddToDeleteList(point6)
    
    scalar4 = workPart.Scalars.CreateScalarExpression(expression159, NXOpen.Scalar.DimensionalityType.NotSet, NXOpen.SmartObject.UpdateOption.AfterModeling)
    
    scalar5 = workPart.Scalars.CreateScalarExpression(expression160, NXOpen.Scalar.DimensionalityType.NotSet, NXOpen.SmartObject.UpdateOption.AfterModeling)
    
    scalar6 = workPart.Scalars.CreateScalarExpression(expression161, NXOpen.Scalar.DimensionalityType.NotSet, NXOpen.SmartObject.UpdateOption.AfterModeling)
    
    point7 = workPart.Points.CreatePoint(scalar4, scalar5, scalar6, NXOpen.SmartObject.UpdateOption.AfterModeling)
    
    markId18 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Point")
    
    theSession.DeleteUndoMark(markId18, None)
    
    markId19 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Point")
    
    expression159.RightHandSide = "0.00000000000"
    
    expression160.RightHandSide = "-122.00000000000"
    
    expression161.RightHandSide = "61.00000000000"
    
    nErrs4 = theSession.UpdateManager.AddToDeleteList(point7)
    
    scalar7 = workPart.Scalars.CreateScalarExpression(expression159, NXOpen.Scalar.DimensionalityType.NotSet, NXOpen.SmartObject.UpdateOption.AfterModeling)
    
    scalar8 = workPart.Scalars.CreateScalarExpression(expression160, NXOpen.Scalar.DimensionalityType.NotSet, NXOpen.SmartObject.UpdateOption.AfterModeling)
    
    scalar9 = workPart.Scalars.CreateScalarExpression(expression161, NXOpen.Scalar.DimensionalityType.NotSet, NXOpen.SmartObject.UpdateOption.AfterModeling)
    
    point8 = workPart.Points.CreatePoint(scalar7, scalar8, scalar9, NXOpen.SmartObject.UpdateOption.AfterModeling)
    
    theSession.DeleteUndoMark(markId19, None)
    
    theSession.SetUndoMarkName(markId17, "Point")
    
    try:
        # Expression is still in use.
        workPart.Expressions.Delete(expression162)
    except NXOpen.NXException as ex:
        ex.AssertErrorCode(1050029)
        
    try:
        # Expression is still in use.
        workPart.Expressions.Delete(expression163)
    except NXOpen.NXException as ex:
        ex.AssertErrorCode(1050029)
        
    try:
        # Expression is still in use.
        workPart.Expressions.Delete(expression164)
    except NXOpen.NXException as ex:
        ex.AssertErrorCode(1050029)
        
    try:
        # Expression is still in use.
        workPart.Expressions.Delete(expression165)
    except NXOpen.NXException as ex:
        ex.AssertErrorCode(1050029)
        
    try:
        # Expression is still in use.
        workPart.Expressions.Delete(expression166)
    except NXOpen.NXException as ex:
        ex.AssertErrorCode(1050029)
        
    try:
        # Expression is still in use.
        workPart.Expressions.Delete(expression167)
    except NXOpen.NXException as ex:
        ex.AssertErrorCode(1050029)
        
    try:
        # Expression is still in use.
        workPart.Expressions.Delete(expression168)
    except NXOpen.NXException as ex:
        ex.AssertErrorCode(1050029)
        
    try:
        # Expression is still in use.
        workPart.Expressions.Delete(expression169)
    except NXOpen.NXException as ex:
        ex.AssertErrorCode(1050029)
        
    try:
        # Expression is still in use.
        workPart.Expressions.Delete(expression170)
    except NXOpen.NXException as ex:
        ex.AssertErrorCode(1050029)
        
    try:
        # Expression is still in use.
        workPart.Expressions.Delete(expression171)
    except NXOpen.NXException as ex:
        ex.AssertErrorCode(1050029)
        
    try:
        # Expression is still in use.
        workPart.Expressions.Delete(expression172)
    except NXOpen.NXException as ex:
        ex.AssertErrorCode(1050029)
        
    try:
        # Expression is still in use.
        workPart.Expressions.Delete(expression173)
    except NXOpen.NXException as ex:
        ex.AssertErrorCode(1050029)
        
    workPart.MeasureManager.SetPartTransientModification()
    
    workPart.Expressions.Delete(expression158)
    
    workPart.MeasureManager.ClearPartTransientModification()
    
    theSession.DeleteUndoMark(markId17, None)
    
    jointBuilder1.JointDefine.FirstOrigin = point8
    
    workPart.Points.DeletePoint(point4)
    
    scalar10 = workPart.Scalars.CreateScalarExpression(expression159, NXOpen.Scalar.DimensionalityType.NotSet, NXOpen.SmartObject.UpdateOption.AfterModeling)
    
    scalar11 = workPart.Scalars.CreateScalarExpression(expression160, NXOpen.Scalar.DimensionalityType.NotSet, NXOpen.SmartObject.UpdateOption.AfterModeling)
    
    scalar12 = workPart.Scalars.CreateScalarExpression(expression161, NXOpen.Scalar.DimensionalityType.NotSet, NXOpen.SmartObject.UpdateOption.AfterModeling)
    
    point9 = workPart.Points.CreatePoint(scalar10, scalar11, scalar12, NXOpen.SmartObject.UpdateOption.AfterModeling)
    
    globalSelectionBuilder15 = theSession.MotionSession.MotionMethods.GetGlobalSelectionBuilder(workPart)
    
    selectTaggedObjectList14 = globalSelectionBuilder15.Selection
    
    globalSelectionBuilder16 = theSession.MotionSession.MotionMethods.GetGlobalSelectionBuilder(workPart)
    
    selectTaggedObjectList15 = globalSelectionBuilder16.Selection
    
    origin74 = NXOpen.Point3d(0.0, 0.0, 0.0)
    vector73 = NXOpen.Vector3d(0.0, 0.0, 1.0)
    direction1 = workPart.Directions.CreateDirection(origin74, vector73, NXOpen.SmartObject.UpdateOption.AfterModeling)
    
    jointBuilder1.JointDefine.FirstVector = direction1
    
    markId20 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Joint")
    
    theSession.DeleteUndoMark(markId20, None)
    
    markId21 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Joint")
    
    nXObject158 = jointBuilder1.Commit()
    
    theSession.DeleteUndoMark(markId21, None)
    
    theSession.SetUndoMarkName(markId16, "Joint")
    
    jointBuilder1.Destroy()
    
    workPart.Points.DeletePoint(point9)
    
    workPart.MeasureManager.SetPartTransientModification()
    
    workPart.Expressions.Delete(expression157)
    
    workPart.MeasureManager.ClearPartTransientModification()
    
    workPart.MeasureManager.SetPartTransientModification()
    
    workPart.Expressions.Delete(expression151)
    
    workPart.MeasureManager.ClearPartTransientModification()
    
    workPart.MeasureManager.SetPartTransientModification()
    
    workPart.Expressions.Delete(expression152)
    
    workPart.MeasureManager.ClearPartTransientModification()
    
    workPart.MeasureManager.SetPartTransientModification()
    
    workPart.Expressions.Delete(expression153)
    
    workPart.MeasureManager.ClearPartTransientModification()
    
    workPart.MeasureManager.SetPartTransientModification()
    
    workPart.Expressions.Delete(expression154)
    
    workPart.MeasureManager.ClearPartTransientModification()
    
    workPart.MeasureManager.SetPartTransientModification()
    
    workPart.Expressions.Delete(expression155)
    
    workPart.MeasureManager.ClearPartTransientModification()
    
    workPart.MeasureManager.SetPartTransientModification()
    
    workPart.Expressions.Delete(expression156)
    
    workPart.MeasureManager.ClearPartTransientModification()
    
    # ----------------------------------------------
    #   Menu: Insert->Joint...
    # ----------------------------------------------
    markId22 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")
    
    jointBuilder2 = workPart.MotionManager.Joints.CreateJointBuilder(NXOpen.Motion.Joint.Null)
    
    jointBuilder2.JointDefine.UpperLimitExpression.SetFormula("0")
    
    jointBuilder2.JointDefine.LowerLimitExpression.SetFormula("0")
    
    jointBuilder2.JointDefine.UpperLimitAngleExpression.SetFormula("0")
    
    jointBuilder2.JointDefine.LowerLimitAngleExpression.SetFormula("0")
    
    jointBuilder2.JointDefine.ScrewRatioExpression.SetFormula("1")
    
    jointBuilder2.JointFriction.AdamsFriction.MuStaticExpression.SetFormula("0")
    
    jointBuilder2.JointFriction.AdamsFriction.MuDynamicExpression.SetFormula("0.1")
    
    jointBuilder2.JointFriction.AdamsFriction.StictionTransitionVelocityExpression.SetFormula("0.1")
    
    jointBuilder2.JointFriction.AdamsFriction.MaxStictionDeformationExpression.SetFormula("0.01")
    
    jointBuilder2.JointFriction.AdamsFriction.BallRadiusExpression.SetFormula("1")
    
    jointBuilder2.JointFriction.AdamsFriction.PinRadiusExpression.SetFormula("1")
    
    jointBuilder2.JointFriction.AdamsFriction.BendingArmExpression.SetFormula("1")
    
    jointBuilder2.JointFriction.AdamsFriction.FrictionArmExpression.SetFormula("1")
    
    jointBuilder2.JointFriction.AdamsFriction.ReactionArmExpression.SetFormula("1")
    
    jointBuilder2.JointFriction.AdamsFriction.InitialOverlapExpression.SetFormula("1000")
    
    jointBuilder2.JointFriction.AdamsFriction.ForcePreloadExpression.SetFormula("0")
    
    jointBuilder2.JointFriction.AdamsFriction.TorquePreloadExpression.SetFormula("0")
    
    jointBuilder2.JointFriction.RecurDynFriction.MuStaticExpression.SetFormula("0")
    
    jointBuilder2.JointFriction.RecurDynFriction.MuDynamicExpression.SetFormula("0.1")
    
    jointBuilder2.JointFriction.RecurDynFriction.StictionTransitionVelocityExpression.SetFormula("0.1")
    
    jointBuilder2.JointFriction.RecurDynFriction.MaxStictionDeformationExpression.SetFormula("0.01")
    
    jointBuilder2.JointFriction.RecurDynFriction.BallRadiusExpression.SetFormula("1")
    
    jointBuilder2.JointFriction.RecurDynFriction.PinRadiusExpression.SetFormula("1")
    
    jointBuilder2.JointFriction.RecurDynFriction.BendingArmExpression.SetFormula("1")
    
    jointBuilder2.JointFriction.RecurDynFriction.FrictionArmExpression.SetFormula("1")
    
    jointBuilder2.JointFriction.RecurDynFriction.ReactionArmExpression.SetFormula("10")
    
    jointBuilder2.JointFriction.RecurDynFriction.InitialOverlapExpression.SetFormula("1000")
    
    jointBuilder2.JointFriction.RecurDynFriction.ForcePreloadExpression.SetFormula("0")
    
    jointBuilder2.JointFriction.RecurDynFriction.TorquePreloadExpression.SetFormula("0")
    
    jointBuilder2.JointFriction.RecurDynFriction.MaxFrictionForceExpression.SetFormula("0")
    
    jointBuilder2.JointFriction.RecurDynFriction.MaxFrictionTorqueExpression.SetFormula("0")
    
    jointBuilder2.JointFriction.LmsFriction.MuStatic.SetFormula("0")
    
    jointBuilder2.JointFriction.LmsFriction.MuDynamic.SetFormula("0.1")
    
    jointBuilder2.JointFriction.LmsFriction.TranslationalStictionTransitionVelocity.SetFormula("0.1")
    
    jointBuilder2.JointFriction.LmsFriction.RotationalStictionTransitionVelocity.SetFormula("0.0572957795130824")
    
    jointBuilder2.JointFriction.LmsFriction.PinRadius.SetFormula("1")
    
    jointBuilder2.JointFriction.LmsFriction.BendingReactionArm.SetFormula("1")
    
    jointBuilder2.JointFriction.LmsFriction.FrictionArm.SetFormula("1")
    
    jointBuilder2.JointFriction.LmsFriction.ReactionArm.SetFormula("10")
    
    jointBuilder2.JointFriction.LmsFriction.InitialOverlap.SetFormula("1000")
    
    jointBuilder2.JointFriction.LmsFriction.BallRadius.SetFormula("1")
    
    jointBuilder2.JointMultiDrivers.MotionEulerAngle1.DisplacementExpression.SetFormula("0")
    
    jointBuilder2.JointMultiDrivers.MotionEulerAngle1.VelocityExpression.SetFormula("0")
    
    jointBuilder2.JointMultiDrivers.MotionEulerAngle1.AccelerationExpression.SetFormula("0")
    
    jointBuilder2.JointMultiDrivers.MotionEulerAngle1.JerkExpression.SetFormula("0")
    
    jointBuilder2.JointMultiDrivers.MotionEulerAngle1.AmplitudeExpression.SetFormula("0")
    
    jointBuilder2.JointMultiDrivers.MotionEulerAngle1.FrequencyExpression.SetFormula("0")
    
    jointBuilder2.JointMultiDrivers.MotionEulerAngle1.PhaseAngleExpression.SetFormula("0")
    
    jointBuilder2.JointMultiDrivers.MotionEulerAngle1.HarmonicDisplacementExpression.SetFormula("0")
    
    jointBuilder2.JointMultiDrivers.MotionEulerAngle1.InitialDisplacementExpression.SetFormula("0")
    
    jointBuilder2.JointMultiDrivers.MotionEulerAngle1.InitialVelocityExpression.SetFormula("0")
    
    jointBuilder2.JointMultiDrivers.MotionEulerAngle1.ControlInitialVelocityExpression.SetFormula("0")
    
    jointBuilder2.JointMultiDrivers.MotionEulerAngle1.ControlInitialAccelerationExpression.SetFormula("0")
    
    jointBuilder2.JointMultiDrivers.MotionTranslationZ.DisplacementExpression.SetFormula("0")
    
    jointBuilder2.JointMultiDrivers.MotionTranslationZ.VelocityExpression.SetFormula("0")
    
    jointBuilder2.JointMultiDrivers.MotionTranslationZ.AccelerationExpression.SetFormula("0")
    
    jointBuilder2.JointMultiDrivers.MotionTranslationZ.JerkExpression.SetFormula("0")
    
    jointBuilder2.JointMultiDrivers.MotionTranslationZ.AmplitudeExpression.SetFormula("0")
    
    jointBuilder2.JointMultiDrivers.MotionTranslationZ.FrequencyExpression.SetFormula("0")
    
    jointBuilder2.JointMultiDrivers.MotionTranslationZ.PhaseAngleExpression.SetFormula("0")
    
    jointBuilder2.JointMultiDrivers.MotionTranslationZ.HarmonicDisplacementExpression.SetFormula("0")
    
    jointBuilder2.JointMultiDrivers.MotionTranslationZ.InitialDisplacementExpression.SetFormula("0")
    
    jointBuilder2.JointMultiDrivers.MotionTranslationZ.InitialVelocityExpression.SetFormula("0")
    
    jointBuilder2.JointMultiDrivers.MotionTranslationZ.ControlInitialVelocityExpression.SetFormula("0")
    
    jointBuilder2.JointMultiDrivers.MotionTranslationZ.ControlInitialAccelerationExpression.SetFormula("0")
    
    jointBuilder2.JointMultiDrivers.MotionPointOnCurve.DisplacementExpression.SetFormula("0")
    
    jointBuilder2.JointMultiDrivers.MotionPointOnCurve.VelocityExpression.SetFormula("0")
    
    jointBuilder2.JointMultiDrivers.MotionPointOnCurve.AccelerationExpression.SetFormula("0")
    
    jointBuilder2.JointMultiDrivers.MotionPointOnCurve.JerkExpression.SetFormula("0")
    
    jointBuilder2.JointMultiDrivers.MotionPointOnCurve.AmplitudeExpression.SetFormula("0")
    
    jointBuilder2.JointMultiDrivers.MotionPointOnCurve.FrequencyExpression.SetFormula("0")
    
    jointBuilder2.JointMultiDrivers.MotionPointOnCurve.PhaseAngleExpression.SetFormula("0")
    
    jointBuilder2.JointMultiDrivers.MotionPointOnCurve.HarmonicDisplacementExpression.SetFormula("0")
    
    jointBuilder2.JointMultiDrivers.MotionPointOnCurve.InitialDisplacementExpression.SetFormula("0")
    
    jointBuilder2.JointMultiDrivers.MotionPointOnCurve.InitialVelocityExpression.SetFormula("0")
    
    jointBuilder2.JointMultiDrivers.MotionPointOnCurve.ControlInitialVelocityExpression.SetFormula("0")
    
    jointBuilder2.JointMultiDrivers.MotionPointOnCurve.ControlInitialAccelerationExpression.SetFormula("0")
    
    theSession.SetUndoMarkName(markId22, "Joint Dialog")
    
    expression174 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    expression175 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    expression176 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    expression177 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    expression178 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    expression179 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    jointBuilder2.JointDefine.ScrewSplineFunction = NXOpen.CAE.Function.Null
    
    jointBuilder2.JointDefine.ScrewDisplCurveFunction = NXOpen.CAE.Function.Null
    
    jointBuilder2.JointMultiDrivers.MotionEulerAngle1.Function = NXOpen.NXObject.Null
    
    jointBuilder2.JointMultiDrivers.MotionEulerAngle1.Function = NXOpen.NXObject.Null
    
    jointBuilder2.JointMultiDrivers.MotionTranslationZ.Function = NXOpen.NXObject.Null
    
    jointBuilder2.JointMultiDrivers.MotionTranslationZ.Function = NXOpen.NXObject.Null
    
    jointBuilder2.JointMultiDrivers.MotionPointOnCurve.Function = NXOpen.NXObject.Null
    
    jointBuilder2.JointMultiDrivers.MotionPointOnCurve.Function = NXOpen.NXObject.Null
    
    jointBuilder2.JointMultiDrivers.MotionEulerAngle1.Function = NXOpen.NXObject.Null
    
    jointBuilder2.JointMultiDrivers.MotionTranslationZ.Function = NXOpen.NXObject.Null
    
    jointBuilder2.JointMultiDrivers.MotionPointOnCurve.Function = NXOpen.NXObject.Null
    
    globalSelectionBuilder17 = theSession.MotionSession.MotionMethods.GetGlobalSelectionBuilder(workPart)
    
    selectTaggedObjectList16 = globalSelectionBuilder17.Selection
    
    globalSelectionBuilder18 = theSession.MotionSession.MotionMethods.GetGlobalSelectionBuilder(workPart)
    
    selectTaggedObjectList17 = globalSelectionBuilder18.Selection
    
    globalSelectionBuilder19 = theSession.MotionSession.MotionMethods.GetGlobalSelectionBuilder(workPart)
    
    selectTaggedObjectList18 = globalSelectionBuilder19.Selection
    
    link2 = nXObject155
    jointBuilder2.JointDefine.FirstLinkSelection.Value = link2
    
    globalSelectionBuilder20 = theSession.MotionSession.MotionMethods.GetGlobalSelectionBuilder(workPart)
    
    selectTaggedObjectList19 = globalSelectionBuilder20.Selection
    
    expression180 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    edge4 = cylinder1.FindObject("EDGE * 1 CYLINDER(66) 3 {(-1.0166666666667,-1.7609183210284,122)(2.0333333333333,0,122)(-1.0166666666667,1.7609183210284,122) CYLINDER(1)}")
    point10 = workPart.Points.CreatePoint(edge4, NXOpen.SmartObject.UpdateOption.AfterModeling)
    
    edge5 = component1.FindObject("PROTO#.Features|CYLINDER(1)|EDGE * 1 CYLINDER(66) 3 {(-1.0166666666667,-1.7609183210284,122)(2.0333333333333,0,122)(-1.0166666666667,1.7609183210284,122) CYLINDER(1)}")
    xform4, nXObject159 = workPart.Xforms.CreateExtractXform(edge5, NXOpen.SmartObject.UpdateOption.AfterModeling, False)
    
    point11 = workPart.Points.CreatePoint(point10, xform4, NXOpen.SmartObject.UpdateOption.AfterModeling)
    
    globalSelectionBuilder21 = theSession.MotionSession.MotionMethods.GetGlobalSelectionBuilder(workPart)
    
    selectTaggedObjectList20 = globalSelectionBuilder21.Selection
    
    partLoadStatus2 = part152.LoadFeatureDataForSelection()
    
    partLoadStatus2.Dispose()
    edge6 = nXObject159
    point12 = workPart.Points.CreatePoint(edge6, NXOpen.SmartObject.UpdateOption.AfterModeling)
    
    xform5, nXObject160 = workPart.Xforms.CreateExtractXform(edge5, NXOpen.SmartObject.UpdateOption.AfterModeling, False)
    
    point13 = workPart.Points.CreatePoint(point12, xform5, NXOpen.SmartObject.UpdateOption.AfterModeling)
    
    jointBuilder2.JointDefine.FirstOrigin = point13
    
    origin75 = NXOpen.Point3d(0.0, 0.0, 121.99999999999999)
    xDirection2 = NXOpen.Vector3d(1.0, 0.0, 0.0)
    yDirection2 = NXOpen.Vector3d(0.0, 1.0, 0.0)
    xform6 = workPart.Xforms.CreateXform(origin75, xDirection2, yDirection2, NXOpen.SmartObject.UpdateOption.AfterModeling, 1.0)
    
    cartesianCoordinateSystem2 = workPart.CoordinateSystems.CreateCoordinateSystem(xform6, NXOpen.SmartObject.UpdateOption.AfterModeling)
    
    jointBuilder2.JointDefine.FirstCsys = cartesianCoordinateSystem2
    
    globalSelectionBuilder22 = theSession.MotionSession.MotionMethods.GetGlobalSelectionBuilder(workPart)
    
    selectTaggedObjectList21 = globalSelectionBuilder22.Selection
    
    workPart.Points.DeletePoint(point11)
    
    point14 = workPart.Points.CreatePoint(point12, xform5, NXOpen.SmartObject.UpdateOption.AfterModeling)
    
    markId23 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Start")
    
    expression181 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    expression182 = workPart.Expressions.CreateSystemExpressionWithUnits("p91_x=0.00000000000", unit1)
    
    expression183 = workPart.Expressions.CreateSystemExpressionWithUnits("p92_y=0.00000000000", unit1)
    
    expression184 = workPart.Expressions.CreateSystemExpressionWithUnits("p93_z=122.00000000000", unit1)
    
    expression185 = workPart.Expressions.CreateSystemExpressionWithUnits("p94_xdelta=0", unit1)
    
    expression186 = workPart.Expressions.CreateSystemExpressionWithUnits("p95_ydelta=0", unit1)
    
    expression187 = workPart.Expressions.CreateSystemExpressionWithUnits("p96_zdelta=0", unit1)
    
    expression188 = workPart.Expressions.CreateSystemExpressionWithUnits("p97_radius=0", unit1)
    
    expression189 = workPart.Expressions.CreateSystemExpressionWithUnits("p98_angle=0", unit2)
    
    expression190 = workPart.Expressions.CreateSystemExpressionWithUnits("p99_zdelta=0", unit1)
    
    expression191 = workPart.Expressions.CreateSystemExpressionWithUnits("p100_radius=0", unit1)
    
    expression192 = workPart.Expressions.CreateSystemExpressionWithUnits("p101_angle1=0", unit2)
    
    expression193 = workPart.Expressions.CreateSystemExpressionWithUnits("p102_angle2=0", unit2)
    
    expression194 = workPart.Expressions.CreateSystemExpressionWithUnits("p103_distance=0", unit1)
    
    expression195 = workPart.Expressions.CreateSystemExpressionWithUnits("p104_arclen=0", unit1)
    
    expression196 = workPart.Expressions.CreateSystemExpressionWithUnits("p105_percent=0", NXOpen.Unit.Null)
    
    theSession.SetUndoMarkName(markId23, "Point Dialog")
    
    expression182.SetFormula("0")
    
    expression183.SetFormula("0")
    
    expression184.SetFormula("122")
    
    expression182.SetFormula("0.00000000000")
    
    expression183.SetFormula("0.00000000000")
    
    expression184.SetFormula("122.00000000000")
    
    # ----------------------------------------------
    #   Dialog Begin Point
    # ----------------------------------------------
    globalSelectionBuilder23 = theSession.MotionSession.MotionMethods.GetGlobalSelectionBuilder(workPart)
    
    selectTaggedObjectList22 = globalSelectionBuilder23.Selection
    
    expression184.SetFormula("61.00000000000")
    
    nErrs5 = theSession.UpdateManager.AddToDeleteList(point14)
    
    globalSelectionBuilder24 = theSession.MotionSession.MotionMethods.GetGlobalSelectionBuilder(workPart)
    
    selectTaggedObjectList23 = globalSelectionBuilder24.Selection
    
    globalSelectionBuilder25 = theSession.MotionSession.MotionMethods.GetGlobalSelectionBuilder(workPart)
    
    selectTaggedObjectList24 = globalSelectionBuilder25.Selection
    
    scalar13 = workPart.Scalars.CreateScalarExpression(expression182, NXOpen.Scalar.DimensionalityType.NotSet, NXOpen.SmartObject.UpdateOption.AfterModeling)
    
    scalar14 = workPart.Scalars.CreateScalarExpression(expression183, NXOpen.Scalar.DimensionalityType.NotSet, NXOpen.SmartObject.UpdateOption.AfterModeling)
    
    scalar15 = workPart.Scalars.CreateScalarExpression(expression184, NXOpen.Scalar.DimensionalityType.NotSet, NXOpen.SmartObject.UpdateOption.AfterModeling)
    
    point15 = workPart.Points.CreatePoint(scalar13, scalar14, scalar15, NXOpen.SmartObject.UpdateOption.AfterModeling)
    
    expression182.RightHandSide = "0.00000000000"
    
    expression183.RightHandSide = "0.00000000000"
    
    expression184.RightHandSide = "61.00000000000"
    
    nErrs6 = theSession.UpdateManager.AddToDeleteList(point15)
    
    scalar16 = workPart.Scalars.CreateScalarExpression(expression182, NXOpen.Scalar.DimensionalityType.NotSet, NXOpen.SmartObject.UpdateOption.AfterModeling)
    
    scalar17 = workPart.Scalars.CreateScalarExpression(expression183, NXOpen.Scalar.DimensionalityType.NotSet, NXOpen.SmartObject.UpdateOption.AfterModeling)
    
    scalar18 = workPart.Scalars.CreateScalarExpression(expression184, NXOpen.Scalar.DimensionalityType.NotSet, NXOpen.SmartObject.UpdateOption.AfterModeling)
    
    point16 = workPart.Points.CreatePoint(scalar16, scalar17, scalar18, NXOpen.SmartObject.UpdateOption.AfterModeling)
    
    expression184.SetFormula("61.00000000000")
    
    expression182.RightHandSide = "0.00000000000"
    
    expression183.RightHandSide = "0.00000000000"
    
    expression184.RightHandSide = "61.00000000000"
    
    nErrs7 = theSession.UpdateManager.AddToDeleteList(point16)
    
    scalar19 = workPart.Scalars.CreateScalarExpression(expression182, NXOpen.Scalar.DimensionalityType.NotSet, NXOpen.SmartObject.UpdateOption.AfterModeling)
    
    scalar20 = workPart.Scalars.CreateScalarExpression(expression183, NXOpen.Scalar.DimensionalityType.NotSet, NXOpen.SmartObject.UpdateOption.AfterModeling)
    
    scalar21 = workPart.Scalars.CreateScalarExpression(expression184, NXOpen.Scalar.DimensionalityType.NotSet, NXOpen.SmartObject.UpdateOption.AfterModeling)
    
    point17 = workPart.Points.CreatePoint(scalar19, scalar20, scalar21, NXOpen.SmartObject.UpdateOption.AfterModeling)
    
    markId24 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Point")
    
    theSession.DeleteUndoMark(markId24, None)
    
    markId25 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Point")
    
    expression182.RightHandSide = "0.00000000000"
    
    expression183.RightHandSide = "0.00000000000"
    
    expression184.RightHandSide = "61.00000000000"
    
    nErrs8 = theSession.UpdateManager.AddToDeleteList(point17)
    
    scalar22 = workPart.Scalars.CreateScalarExpression(expression182, NXOpen.Scalar.DimensionalityType.NotSet, NXOpen.SmartObject.UpdateOption.AfterModeling)
    
    scalar23 = workPart.Scalars.CreateScalarExpression(expression183, NXOpen.Scalar.DimensionalityType.NotSet, NXOpen.SmartObject.UpdateOption.AfterModeling)
    
    scalar24 = workPart.Scalars.CreateScalarExpression(expression184, NXOpen.Scalar.DimensionalityType.NotSet, NXOpen.SmartObject.UpdateOption.AfterModeling)
    
    point18 = workPart.Points.CreatePoint(scalar22, scalar23, scalar24, NXOpen.SmartObject.UpdateOption.AfterModeling)
    
    theSession.DeleteUndoMark(markId25, None)
    
    theSession.SetUndoMarkName(markId23, "Point")
    
    try:
        # Expression is still in use.
        workPart.Expressions.Delete(expression185)
    except NXOpen.NXException as ex:
        ex.AssertErrorCode(1050029)
        
    try:
        # Expression is still in use.
        workPart.Expressions.Delete(expression186)
    except NXOpen.NXException as ex:
        ex.AssertErrorCode(1050029)
        
    try:
        # Expression is still in use.
        workPart.Expressions.Delete(expression187)
    except NXOpen.NXException as ex:
        ex.AssertErrorCode(1050029)
        
    try:
        # Expression is still in use.
        workPart.Expressions.Delete(expression188)
    except NXOpen.NXException as ex:
        ex.AssertErrorCode(1050029)
        
    try:
        # Expression is still in use.
        workPart.Expressions.Delete(expression189)
    except NXOpen.NXException as ex:
        ex.AssertErrorCode(1050029)
        
    try:
        # Expression is still in use.
        workPart.Expressions.Delete(expression190)
    except NXOpen.NXException as ex:
        ex.AssertErrorCode(1050029)
        
    try:
        # Expression is still in use.
        workPart.Expressions.Delete(expression191)
    except NXOpen.NXException as ex:
        ex.AssertErrorCode(1050029)
        
    try:
        # Expression is still in use.
        workPart.Expressions.Delete(expression192)
    except NXOpen.NXException as ex:
        ex.AssertErrorCode(1050029)
        
    try:
        # Expression is still in use.
        workPart.Expressions.Delete(expression193)
    except NXOpen.NXException as ex:
        ex.AssertErrorCode(1050029)
        
    try:
        # Expression is still in use.
        workPart.Expressions.Delete(expression194)
    except NXOpen.NXException as ex:
        ex.AssertErrorCode(1050029)
        
    try:
        # Expression is still in use.
        workPart.Expressions.Delete(expression195)
    except NXOpen.NXException as ex:
        ex.AssertErrorCode(1050029)
        
    try:
        # Expression is still in use.
        workPart.Expressions.Delete(expression196)
    except NXOpen.NXException as ex:
        ex.AssertErrorCode(1050029)
        
    workPart.MeasureManager.SetPartTransientModification()
    
    workPart.Expressions.Delete(expression181)
    
    workPart.MeasureManager.ClearPartTransientModification()
    
    theSession.DeleteUndoMark(markId23, None)
    
    jointBuilder2.JointDefine.FirstOrigin = point18
    
    workPart.Points.DeletePoint(point13)
    
    scalar25 = workPart.Scalars.CreateScalarExpression(expression182, NXOpen.Scalar.DimensionalityType.NotSet, NXOpen.SmartObject.UpdateOption.AfterModeling)
    
    scalar26 = workPart.Scalars.CreateScalarExpression(expression183, NXOpen.Scalar.DimensionalityType.NotSet, NXOpen.SmartObject.UpdateOption.AfterModeling)
    
    scalar27 = workPart.Scalars.CreateScalarExpression(expression184, NXOpen.Scalar.DimensionalityType.NotSet, NXOpen.SmartObject.UpdateOption.AfterModeling)
    
    point19 = workPart.Points.CreatePoint(scalar25, scalar26, scalar27, NXOpen.SmartObject.UpdateOption.AfterModeling)
    
    globalSelectionBuilder26 = theSession.MotionSession.MotionMethods.GetGlobalSelectionBuilder(workPart)
    
    selectTaggedObjectList25 = globalSelectionBuilder26.Selection
    
    globalSelectionBuilder27 = theSession.MotionSession.MotionMethods.GetGlobalSelectionBuilder(workPart)
    
    selectTaggedObjectList26 = globalSelectionBuilder27.Selection
    
    origin76 = NXOpen.Point3d(0.0, 0.0, 0.0)
    vector74 = NXOpen.Vector3d(0.0, 0.0, 1.0)
    direction2 = workPart.Directions.CreateDirection(origin76, vector74, NXOpen.SmartObject.UpdateOption.AfterModeling)
    
    jointBuilder2.JointDefine.FirstVector = direction2
    
    markId26 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Joint")
    
    theSession.DeleteUndoMark(markId26, None)
    
    markId27 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Joint")
    
    nXObject161 = jointBuilder2.Commit()
    
    theSession.DeleteUndoMark(markId27, None)
    
    theSession.SetUndoMarkName(markId22, "Joint")
    
    jointBuilder2.Destroy()
    
    workPart.Points.DeletePoint(point19)
    
    workPart.MeasureManager.SetPartTransientModification()
    
    workPart.Expressions.Delete(expression180)
    
    workPart.MeasureManager.ClearPartTransientModification()
    
    workPart.MeasureManager.SetPartTransientModification()
    
    workPart.Expressions.Delete(expression174)
    
    workPart.MeasureManager.ClearPartTransientModification()
    
    workPart.MeasureManager.SetPartTransientModification()
    
    workPart.Expressions.Delete(expression175)
    
    workPart.MeasureManager.ClearPartTransientModification()
    
    workPart.MeasureManager.SetPartTransientModification()
    
    workPart.Expressions.Delete(expression176)
    
    workPart.MeasureManager.ClearPartTransientModification()
    
    workPart.MeasureManager.SetPartTransientModification()
    
    workPart.Expressions.Delete(expression177)
    
    workPart.MeasureManager.ClearPartTransientModification()
    
    workPart.MeasureManager.SetPartTransientModification()
    
    workPart.Expressions.Delete(expression178)
    
    workPart.MeasureManager.ClearPartTransientModification()
    
    workPart.MeasureManager.SetPartTransientModification()
    
    workPart.Expressions.Delete(expression179)
    
    workPart.MeasureManager.ClearPartTransientModification()
    
    # ----------------------------------------------
    #   Menu: Insert->Coupler->Gear Coupler...
    # ----------------------------------------------
    markId28 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")
    
    couplerGearBuilder1 = workPart.MotionManager.Couplers.CreateCouplerGearBuilder(NXOpen.Motion.CouplerGear.Null)
    
    couplerGearBuilder1.RatioExpression.SetFormula("1")
    
    couplerGearBuilder1.FirstRadiusExpression.SetFormula("61")
    
    couplerGearBuilder1.SecondRadiusExpression.SetFormula("61")
    
    couplerGearBuilder1.DisplayScale = 1.0
    
    theSession.SetUndoMarkName(markId28, "Gear Coupler Dialog")
    
    globalSelectionBuilder28 = theSession.MotionSession.MotionMethods.GetGlobalSelectionBuilder(workPart)
    
    selectTaggedObjectList27 = globalSelectionBuilder28.Selection
    
    joint1 = nXObject158
    couplerGearBuilder1.FirstJoint.Value = joint1
    
    globalSelectionBuilder29 = theSession.MotionSession.MotionMethods.GetGlobalSelectionBuilder(workPart)
    
    selectTaggedObjectList28 = globalSelectionBuilder29.Selection
    
    globalSelectionBuilder30 = theSession.MotionSession.MotionMethods.GetGlobalSelectionBuilder(workPart)
    
    selectTaggedObjectList29 = globalSelectionBuilder30.Selection
    
    joint2 = nXObject161
    couplerGearBuilder1.SecondJoint.Value = joint2
    
    coordinates1 = NXOpen.Point3d(0.0, -122.0, 61.0)
    point20 = workPart.Points.CreatePoint(coordinates1)
    
    markId29 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Gear Coupler")
    
    globalSelectionBuilder31 = theSession.MotionSession.MotionMethods.GetGlobalSelectionBuilder(workPart)
    
    selectTaggedObjectList30 = globalSelectionBuilder31.Selection
    
    theSession.DeleteUndoMark(markId29, None)
    
    markId30 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Gear Coupler")
    
    coordinates2 = NXOpen.Point3d(0.0, -122.0, 61.0)
    point21 = workPart.Points.CreatePoint(coordinates2)
    
    nXObject162 = couplerGearBuilder1.Commit()
    
    theSession.DeleteUndoMark(markId30, None)
    
    theSession.SetUndoMarkName(markId28, "Gear Coupler")
    
    couplerGearBuilder1.Destroy()
    
    # ----------------------------------------------
    #   Menu: Insert->Driver->Driver...
    # ----------------------------------------------
    markId31 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")
    
    jointDriverBuilder1 = workPart.MotionManager.JointDrivers.CreateJointDriverBuilder(NXOpen.Motion.JointDriver.Null)
    
    theSession.SetUndoMarkName(markId31, "Driver Dialog")
    
    jointDriverBuilder1.DriverMultiOperations.MotionEulerAngle1.Function = NXOpen.NXObject.Null
    
    jointDriverBuilder1.DriverMultiOperations.MotionEulerAngle1.Function = NXOpen.NXObject.Null
    
    jointDriverBuilder1.DriverMultiOperations.MotionTranslationZ.Function = NXOpen.NXObject.Null
    
    jointDriverBuilder1.DriverMultiOperations.MotionTranslationZ.Function = NXOpen.NXObject.Null
    
    jointDriverBuilder1.DriverMultiOperations.MotionPointOnCurve.Function = NXOpen.NXObject.Null
    
    jointDriverBuilder1.DriverMultiOperations.MotionPointOnCurve.Function = NXOpen.NXObject.Null
    
    globalSelectionBuilder32 = theSession.MotionSession.MotionMethods.GetGlobalSelectionBuilder(workPart)
    
    selectTaggedObjectList31 = globalSelectionBuilder32.Selection
    
    jointDriverBuilder1.Joint.Value = joint1
    
    jointDriverBuilder1.DriverMultiOperations.MotionEulerAngle1.TypeOption = NXOpen.Motion.DriverOperation.Type.Polynomial
    
    jointDriverBuilder1.DriverMultiOperations.MotionEulerAngle1.Function = NXOpen.NXObject.Null
    
    jointDriverBuilder1.DriverMultiOperations.MotionEulerAngle1.VelocityExpression.SetFormula("1")
    
    markId32 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Driver")
    
    globalSelectionBuilder33 = theSession.MotionSession.MotionMethods.GetGlobalSelectionBuilder(workPart)
    
    selectTaggedObjectList32 = globalSelectionBuilder33.Selection
    
    theSession.DeleteUndoMark(markId32, None)
    
    markId33 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Driver")
    
    nXObject163 = jointDriverBuilder1.Commit()
    
    theSession.DeleteUndoMark(markId33, None)
    
    theSession.SetUndoMarkName(markId31, "Driver")
    
    jointDriverBuilder1.Destroy()
    
    # ----------------------------------------------
    #   Menu: Insert->Solution->Solution...
    # ----------------------------------------------
    markId34 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")
    
    motionSolutionBuilder1 = workPart.MotionManager.MotionSolutions.CreateSolutionBuilder(NXOpen.Motion.MotionSolution.Null)
    
    theSession.SetUndoMarkName(markId34, "Solution Dialog")
    
    expression197 = workPart.Expressions.CreateSystemExpressionWithUnits("0", unit1)
    
    markId35 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Solution")
    
    theSession.DeleteUndoMark(markId35, None)
    
    markId36 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Solution")
    
    unit3 = workPart.UnitCollection.FindObject("Second")
    motionSolutionBuilder1.SetScalarExpressionPropertyValue("SolutionEndTime", "10", unit3)
    
    nXObject164 = motionSolutionBuilder1.Commit()
    
    theSession.DeleteUndoMark(markId36, None)
    
    theSession.SetUndoMarkName(markId34, "Solution")
    
    motionSolutionBuilder1.Destroy()
    
    workPart.MeasureManager.SetPartTransientModification()
    
    workPart.Expressions.Delete(expression197)
    
    workPart.MeasureManager.ClearPartTransientModification()
    
    theSession.MotionSession.MotionMethods.ModelCheck(False)
    
    globalSelectionBuilder34 = theSession.MotionSession.MotionMethods.GetGlobalSelectionBuilder(workPart)
    
    selectTaggedObjectList33 = globalSelectionBuilder34.Selection
    
    markId37 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, None)
    
    motionSolution1 = nXObject164
    motionSolution1.SolveNormalRunSolution()
    
    theSession.DeleteUndoMark(markId37, None)
    
    # ----------------------------------------------
    #   Menu: Analysis->Motion->Animation Player...
    # ----------------------------------------------
    markId38 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Animation Player")
    
    animationControl1 = motionSolution1.GetAnimationControl()
    
    markId39 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Start")
    
    theSession.SetUndoMarkName(markId39, "Animation Player Dialog")
    
    theSession.SetUndoMarkVisibility(markId39, None, NXOpen.Session.MarkVisibility.Invisible)
    
    theSession.MotionSession.PostProcess.SetInterferenceOption(False)
    
    theSession.MotionSession.PostProcess.SetMeasureOption(False)
    
    theSession.MotionSession.PostProcess.SetTraceOption(False)
    
    theSession.MotionSession.PostProcess.SetStopOnEventOption(False)
    
    theSession.MotionSession.PostProcess.SetInterferenceOption(False)
    
    theSession.MotionSession.PostProcess.SetMeasureOption(False)
    
    theSession.MotionSession.PostProcess.SetTraceOption(False)
    
    theSession.MotionSession.PostProcess.SetStopOnEventOption(False)
    
    animationControl1.Delay = 0
    
    animationControl1.Mode = NXOpen.Motion.PlayMode.PlayOnce
    
    animationControl1.StepToAssemblyPosition()
    
    animationControl1.Play()
    
    matrix1 = NXOpen.Matrix3x3()
    
    matrix1.Xx = 0.0
    matrix1.Xy = 1.0
    matrix1.Xz = 0.0
    matrix1.Yx = -1.0
    matrix1.Yy = 0.0
    matrix1.Yz = 0.0
    matrix1.Zx = 0.0
    matrix1.Zy = -0.0
    matrix1.Zz = 1.0
    workPart.ModelingViews.WorkView.Orient(matrix1)
    
    animationControl1.StepToAssemblyPosition()
    
    theSession.SetUndoMarkName(markId39, "Animation Player")
    
    theSession.DeleteUndoMark(markId39, None)
    
    animationControl1.Finish()
    
    # ----------------------------------------------
    #   Menu: Tools->Journal->Stop Recording
    # ----------------------------------------------
    
if __name__ == '__main__':
    main()