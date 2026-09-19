import numpy as np

def quantize_and_frame(data, decimals, pad_width):
    """Returns: np.ndarray of shape (3, m+2p, n+2p), stacked rounded, floored, ceiled with zero-padding"""
    data = np.array(data, dtype=np.float64)
    a1 = np.pad(np.round(data, decimals), pad_width, mode='constant', constant_values=0)
    a2 = np.pad(np.floor(data), pad_width, mode='constant', constant_values=0)
    a3 = np.pad(np.ceil(data), pad_width, mode='constant', constant_values=0)
    return np.stack([a1,a2,a3])