import numpy as np

def compare_correlations(a, b):
    """Returns: np.ndarray of shape (3, n, n), stacked correlation matrices"""
    a = np.array(a, dtype=np.float64)
    b = np.array(b, dtype=np.float64)
    combined = np.concatenate([a,b], axis=0)
    row_0 = np.corrcoef(a, rowvar=False)
    row_1 = np.corrcoef(b, rowvar=False)
    row_2 = np.corrcoef(combined, rowvar=False)
    return np.stack([row_0,row_1, row_2])