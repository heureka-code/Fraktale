from Fraktale.Welten.basis_welt import FraktalWelt
import numpy as np


class MandelbrotWelt(FraktalWelt):
    """
    Repraesentiert eine Mandelbrotmenge in einer eigenen Welt
    """

    def __init__(self, screen_width: int, screen_height: int, max_iter: int = 255):
        """
        Repraesentiert eine Mandelbrotmenge in einer eigenen Welt

        :param screen_width: Die Breite des realen Bildschirms
        :param screen_height: Die Hoehe des realen Bildschirms
        :param max_iter: Die maximale Anzahl an Iterationen

        :type screen_width: int
        :type screen_height: int
        :type max_iter: int
        """
        super(MandelbrotWelt, self).__init__(screen_width, screen_height, max_iter)

        self.update_data()

    def update_data(self):
        """ Aktualisiert die Welt """
        c_vls = self._coordinates()
        z_now = np.zeros(c_vls.shape, complex)
        activate = np.full(c_vls.shape, True, bool)

        result = np.full(activate.shape, self.max_iter)

        for i in range(self.max_iter):
            z_now[activate] = z_now[activate] ** 2 + c_vls[activate]
            new_activate = abs(z_now) < 2

            result[activate != new_activate] = i
            activate = new_activate

        self._data = result / self.max_iter
