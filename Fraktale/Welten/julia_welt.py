from Fraktale.Welten.basis_welt import FraktalWelt
import numpy as np
from typing import Callable


class JuliaWelt(FraktalWelt):
    """
    Repraesentiert eine Juliamenge in einer eigenen Welt
    """

    def __init__(self, screen_width: int, screen_height: int, c: complex, max_iter: int = 255,
                 f: Callable[[complex, complex], complex] = None):
        """
        Repraesentiert eine Juliamenge in einer eigenen Welt

        :param screen_width: Die Breite des realen Bildschirms
        :param screen_height: Die Hoehe des realen Bildschirms
        :param c: Die komplexe Zahl, zu der die Juliamenge berechnet werden soll
        :param max_iter: Die maximale Anzahl an Iterationen

        :type screen_width: int
        :type screen_height: int
        :type c: complex
        :type max_iter: int
        """

        self.__f: Callable[[complex, complex], complex] = f if f else lambda z, c_v: z ** 2 + c_v
        super(JuliaWelt, self).__init__(screen_width, screen_height, max_iter)
        self.__c = c

        self.update_data()

    def update_data(self):
        z_now = self._coordinates()
        activate = np.full(z_now.shape, True, bool)

        result = np.full(activate.shape, self.max_iter)

        for i in range(self.max_iter):
            z_now[activate] = self.__f(z_now[activate], self.__c)
            new_activate = abs(z_now) < 2
            result[new_activate != activate] = i
            activate = new_activate
        self._data = result / self.max_iter

    @property
    def c(self) -> complex:
        """ Die komplexe Zahl, zu der die Juliamenge erstellt wird """
        return self.__c

    @property
    def f(self) -> Callable[[complex, complex], complex]:
        return self.__f
    pass
