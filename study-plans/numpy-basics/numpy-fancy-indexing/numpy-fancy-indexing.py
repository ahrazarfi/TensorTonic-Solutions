import numpy as np

def select_by_index(arr, indices, axis):
    """
    Returns: 2D ndarray of float64
    """
    data = np.array(arr, dtype=np.float64)
    return data[indices, :] if axis== 0 else data[:, indices]