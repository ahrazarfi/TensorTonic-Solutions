import numpy as np

def row_extremes(data):
    """Returns: np.ndarray of shape (4, m), rows are max_val, max_col, min_val, min_col"""
    data = np.array(data, dtype=np.float64)
    # max_indices= np.argmax(data, axis=1)
    # min_indices = np.argmin(data, axis=1)
    # return np.stack([np.take_along_axis(data, max_indices[:, None], axis=1).squeeze(), max_indices, np.take_along_axis(data, min_indices[:, None], axis=1).squeeze(), min_indices])

    # other version using fancy indexing
    max_indices = np.argmax(data, axis=1)
    min_indices = np.argmin(data, axis=1)
    return np.stack([data[np.arange(data.shape[0]), max_indices], max_indices,
                   data[np.arange(data.shape[0]), min_indices], min_indices
                    ])

    