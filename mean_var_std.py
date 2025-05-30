import numpy as np
def calculate(lst):
    if len(lst)!=9:
        raise ValueError("List must contain nine numbers.")
    matrix=np.array(lst).reshape(3,3)
    calculations = {
        'mean':               [np.mean(matrix, axis=0).tolist(), np.mean(matrix, axis=1).tolist(), np.mean(matrix)],
        'variance':           [np.var(matrix, axis=0).tolist(), np.var(matrix, axis=1).tolist(), np.var(matrix)],
        'standard deviation': [np.std(matrix, axis=0).tolist(), np.std(matrix, axis=1).tolist(), np.std(matrix)],
        'max':                [np.max(matrix, axis=0).tolist(), np.max(matrix, axis=1).tolist(), np.max(matrix)],
        'min':                [np.min(matrix, axis=0).tolist(), np.min(matrix, axis=1).tolist(), np.min(matrix)],
        'sum':                [np.sum(matrix, axis=0).tolist(), np.sum(matrix, axis=1).tolist(), np.sum(matrix)]
    }
    return calculations
print(calculate([2,6,2,8,4,0,1,5,7]))

