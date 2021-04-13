from typing import Union
import tkinter


def set_window_geometry(
        window: Union[tkinter.Tk, tkinter.Toplevel],
        width: int,
        height: int,
        x: Union[int, None] = None,
        y: Union[int, None] = None) -> None:
    """
    :param window: window instance to be set
    :param width: desired width of the window
    :param height: desired height of the window
    :param x: desired x offset of the window
    :param y: desired y offset of the window

    set_window_geometry(window, width, height)
    set_window_geometry(window, width, height, x, y)

    wrapper function of [window.geometry].

    set window geometry(x, y, width, height) as given parameters.
    """
    if x is None or y is None:
        window.geometry(str(width) + "x" + str(height))
    else:
        window.geometry(str(width) + "x" + str(height) + "+" + str(x) + "+" + str(y))
