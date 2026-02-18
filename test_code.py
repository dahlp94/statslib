import numpy as np
from statslib.core.data import Dataset

# Create from raw data
data = [[1.0, 2.0], [3.0, 4.0], [5.0, 6.0]]
ds = Dataset(data, columns=["A", "B"])

print(ds.shape) # (3, 2)
print(ds["A"])