import numpy as np

def norm_diff(a, b, lo, hi):
    """Returns: np.ndarray of absolute differences after clipping and rescaling to [0, 1]"""
    a = np.array(a, dtype=np.float64)
    b = np.array(b, dtype=np.float64)
    clip_a = np.clip(a, lo, hi)
    clip_b = np.clip(b, lo, hi)
    if lo == hi:
        return np.zeros_like(a, dtype=np.float64)
    rescale_a = (clip_a - lo) / (hi-lo)
    rescale_b = (clip_b - lo) / (hi-lo)
    return abs(rescale_a -rescale_b)