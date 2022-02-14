from .basis_farbadapter import BasisFarbadapter
import numpy as np


class GraustufenFarbadapter(BasisFarbadapter):
    def konvertieren(self, data: np.ndarray) -> np.ndarray:
        return data * 255

    @property
    def farbmodus(self) -> str:
        return "L"
