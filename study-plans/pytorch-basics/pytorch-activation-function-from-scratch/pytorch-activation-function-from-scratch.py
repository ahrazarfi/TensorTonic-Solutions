import torch
import math

def activate(x, method="relu"):
    """
    Returns: list (activated tensor converted via .tolist())
    """
    x = torch.tensor(x,dtype=torch.float32)

    if method == 'relu':
        # return torch.maximum(x, torch.tensor(0.0))
        # return torch.where(x>0,x,0)
        return torch.clamp(x,min=0.0).tolist()
    elif method == 'sigmoid':
        # return [1 / (1 + math.exp(-v.item())) for v in x]
        return (1.0 / (1.0 + torch.exp(-x))).tolist()
    elif method == 'tanh':
        return torch.tanh(x).tolist()
    else:
        # return torch.clip(x, min=0.01 * x)
        return torch.where(x>0,x,0.01*x)
    pass