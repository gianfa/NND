
from typing import Tuple
import numpy as np


def compute_parlpd(
    dims:Tuple[float, float, float],
    pos:Tuple[float,float,float],
    axes:np.ndarray
):
    """Compute a parallelepiped with dimensions `dims` and position `pos`.
    
    """
    X, Y, Z = axes
    return \
    ( pos[0] <axes[0] ) & ( axes[0] <= pos[0]+dims[0]) & \
    ( pos[1] <axes[1] ) & ( axes[1] <= pos[1]+dims[1]) & \
    ( pos[2] <axes[2] ) & ( axes[2] <= pos[2]+dims[2])


def draw_Dense(n:int, pos:Tuple[float,float,float], axes:np.ndarray):
    dims = (1,1,n) # dx, dy, dz
    return compute_parlpd(dims, pos, axes)

def draw_Dense2D(n:int, m:int, pos:Tuple[float,float,float], axes:np.ndarray):
    dims = (1,m,n) # dx, dy, dz
    return compute_parlpd(dims, pos, axes)


