import math
import maya.api.OpenMaya as om

def selectEdgesByAngle(angle):
    radians = math.radians(angle)
    curSelList = om.MGlobal.getActiveSelectionList()
    selIte = om.MItSelectionList(curSelList)
    newSelList = om.MSelectionList()
    while not selIte.isDone():
        edge_comp = om.MFnSingleIndexedComponent()
        edge_comp.create(om.MFn.kMeshEdgeComponent)
        edgeIte = om.MItMeshEdge(selIte.getDagPath())
        mesh = om.MFnMesh(selIte.getDagPath())
        while not edgeIte.isDone():
            faces = edgeIte.getConnectedFaces()
            # Avoid none-manifold topology and border edges
            if len(faces) != 2:
                continue
            v1 = mesh.getPolygonNormal(faces[0])
            v2 = mesh.getPolygonNormal(faces[1])
            deg = v1.angle(v2)
            if deg <= radians:
                edge_comp.addElement(edgeIte.index())
            edgeIte.next()
        selIte.next()
        newSelList.add((mesh.getPath(), edge_comp.object()), mergeWithExisting=True)
    om.MGlobal.setActiveSelectionList(newSelList)