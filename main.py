from Fraktale import make_tkinter, Welten
from Fraktale.Farbadapter import GraustufenFarbadapter
from Fraktale.Farbadapter import SinusAdapter


if __name__ == "__main__":
    treiber = make_tkinter(
        Welten.MandelbrotWelt,
        SinusAdapter.FarbadapterSin(anteile=SinusAdapter.SinusFarbanteil(-0.99999, -1.12, 2.32)),
        1080, 1080
    )
    treiber.start_loop()
