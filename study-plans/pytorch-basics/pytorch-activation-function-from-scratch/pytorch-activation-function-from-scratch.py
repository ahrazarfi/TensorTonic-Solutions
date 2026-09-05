import torch
import math

def activate(x, method="relu"):
    """
    Returns: list (activated tensor converted via .tolist())
    """
    x = torch.tensor(x,dtype=torch.float32)

    if method == 'relu':
        return torch.maximum(torch.tensor(0.0),x).tolist()
    elif method == 'sigmoid':
        return (1 + torch.exp(-x)) ** -1
    elif method == 'tanh':
        return (torch.exp(x) - torch.exp(-x)) / (torch.exp(x) + torch.exp(-x))
    else:
        return torch.where(x>0,x,0.01 * x)
