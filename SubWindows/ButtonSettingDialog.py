import tkinter
from typing import Union
from functools import partial

from command_handler import handle_command_oneshot
from SubWindows import ColorChooserDialog


class ButtonSettingDialog(tkinter.Toplevel):
    def __init__(
            self,
            master: Union[tkinter.Tk, tkinter.Toplevel],
            text_value: tkinter.StringVar,
            command_value: tkinter.StringVar,
            color_value: tkinter.StringVar,
            config: dict = {},
            **kwargs):
        """
        :param master: window instance to be set as master of current instance
        :param text_value: [ref]tkinter variable for text to be displayed in front of button
        :param command_value: [ref]tkinter variable for command to be executed when button has been pressed
        :param color_value: [ref]tkinter variable for color hex string
        :param config: tkinter config dictionary parameter
        :param kwargs: tkinter kw. keyword arguments to be passed

        ButtonSettingDialog(master, text_value, command_value, color_value)
        ButtonSettingDialog(master, text_value, command_value, color_value, config)
        ButtonSettingDialog(master, text_value, command_value, color_value, config, **kwargs)

        General setting dialog for grid-button window(opens when the shortcut button has been right-clicked).

        This window can set following options: text, color, command
        """
        tkinter.Toplevel.__init__(self, master=master, cnf=config, **kwargs)

        # backup row and column value for [cancel] button
        self.__backup_command: str = command_value.get()
        self.__backup_color: str = color_value.get()
        self.__backup_text = text_value.get()

        # save as self variable for use in another method
        self.text_value = text_value
        self.command_value = command_value
        self.color_value = color_value

        # ui placement
        self.geometry("400x200")

        ui_label_text = tkinter.Label(self, text="text : ")
        ui_entry_text = tkinter.Entry(self, textvariable=text_value)

        ui_label_command = tkinter.Label(self, text="command : ")
        ui_entry_command = tkinter.Entry(self, textvariable=command_value)

        color_button = tkinter.Button(self, text="Color", command=self.__command_color)
        self.color_label_after = tkinter.Label(self, bg=color_value.get(), borderwidth=1, relief="groove")
        self.color_label_before = tkinter.Label(self, bg=color_value.get(), borderwidth=1, relief="groove")

        ui_button_ok = tkinter.Button(self, text="OK", command=self.__command_ok)
        ui_button_cancel = tkinter.Button(self, text="Cancel", command=self.__command_cancel)

        ui_label_text.place(x=50, y=20, width=100)
        ui_entry_text.place(x=150, y=20, width=200)

        ui_label_command.place(x=50, y=60, width=100)
        ui_entry_command.place(x=150, y=60, width=200)

        color_button.place(x=50, y=100, width=100)

        self.color_label_before.place(x=250, y=100, width=50)
        self.color_label_after.place(x=300, y=100, width=50)

        ui_button_ok.place(x=50, y=140, width=100)
        ui_button_cancel.place(x=250, y=140, width=100)

        # window management: set to front and grab window so that another window cannot be focused instead.
        self.lift(master)
        self.grab_set()

    def __command_color(self):
        """
        __command_color()

        [PRIVATE]

        Command action for [color] button. opens color chooser dialog as new window.
        """
        ColorChooserDialog(self, color_value=self.color_value)
        self.color_label_after.config(bg=self.color_value.get())

    def __command_ok(self):
        """
        __command_ok()

        [PRIVATE]

        Command action for [OK] button. applies settings given.
        """
        # refine command for [not executable], [web directory] and [os directory]
        refined_command = handle_command_oneshot(self.command_value.get())
        self.command_value.set(refined_command)

        self.destroy()

    def __command_cancel(self):
        """
        __command_ok()

        [PRIVATE]

        Command action for [cancel] button. discard settings given.
        """
        # restore saved value from init
        self.text_value.set(self.__backup_text)
        self.command_value.set(self.__backup_command)
        self.color_value.set(self.__backup_color)

        self.destroy()


if __name__ == "__main__":
    main_window = tkinter.Tk()

    text = tkinter.StringVar(value="test")
    command = tkinter.StringVar(value="D:\\")
    color = tkinter.StringVar(value="#F0F0F0")

    button = tkinter.Button(
        main_window,
        text="test",
        command=partial(ButtonSettingDialog, main_window, text, command, color)
    )
    button.place(x=50, y=100, width=100, height=20)

    print()

    main_window.mainloop()
