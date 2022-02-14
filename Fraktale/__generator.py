from Fraktale.Treiber.basis_treiber import BasisTreiber
from Fraktale.Welten.basis_welt import FraktalWelt
from Fraktale.Farbadapter.basis_farbadapter import BasisFarbadapter

from Fraktale.Welten import JuliaWelt, MandelbrotWelt

from Fraktale.Treiber import TkinterTreiber


def make(welt_cls: type[FraktalWelt],
         treiber_cls: type[BasisTreiber],
         adapter: BasisFarbadapter,
         width: int, height: int,
         max_iter: int = 255, c: complex = None):
    assert issubclass(welt_cls, FraktalWelt)
    assert issubclass(treiber_cls, BasisTreiber)
    assert isinstance(adapter, BasisFarbadapter)

    if issubclass(welt_cls, JuliaWelt):
        assert c is not None, "Fuer die Julia-Menge ist ein c erforderlich"

    if issubclass(welt_cls, MandelbrotWelt):
        assert c is None, "Bei der Mandelbrotmenge darf c nicht gesetzt sein"
        welt = welt_cls(width, height, max_iter)
    else:
        welt = welt_cls(screen_width=width, screen_height=height, max_iter=max_iter, c=c)
    treiber = treiber_cls(width, height, welt, adapter)
    return treiber


def make_tkinter(welt_cls: type[FraktalWelt],
                 adapter: BasisFarbadapter,
                 width: int, height: int, max_iter: int = 255, c=None) -> TkinterTreiber:
    res = make(welt_cls, TkinterTreiber, adapter, width, height, max_iter, c=c)
    res.start_loop()
    return res
