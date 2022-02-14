from abc import ABC, abstractmethod
import numpy as np


class BasisFarbadapter(ABC):
    @abstractmethod
    def konvertieren(self, data: np.ndarray) -> np.ndarray:
        pass

    @property
    @abstractmethod
    def farbmodus(self) -> str:
        pass
    pass
