import tkinter
from typing import Union


class CreditDialog(tkinter.Toplevel):
    def __init__(
            self,
            master: Union[tkinter.Tk, tkinter.Toplevel],
            config: dict = {},
            **kwargs):
        """
        :param master: window instance to be set as master of current instance
        :param config: tkinter config dictionary parameter
        :param kwargs: tkinter kw. keyword arguments to be passed

        CreditDialog(master)
        CreditDialog(master, config)
        CreditDialog(master, config, **kwargs)

        Display dialog for credits.
        """
        tkinter.Toplevel.__init__(self, master=master, cnf=config, **kwargs)

        # ui placement
        self.geometry("400x100")

        label_program_name = tkinter.Label(self, text="Shortcut Launcher")
        label_program_credit = tkinter.Label(self, text="Guardian_demoN @ Project_guardiaN")

        label_program_name.pack(pady=15)
        label_program_credit.pack(pady=5)

        # window management: set to front and grab window so that another window cannot be focused instead.
        self.lift(master)
        self.grab_set()


if __name__ == "__main__":
    main_window = tkinter.Tk()

    sub_window = CreditDialog(main_window)

    main_window.mainloop()
