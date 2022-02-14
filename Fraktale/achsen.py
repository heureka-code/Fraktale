import numpy as np


class Achse:
    """
    Klasse zur Abstraktion einer Koordinatenachse
    """

    def __init__(self, length_on_screen: int, world_span: int, inverted: bool, world_start: float = None):
        """
        Klasse zur Abstraktion einer Koordinatenachse

        :param length_on_screen: Die Anzahl an Pixeln in Richtung der Achse.
        :param world_span: Die Laenge der Achse innerhalb der Welt
        :param inverted: Gibt an, in welche Richtung die Achse verlaeuft
        :param world_start: Die kleinste Koordinate, die innerhalb der Welt auf der Achse dargestellt wird.
        """
        self.__inverted_sign = -1 if inverted else 1
        self.length = length_on_screen
        self.world_span = world_span
        if world_start is not None:
            self.world_start = world_start
        else:
            self.world_start = -self.__inverted_sign * self.world_span / 2

    @property
    def world_end(self):
        """
        Property-Attribut, dass den End-Wert der in der Welt befindlichen Achse errechnet.
        :rtype: float
        """
        return self.world_start + self.__inverted_sign * self.span

    def sample_pixel(self):
        """
        Berechnet den Vektor aus unterschiedlichen Koordinatenpunkten, die berechnet werden sollen.
        :return: Einen Vektor aus den darzustellenden Koordinaten
        :rtype: np.ndarray
        """
        return np.linspace(0., self.__inverted_sign * self.world_span, self.length) + self.world_start

    def pixel2world(self, pixel: int) -> float:
        """
        Berechnet die Welt-Koordinate zu einem Pixel
        :type pixel: int
        :param pixel: Die Koordinate des Pixels auf der Achse
        :return: Die Welt-Koordinate auf der Achse
        :rtype: float
        """
        pixel *= self.__inverted_sign
        return pixel * self.world_span / self.length + self.world_start

    def world2pixel(self, world: float) -> int:
        """
        Berechnet als Gegenstueck zu pixel2world eine Welt-Koordinate in den dazugehoerigen Pixel um
        :param world: Die umzurechnende Welt-Koordinate
        :return: Die umgerechnete Pixel-Koordinate.
        :rtype: int
        :type world: float
        """
        return int(self.__inverted_sign * (world - self.world_start) * self.length / self.world_span)

    def zoom(self, pixel: int, factor: float):
        """
        Zoomt eine gewisse Pixel-Koordinate auf einen gegebenen Faktor
        :param pixel: Die Koordinate, auf die gezoomt werden soll
        :param factor: Der Faktor, um den gezoomt werden soll
        :type pixel: int
        :type factor: float
        :return: None
        """
        oldpos = self.pixel2world(pixel)
        world_distance_from_start = pixel / self.length * self.world_span
        self.world_start = oldpos - self.__inverted_sign * world_distance_from_start / factor
        self.world_span /= factor

    def __str__(self):
        return f"<Achse screen={self.length} {self.world_start}-{self.world_end} ({self.world_span})>"

    def __repr__(self):
        return f"Achse({self.length}, {self.world_span}, {self.__inverted_sign == -1}, {self.world_start})"
    pass
