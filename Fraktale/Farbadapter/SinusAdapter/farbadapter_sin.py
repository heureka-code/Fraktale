from Fraktale.Farbadapter.basis_farbadapter import BasisFarbadapter
from .sinus_farbanteil import SinusFarbanteil
import numpy as np


class FarbadapterSin(BasisFarbadapter):
    def __init__(self, anteile: "SinusFarbanteil"):
        self.__anteile = anteile

    @property
    def farbmodus(self) -> str:
        return "RGB"

    def konvertieren(self, data: np.ndarray) -> np.ndarray:
        data = data * 255
        shape = data.shape
        res = np.zeros((shape[0], shape[1], 3))
        res[:, :, 0] = np.round(np.sin(0.024 * data[:, :] + self.__anteile.Red) * 127 + 128)
        res[:, :, 1] = np.round(np.sin(0.024 * data[:, :] + self.__anteile.Green) * 127 + 128)
        res[:, :, 2] = np.round(np.sin(0.024 * data[:, :] + self.__anteile.Blue) * 127 + 128)
        return res
        pass
    pass
