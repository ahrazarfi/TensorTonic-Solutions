import torch

def tensor_op(x, y, op):
    """
    Returns: list (result tensor converted via .tolist())
    """
    x = torch.tensor(x, dtype= torch.float32)
    y = torch.tensor(y, dtype= torch.float32)
    if op == 'add':
        return torch.add(x,y).tolist()
    elif op == 'multiply':
        return torch.mul(x,y).tolist()
    elif op == 'matmul':
        a = x @ y
        return a.tolist()
    elif  op == 'power':
        return torch.pow(x,y).tolist()
    else:
        return torch.max(x,y).tolist()
    pass