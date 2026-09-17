import numpy as np

def normalize(data):
    """Returns: np.ndarray of shape (m, n), z-score normalized per column"""
    data = np.array(data, dtype=np.float64)
    mean = np.mean(data, axis=0)
    std = np.std(data, axis=0)
    return (data-mean) / std