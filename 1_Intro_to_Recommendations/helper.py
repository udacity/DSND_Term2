import numpy as np

def test_eucl(x, y):
    return np.linalg.norm(x - y)
    

def test_manhat(x, y):
    return sum(abs(e - s) for s,e in zip(x, y))