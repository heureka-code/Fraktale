from .basis_farbadapter import BasisFarbadapter
import numpy as np


class HSVFarbadapter(BasisFarbadapter):
    def konvertieren(self, data: np.ndarray) -> np.ndarray:
        shape = data.shape
        res = np.zeros((shape[0], shape[1], 3))
        res[:, :, 0] = data[:, :] * 360
        res[:, :, 1] = 100
        res[:, :, 2] = 100
        return res

    @property
    def farbmodus(self) -> str:
        return "HSV"
    pass
