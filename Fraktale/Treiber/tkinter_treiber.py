from abc import ABC, abstractmethod

import numpy as np
import tkinter
from PIL import Image, ImageTk
from Fraktale.Treiber.basis_treiber import BasisTreiber
from Fraktale.Welten.basis_welt import FraktalWelt
from Fraktale.Welten import MandelbrotWelt, JuliaWelt


class TkinterTreiber(BasisTreiber):
    def __init__(self, screen_width: int, screen_height: int, welt, farbadapter):
        super(TkinterTreiber, self).__init__(screen_width, screen_height, welt, farbadapter)
        self._zoom_number = 0
        self._zoom_factor = 1.25

        self._init_root_and_canvas()
        self.root.bind("<MouseWheel>", self._zoom)
        self.root.bind("<Left>", self._left_shift)
        self.root.bind("<Right>", self._right_shift)
        self.root.bind("<Down>", self._down_shift)
        self.root.bind("<Up>", self._up_shift)
        self.root.bind("<KeyPress>", self._key_pressed)
        self._init_image()
        self._add_image()

    def _key_pressed(self, event):
        if event.char.lower() == "c":
            self._print_coordinate()
        if event.char.lower() == "j":
            self._show_julia()
        if event.char.lower() == "m":
            self._show_mandelbrot()
        if event.char.lower() == "s":
            self._save_image()

    def _save_image(self):
        zoom_suffix = f"_{self._zoom_factor ** self._zoom_number}_{self._zoom_factor}"
        try:
            xy_prefix = f"{self.welt.c.real, self.welt.c.imag}_"
        except AttributeError:
            xy_prefix = ""
        finally:
            xy_prefix += f"{self._pointer_coordinates}"
        self._pil_img.save(
            "img/" + f"{'mandelbrot' if isinstance(self.welt, MandelbrotWelt) else ''}{xy_prefix}{zoom_suffix}.png")

    def _show_julia(self):
        if isinstance(self.welt, MandelbrotWelt):
            x, y = self._pointer_coordinates
            c = x + y * 1j
            print(c)
            self._welt = JuliaWelt(self.width, self.height, c, self.welt.max_iter)
            self._update_canvas()

    def _show_mandelbrot(self):
        if isinstance(self.welt, JuliaWelt):
            self._welt = MandelbrotWelt(self.width, self.height, self.welt.max_iter)
            self._update_canvas()

    def _print_coordinate(self):
        x, y = self._pointer_coordinates
        print(f"{x}{'+' if y >=0 else ''}{y}j")

    @property
    def _pointer_coordinates(self):
        x = self.root.winfo_pointerx() - self.root.winfo_rootx()
        y = self.root.winfo_pointery() - self.root.winfo_rooty()
        w_x = self.welt.x_achse.pixel2world(x)
        w_y = self.welt.y_achse.pixel2world(y)
        return w_x, w_y

    def _left_shift(self, event):
        self.welt.left_shift(50)
        self._update_canvas()

    def _up_shift(self, event):
        self.welt.up_shift(50)
        self._update_canvas()

    def _down_shift(self, event):
        self.welt.down_shift(50)
        self._update_canvas()

    def _right_shift(self, event):
        self.welt.right_shift(50)
        self._update_canvas()

    def _zoom(self, event):
        if event.delta > 0:
            self._zoom_number += 1
            self.welt.zoom_in(event.x, event.y, self._zoom_factor)
        else:
            self._zoom_number -= 1
            self.welt.zoom_out(event.x, event.y, self._zoom_factor)
        self._update_canvas()

        pass

    def start_loop(self):
        self._update_canvas()

        self.canvas.pack()
        self.canvas.mainloop()

    def _init_root_and_canvas(self):
        self.root: tkinter.Tk = tkinter.Tk("Fraktale")
        self.root.title("Fraktale")
        self.root.minsize(self.height, self.width)
        self.root.maxsize(self.height, self.width)
        self.canvas = tkinter.Canvas(master=self.root, width=self.width, height=self.height)

    def _init_image(self):
        self.__img = ImageTk.PhotoImage(image=Image.new(self.farbadapter.farbmodus, (self.width, self.height), "black"))

    def _add_image(self):
        self.canvas.create_image(0, 0, anchor="nw", image=self.img)

    def _put_canvas_in_image(self) -> np.ndarray:
        return self.calc_data()

    def _update_canvas(self):
        to_show = self._put_canvas_in_image()
        self._pil_img = Image.fromarray(np.uint8(to_show))
        self.img.paste(self._pil_img)

    @property
    def img(self) -> ImageTk.PhotoImage:
        return self.__img

    pass
