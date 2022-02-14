from Fraktale import make_tkinter, Welten, Treiber
from Fraktale.Farbadapter.SinusAdapter import *
from Fraktale.Farbadapter import GraustufenFarbadapter
from os import mkdir


if __name__ == "__main__":
    try:
        mkdir("img")
    except FileExistsError:
        pass
    treiber = make_tkinter(Welten.JuliaWelt,
                           GraustufenFarbadapter(),
                           1080, 1080, c=0.3222222222222224+0.5666666666666667j)
    treiber.start_loop()
