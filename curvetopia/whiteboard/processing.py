# whiteboard/processing.py
import numpy as np
from scipy.interpolate import CubicSpline

def process_polylines(polylines):
    beautified_curves = []
    for polyline in polylines:
        points = np.array(polyline)
        t = np.linspace(0, 1, len(points))
        cs = CubicSpline(t, points, bc_type='natural')
        beautified_curves.append(cs(t))
    return beautified_curves
