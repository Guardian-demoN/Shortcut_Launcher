from typing import Union
import tkinter
from functools import partial

from SubWindows.ColorChooserDialog import ColorChooserDialog


class GeneralSettingDialog(tkinter.Toplevel):
    def __init__(
            self,
            master: Union[tkinter.Tk, tkinter.Toplevel],
            row_value: tkinter.IntVar,
            column_value: tkinter.IntVar,
            color_value: tkinter.StringVar,
            config: dict = {},
            **kwargs):
        """
        :param master: window
        :param row_value: [ref]tkinter variable for grids row count
        :param column_value: [ref]tkinter variable for girds column count
        :param color_value: [ref]tkinter variable for color hex string
        :param config: tkinter config dictionary parameter
        :param kwargs: tkinter kw. keyword arguments to be passed

        GeneralSettingDialog(master, row_value, column_value, color_value)
        GeneralSettingDialog(master, row_value, column_value, color_value, config)
        GeneralSettingDialog(master, row_value, column_value, color_value, config, **kwargs)

        General setting dialog for grid-button window.

        This window can set following options: row, column, color
        """
        tkinter.Toplevel.__init__(self, master=master, cnf=config, **kwargs)

        # backup variables for [cancel] button
        self.__backup_row: int = row_value.get()
        self.__backup_column: int = column_value.get()
        self.__backup_color: str = color_value.get()

        # save as self variable for use in another method
        self.var_row = row_value
        self.var_column = column_value
        self.var_color = color_value

        # ui placement
        self.geometry("400x200")

        ui_row_label = tkinter.Label(self, text="rows : ")
        ui_row_entry = tkinter.Entry(self, textvariable=row_value)

        ui_column_label = tkinter.Label(self, text="columns : ")
        ui_column_entry = tkinter.Entry(self, textvariable=column_value)

        ui_color_button = tkinter.Button(self, text="Color", command=self.__command_color)
        self.ui_color_label_after = tkinter.Label(self, bg=color_value.get(), borderwidth=1, relief="groove")
        self.ui_color_label_before = tkinter.Label(self, bg=color_value.get(), borderwidth=1, relief="groove")

        ui_button_ok = tkinter.Button(self, text="OK", command=self.__command_ok)
        ui_button_cancel = tkinter.Button(self, text="Cancel", command=self.__command_cancel)

        ui_row_label.place(x=75, y=20, width=100)
        ui_row_entry.place(x=175, y=20, width=100)

        ui_column_label.place(x=75, y=60, width=100)
        ui_column_entry.place(x=175, y=60, width=100)

        ui_color_button.place(x=50, y=100, width=100)

        self.ui_color_label_before.place(x=250, y=100, width=50)
        self.ui_color_label_after.place(x=300, y=100, width=50)

        ui_button_ok.place(x=50, y=140, width=100)
        ui_button_cancel.place(x=250, y=140, width=100)

        # window management: set to front and grab window so that another window cannot be focused instead.
        self.lift(master)
        self.grab_set()

    def __command_ok(self) -> None:
        """
        __command_ok()

        [PRIVATE]

        Command action for [OK] button. applies settings given.
        """
        # check grid row/column range. automatically set as range inclusive.
        if self.var_row.get() <= 2:
            self.var_row.set(2)
        elif self.var_row.get() >= 10:
            self.var_row.set(10)
        if self.var_column.get() <= 2:
            self.var_column.set(2)
        elif self.var_column.get() >= 10:
            self.var_column.set(10)

        self.destroy()

    def __command_cancel(self):
        """
        __command_cancel()

        [PRIVATE]

        Command action for [cancel] button. discard settings given.
        """
        # restore saved value from init
        self.var_row.set(self.__backup_row)
        self.var_column.set(self.__backup_column)
        self.var_color.set(self.__backup_color)

        self.destroy()

    def __command_color(self):
        """
        __command_color()

        [PRIVATE]

        Command action for [color] button. opens color chooser dialog as new window.
        """
        ColorChooserDialog(self, self.var_color)

        # changes label background color for comparison w/ current colored label
        self.ui_color_label_after.config(bg=self.var_color.get())


if __name__ == "__main__":
    # TODO: improve example of [GeneralSettingDialog] class.
    main_window = tkinter.Tk()

    row = tkinter.IntVar(value=3)
    column = tkinter.IntVar(value=4)

    command = tkinter.StringVar()
    color = tkinter.StringVar(value="#F0F0F0")

    button = tkinter.Button(
        main_window,
        text="test",
        command=partial(GeneralSettingDialog, main_window, row, column, color)
                        )

    button.place(x=50, y=100, width=100, height=20)
    sub_window = GeneralSettingDialog(main_window, row_value=row, column_value=column, color_value=color)

    main_window.mainloop()

    print("final value")
    print("row: " + str(row.get()))
    print("column: " + str(column.get()))
