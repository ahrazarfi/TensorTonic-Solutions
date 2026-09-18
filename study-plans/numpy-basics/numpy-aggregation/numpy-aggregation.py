import numpy as np

def summarize(data, axis):
    """Returns: np.ndarray of shape (4, k), rows are mean, std, min, max"""    
    data = np.array(data,dtype=np.float64)
    row_0 = np.mean(data, axis=axis)
    row_1 = np.std(data, axis=axis)
    row_2 = np.min(data, axis=axis)
    row_3 = np.max(data, axis=axis)
    return np.array([row_0, row_1, row_2, row_3])