from typing import Union
from functools import partial
import os
import tkinter

from command_handler import handle_command_oneshot
from SubWindows import ButtonSettingDialog


class ShortcutButton(tkinter.Button):
    info_count: int = 0

    def __init__(
            self,
            master: Union[tkinter.Toplevel, tkinter.Tk],
            command: Union[str, None] = None,
            text: Union[str, None] = None,
            config: dict = {}, **kwargs) -> None:
        """
        :param master: master tkinter ui component
        :param command: os command to execute
        :param text: text to display in button
        :param config: tkinter config dictionary
        :param kwargs: other keyword options

        ShortcutButton(master)
        ShortcutButton(master, command)
        ShortcutButton(master, command, text)
        ShortcutButton(master, command, text, config)

        Tkinter button derived class. Includes command and text, button color information.
        """
        tkinter.Button.__init__(self=self, master=master, cnf=config, **kwargs)
        self.master = master

        self.var_command = tkinter.StringVar(value=command)
        self.var_text = tkinter.StringVar(value=text)
        self.var_button_color = tkinter.StringVar(value="#f0f0f0")
        self.var_is_color_changed = tkinter.BooleanVar(value=False)

        self.index = ShortcutButton.info_count
        ShortcutButton.info_count = ShortcutButton.info_count + 1

        self.bind("<Button-3>", self.__command_right_click)

    def ui_refresh(self) -> None:
        """
        ui_refresh()

        Refreshes current window ui as given configuration.
        """
        # ensure that command is valid command string
        command = handle_command_oneshot(self.var_command.get())

        self.config(bg=self.var_button_color.get())
        self.config(activebackground=self.var_button_color.get())
        self.config(command=partial(os.system, command))
        self.config(text=self.var_text.get())

    def set_color_from_parent(self, color):
        if self.var_is_color_changed.get() is False:
            self.var_button_color.set(color)
            self.config(bg=color)
            self.config(activebackground=color)

    def set_info(self, text, command, background: Union[str, None] = None):

        self.var_text.set(text)
        self.var_command.set(command)
        if self.var_button_color.get() != background and background is not None:
            self.var_is_color_changed.set(True)

        if background is not None:
            self.var_button_color.set(background)

        self.ui_refresh()

    def __command_right_click(self, event):
        """
        __command_right_click()

        [PRIVATE]

        Command action for [button right click]. opens button setting dialog as new window.
        """
        self.wait_window(ButtonSettingDialog(
            master=self.master,
            text_value=self.var_text,
            command_value=self.var_command,
            color_value=self.var_button_color))

        self.ui_refresh()
