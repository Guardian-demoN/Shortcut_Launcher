import tkinter
from typing import Union
from typing import Iterable

from utilities.windows import set_window_geometry
from SubWindows import GeneralSettingDialog
from SubWindows import CreditDialog
from ShortcutButton import ShortcutButton


class GridButtonWindow(tkinter.Tk):
    __max_button_row = 10
    __max_button_column = 10
    __max_button_count = 100

    def __init__(
            self,
            screen_name=None,
            base_name=None,
            class_name: str = 'Tk',
            use_tk=1,
            sync=0,
            use=None):
        """
        :param screen_name: tkinter.Tk [screenName] variable.
        :param base_name: tkinter.Tk [baseName] variable.
        :param class_name: tkinter.Tk [className]  variable.
        :param use_tk: tkinter.Tk [useTk] variable.
        :param sync: tkinter.Tk [sync] variable.
        :param use: tkinter.Tk [use] variable.

        Main window for shortcut launcher program.
        """

        tkinter.Tk.__init__(
            self=self,
            screenName=screen_name,
            baseName=base_name,
            className=class_name,
            useTk=use_tk,
            sync=sync,
            use=use)

        self.var_width = tkinter.IntVar(value=800)
        self.var_height = tkinter.IntVar(value=200)
        self.var_rows = tkinter.IntVar(value=2)
        self.var_columns = tkinter.IntVar(value=4)
        self.var_color = tkinter.StringVar(value="#f0f0f0")
        self.var_is_always_top = tkinter.BooleanVar(False)

        self.ui_shortcut_button = [ShortcutButton(self) for _ in range(GridButtonWindow.__max_button_count)]

        window_title = "Guardian_demoN : Shortcut Launcher"

        self.title(window_title)
        self.resizable(False, False)
        set_window_geometry(self, self.var_width.get(), self.var_height.get(), 100, 100)

        self.ui_place_button_all()

        # menu binding
        menu_control: tkinter.Menu = tkinter.Menu(self)

        menu_setting: tkinter.Menu = tkinter.Menu(menu_control, tearoff=0)
        menu_manual: tkinter.Menu = tkinter.Menu(menu_control, tearoff=0)

        menu_control.add_cascade(label="Setting", menu=menu_setting)
        menu_control.add_cascade(label="Manual", menu=menu_manual)

        # 직관: 기존 tkinter의 컨트롤 생성의 대부분 파라미터에 command가 있었으니 이것도 있겠지
        menu_setting.add_checkbutton(label="Always Top",
                                     onvalue=1,
                                     offvalue=0,
                                     variable=self.var_is_always_top,
                                     command=lambda: main_window.attributes('-topmost', self.var_is_always_top.get()))
        menu_setting.add_command(label="Grid Setting", command=self.__command_window_setting)
        menu_setting.add_separator()
        menu_setting.add_command(label="Exit", command=self.__command_exit)
        menu_manual.add_command(label="Credit", command=self.__command_window_credit)

        self.config(menu=menu_control)

    def calculate_button_geometry(self) -> Iterable:
        return self.var_width.get() / self.var_columns.get(), self.var_height.get() / self.var_rows.get()

    def ui_place_button_all(self):
        [self.ui_place_button(i) for i in range(self.__max_button_count)]

    def ui_place_button(
            self,
            button_index: int):
        ui_button_width, ui_button_height = self.calculate_button_geometry()
        self.ui_shortcut_button[button_index].place(
            x=(button_index % self.var_columns.get()) * ui_button_width,
            y=int(button_index / self.var_columns.get()) * ui_button_height,
            width=ui_button_width,
            height=ui_button_height)

    def ui_set_button_info(self, index, text, command, color: Union[str, None] = None):
        self.ui_shortcut_button[index].set_info(text, command, color)

    def __command_window_setting(self):
        """
        __command_window_setting()

        [PRIVATE]

        Command action for [Setting] button. Displays general setting dialog for setting of window.
        """
        # opens up setting
        self.wait_window(GeneralSettingDialog(self, self.var_rows, self.var_columns, self.var_color))

        # set window background as specified color variable, but it would not work since buttons are filling screen.
        # self.config(bg=self.var_color.get())

        # set background of all buttons to be specified color
        [self.ui_shortcut_button[i].set_color_from_parent(self.var_color.get()) for i in range(self.__max_button_count)]

        self.ui_place_button_all()

    def __command_window_credit(self):
        """
        __command_window_credit()

        [PRIVATE]

        Command action for [Credit] button. Displays credit dialog.
        See [CreditDialog] class for more information.
        """
        self.wait_window(CreditDialog(self))

    def __command_exit(self):
        """
        __command_ok()

        [PRIVATE]

        Command action for [exit] menu. terminates shortcut launcher program.
        """
        self.destroy()


if __name__ == "__main__":
    main_window = GridButtonWindow()
    main_window.title("test window")

    main_window.ui_set_button_info(0, "Calculator", "calc")
    main_window.ui_set_button_info(1, "C:\\", "c:\\")
    main_window.ui_set_button_info(2, "e", "e")
    main_window.ui_set_button_info(3, "google", "www.google.com")

    main_window.mainloop()
