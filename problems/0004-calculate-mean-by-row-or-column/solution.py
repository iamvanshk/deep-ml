import torch

def calculate_matrix_mean(matrix, mode: str) -> torch.Tensor:

    a_t = torch.as_tensor(matrix, dtype=torch.float)

    if mode.lower() == 'row':
        return a_t.mean(dim=1)

    elif mode.lower() == 'column':
        return a_t.mean(dim=0)

    else:
        raise ValueError("mode must be 'row' or 'column'")
    return []
    pass