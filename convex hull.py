import rhinoscriptsyntax as rs
import math
import random
from Rhino.Geometry import Point3d, Vector3d, Line

def get_orientation(p, q, r):
    """determines the orientation of the point triplet (p, q, r)"""
    v1 = Vector3d(q - p)
    v2 = Vector3d(r - q)
    cp = Vector3d.CrossProduct(v1, v2)
    return cp.Z > 0

def get_hull(points):
    """computes the convex hull of the input set of points"""
    points = sorted(set(points))
    if len(points) <= 1:
        return points
    # compute lower hull
    lower = []
    for p in points:
        while len(lower) >= 2 and not get_orientation(lower[-2], lower[-1], p):
            lower.pop()
        lower.append(p)
    # compute upper hull
    upper = []
    for p in reversed(points):
        while len(upper) >= 2 and not get_orientation(upper[-2], upper[-1], p):
            upper.pop()
        upper.append(p)
    return lower[:-1] + upper[:-1]

def get_convex_hull(points):
    """computes the convex hull of the input set of points and draws it in Rhino"""
    # compute the convex hull
    hull_points = get_hull(points)
    
    # create a polyline object
    polyline = rs.AddPolyline(hull_points + [hull_points[0]])
    
    # return the polyline object
    return polyline

def randompoints(x, y):
    num_points = int(y)

    # Create an empty list to store the points
    points = []

    # Generate random points and add them to the list
    for i in range(num_points):
        x = random.uniform(-x, x)
        y = random.uniform(-x, x)
        z = random.uniform(-x, x)
        points.append(Point3d(x, y, z))
    return points

# generate random points
points = randompoints(x, y)

a = points

# compute the convex hull and draw it in Rhino
polyline = get_convex_hull(points)

b = polyline 