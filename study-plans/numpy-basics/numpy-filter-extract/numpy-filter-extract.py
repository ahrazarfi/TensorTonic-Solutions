import numpy as np

def filter_and_extract(data, row_start, row_stop, threshold):
    """
    Returns: 1D ndarray of float64
    """
    data = np.array(data, dtype=np.float64)
    block = data[row_start:row_stop,:]
    return block[block > threshold]