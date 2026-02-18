# statslib/core/data.py
import numpy as np

class Dataset:
    def __init__(self, data, columns=None, rownames=None):
        # data can be 2D array-like
        self._data = np.asarray(data, dtype=float)
        if self._data.ndim != 2:
            raise ValueError("data must be 2 dimensional")
        n_rows, n_cols = self._data.shape

        if columns is None:
            columns = [f"col_{i}" for i in range(n_cols)]
        else:
            if len(columns) != n_cols:
                raise ValueError("Number of column does not match data columns")
        self.columns = list(columns)

        if rownames is not None:
            if len(rownames) != n_rows:
                raise ValueError("Number of rows names does not match with data rows")
        self.rownames = rownames

    @property
    def shape(self):
        return self._data.shape