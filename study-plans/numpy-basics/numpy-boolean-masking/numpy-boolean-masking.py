import numpy as np

def row_summary(data, threshold):
    """Returns: np.ndarray of shape (3, m, n), stacked element mask, any-filtered, all-filtered"""
    data = np.array(data, dtype=np.float64)
    mask1 = data > threshold
    mask2 = np.any(data > threshold, axis=1, keepdims=True)
    mask3 = np.all(data > threshold, axis=1, keepdims=True)
    any_filtered = np.where(mask2, data, 0)
    all_filtered = np.where(mask3, data, 0)
    return np.stack([mask1, any_filtered, all_filtered])