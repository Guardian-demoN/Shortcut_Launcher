from typing import Union
import tkinter


class GridSettingDialog(tkinter.Toplevel):
    def __init__(
            self,
            master: Union[tkinter.Tk, tkinter.Toplevel],
            row_value: tkinter.IntVar,
            column_value: tkinter.IntVar,
            config: dict = {},
            **kwargs):
        """
        :param master: window instance to be set as master of current instance
        :param row_value: [ref]tkinter variable for grids row count
        :param column_value: [ref]tkinter variable for girds column count
        :param config: tkinter config dictionary parameter
        :param kwargs: tkinter kw. keyword arguments to be passed

        GridSettingDialog(master, row_value, column_value)
        GridSettingDialog(master, row_value, column_value, config)
        GridSettingDialog(master, row_value, column_value, config, kwargs)

        [UNUSED]Grid setting dialog for grid-button window.

        This window can set following options: row, column
        """
        tkinter.Toplevel.__init__(self, master=master, cnf=config, **kwargs)

        # backup variables for [cancel] button
        self.__backup_row: int = row_value.get()
        self.__backup_column: int = column_value.get()

        # save as self variable for use in another method
        self.var_row = row_value
        self.var_column = column_value

        # ui placement
        self.geometry("400x200")

        ui_row_label = tkinter.Label(self, text="rows : ")
        ui_row_entry = tkinter.Entry(self, textvariable=row_value)

        ui_column_label = tkinter.Label(self, text="columns : ")
        ui_column_entry = tkinter.Entry(self, textvariable=column_value)

        ui_button_ok = tkinter.Button(self, text="OK", command=self.__command_ok)
        ui_button_cancel = tkinter.Button(self, text="Cancel", command=self.__command_cancel)

        ui_row_label.place(x=75, y=20, width=100)
        ui_row_entry.place(x=175, y=20, width=100)

        ui_column_label.place(x=75, y=60, width=100)
        ui_column_entry.place(x=175, y=60, width=100)

        ui_button_ok.place(x=50, y=140, width=100)
        ui_button_cancel.place(x=250, y=140, width=100)

        # window management: set to front and grab window so that another window cannot be focused instead.
        self.lift(master)
        self.grab_set()

    def __command_ok(self):
        """
        __command_ok()

        [PRIVATE]

        Command action for [OK] button. applies settings given.
        """
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

        self.destroy()


if __name__ == "__main__":
    main_window = tkinter.Tk()

    row = tkinter.IntVar(value=3)
    column = tkinter.IntVar(value=4)

    sub_window = GridSettingDialog(main_window, row_value=row, column_value=column)

    main_window.mainloop()

    print("final value")
    print("row: " + str(row.get()))
    print("column: " + str(column.get()))
