import tkinter
import tkinter.colorchooser


class ColorChooserDialog(tkinter.colorchooser.Chooser):
    def __init__(self, master, color_value: tkinter.StringVar, **kwargs):
        """
        :param master: window instance to be set as master of current instance
        :param color_value: [ref]tkinter variable for color hex string
        :param kwargs: tkinter kw. keyword arguments to be passed

        General setting dialog for choosing color.

        This window can set following options: row, column, color
        """
        tkinter.colorchooser.Chooser.__init__(self, master=master, **kwargs)

        # backup variables for [cancel] button
        __backup_color = color_value.get()
        result_value = tkinter.colorchooser.Chooser.show(self=self, **kwargs)

        # note that result_value[1] will be [None] if button [Cancel] has been pushed.
        if result_value[1] is not None:
            color_value.set(result_value[1])
        else:
            # restore saved value from init
            color_value.set(__backup_color)


if __name__ == "__main__":
    main_window = tkinter.Tk()

    color = tkinter.StringVar(value="#a0a0a0")
    sub_window = ColorChooserDialog(main_window, color_value=color)

    print(color.get())

    main_window.mainloop()
