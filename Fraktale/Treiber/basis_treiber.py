from abc import ABC, abstractmethod
from Fraktale.Farbadapter import BasisFarbadapter
from Fraktale.Welten.basis_welt import FraktalWelt
import numpy as np


class BasisTreiber(ABC):
    def __init__(self,
                 screen_width: int, screen_height: int,
                 welt, farbadapter: BasisFarbadapter):
        self._welt: FraktalWelt = welt
        self._farbadapter = farbadapter
        self.__width = screen_width
        self.__height = screen_height

    def calc_data(self) -> np.ndarray:
        return self._farbadapter.konvertieren(self.welt.data)

    @property
    def farbadapter(self):
        return self._farbadapter

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @property
    def welt(self) -> "FraktalWelt":
        return self._welt
    pass
