import numpy as np

def sort_with_indices(data, axis):
    """Returns: np.ndarray of shape (2, m, n), stacked sorted values and sort indices"""
    data = np.array(data, dtype=np.float64)
    row_0 = np.sort(data,axis = axis)
    row_1 = np.argsort(data, axis = axis)
    return np.stack((row_0, row_1), dtype=np.float64, axis=0)