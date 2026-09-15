import numpy as np

def create_filled_array(shape, kind):
    """
    Returns: 2D numpy array of given shape with dtype float64
    """
    return np.where(kind=='zeros', np.zeros(shape), np.ones(shape))
    pass