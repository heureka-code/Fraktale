from abc import ABC, abstractmethod
from Fraktale.achsen import Achse

import numpy as np


class FraktalWelt(ABC):
    """
    Repraesentation eines Fraktals in einer Welt
    """

    def __init__(self, screen_width: int, screen_height: int, max_iter: int):
        """
        Repraesentation eines Fraktals in einer Welt

        :param screen_width: Die Breite des realen Bildschirms
        :param screen_height: Die Hoehe des realen Bildschirms
        :param max_iter: Die Anzahl an Iterationen, die zur Berechnung des Fraktals genutzt werden

        :type screen_width: int
        :type screen_height: int
        :type max_iter: int
        """

        self.__max_iter: int = max_iter
        self.__width: int = screen_width
        self.__height: int = screen_height
        self.__world_span: int = 4

        self.x_achse = Achse(self.width, self.__world_span, False)
        self.y_achse = Achse(self.height, self.__world_span, True)

        self._data = np.zeros((self.height, self.width), np.uint8)
        pass

    def zoom_in(self, x: int, y: int, factor: float):
        """
        Zoomt in die Welt hinein
        :param x: Die x-Koordinate des Punktes, an den herangezoomt werden soll
        :param y: Die y-Koordinate des Punktes, an den herangezoomt werden soll
        :param factor: Der Faktor, um den gezoomt werden soll
        :return: None

        :type x: int
        :type y: int
        :type factor: float
        """
        self.x_achse.zoom(x, factor)
        self.y_achse.zoom(y, factor)
        self.update_data()
        pass

    def zoom_out(self, x: int, y: int, factor: float):
        """
        Zoomt aus der Welt heraus
        :param x: Die x-Koordinate des Punktes, aus dem herausgezoomt werden soll
        :param y: Die y-Koordinate des Punktes, aus den herausgezoomt werden soll
        :param factor: Der Faktor, um den gezoomt werden soll. (Faktor groesser Eins zoomt raus)
        :return: None

        :type x: int
        :type y: int
        :type factor: float
        """
        self.x_achse.zoom(x, 1 / factor)
        self.y_achse.zoom(y, 1 / factor)
        self.update_data()
        pass

    def left_shift(self, width: float):
        """
        Verschiebt die Betrachtung der Welt nach Links

        :param width: Der Wert, um den verschoben wird
        :type width: float
        :return: None
        """
        self.x_achse.world_start -= (width / self.x_achse.length) * self.x_achse.world_span
        self.update_data()
        pass

    def right_shift(self, width: float):
        """
        Verschiebt die Betrachtung der Welt nach Rechts

        :param width: Der Wert, um den verschoben wird
        :type width: float
        :return: None
        """
        self.x_achse.world_start += (width / self.x_achse.length) * self.x_achse.world_span
        self.update_data()
        pass

    def up_shift(self, width: float):
        """
        Verschiebt die Betrachtung der Welt nach Oben

        :param width: Der Wert, um den verschoben wird
        :type width: float
        :return: None
        """
        self.y_achse.world_start += (width / self.y_achse.length) * self.y_achse.world_span
        self.update_data()
        pass

    def down_shift(self, width: float):
        """
        Verschiebt die Betrachtung der Welt nach Unten

        :param width: Der Wert, um den verschoben wird
        :type width: float
        :return: None
        """
        self.y_achse.world_start -= (width / self.y_achse.length) * self.y_achse.world_span
        self.update_data()
        pass

    def _coordinates(self, x_achse: "Achse" = None, y_achse: "Achse" = None):
        """
        Die einzelnen Koordinaten der Welt (kartesisches Produkt der einzelnen Achsenkoordinaten)

        :param x_achse: Per default die eigene Achse, sonst wird die gegebene Achse genutzt
        :param y_achse: Per default die eigene Achse, sonst wird die gegebene Achse genutzt
        :type x_achse: Achse
        :type y_achse: Achse
        :return: None
        """
        x_achse = x_achse if x_achse else self.x_achse
        y_achse = y_achse if y_achse else self.y_achse

        ima = y_achse.sample_pixel() * 1j
        rea = x_achse.sample_pixel()

        rea = rea.reshape((1, self.x_achse.length))
        ima = ima.reshape((self.y_achse.length, 1))

        z = ima + rea
        return z

    @property
    def width(self) -> int:
        """ Die Breite des Bildschirms, der die Welt darstellen soll """
        return self.__width

    @property
    def height(self) -> int:
        """ Die Hoehe des Bildschirms, der die Welt darstellen soll """
        return self.__height

    @property
    def data(self) -> np.ndarray:
        """ Die berechneten Daten der Welt in Prozent """
        return self._data

    @property
    def max_iter(self) -> int:
        """ Die maximale Anzahl an Iterationen fuer die Berechnung der Welt """
        return self.__max_iter

    @abstractmethod
    def update_data(self):
        """ Abstrakte Methode, die implementiert werden muss, um eine neue Welt zu erstellen. """
        pass
    pass
