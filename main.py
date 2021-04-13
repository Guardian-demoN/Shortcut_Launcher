# 파일이 날아가서 처음부터 다시 코딩함ㅡㅡ
# ================================
# Shortcut Launcher
# ================================
# Credit: Guardian_demoN
# Development period: 1w (2021-04-05 ~ 2021-04-11)
# Maintenance period: ongoing
# ================================
# Description
# This program allows user to execute program at one click. Improving productivity and efficiency.
# ================================
# References

# Tkinter Programming : https://076923.github.io/posts/Python-tkinter-1/
# Get property from Tkinter control : https://stackoverflow.com/questions/46284901/how-do-i-resize-buttons-in-pixels-tkinter
# Passing function with parameter into button as command : https://www.codespeedy.com/using-lambda-in-gui-programs-in-python/#:~:text=Usage%20of%20the%20lambda%20function%201%20def%20click%28%29%3A,tkinter.Button%28frame%2C%20text%3D%27Click%27%2C%20command%3Dclick%29%2010%20button.pack%28%29%20More%20items...%20
# Checking whether given string is valid url or not : https://www.codespeedy.com/check-if-a-string-is-a-valid-url-or-not-in-python/
# Checking whether given string is directory : https://www.geeksforgeeks.org/python-check-if-a-file-or-directory-exists-2/#:~:text=Check%20if%20a%20directory%20exists%20os.path.isdir%20%28%29%20method,a%20directory%20then%20the%20method%20will%20return%20True.
# Checking whether given string is executable : https://stackoverflow.com/questions/377017/test-if-executable-exists-in-python

# Tkinter right click : https://stackoverflow.com/questions/59696557/tkinter-button-different-commands-on-right-and-left-mouse-click
# Tkinter modal to make dialog : https://stackoverflow.com/questions/45171328/grab-set-in-tkinter-window
# Tkinter placing : https://076923.github.io/posts/Python-tkinter-11/
# Tkinter entry for input : https://pythonbasics.org/tkinter-entry/#:~:text=The%20tkinter%20entry%20box%20lets%20you%20input%20text,types%20of%20input%20%28like%20passwords%29%20entry.%20tkinter%20entry.
# Tkinter new window : https://www.delftstack.com/howto/python-tkinter/how-to-create-a-new-window-with-a-button-in-tkinter/
# Tkinter window close : https://www.tutorialspoint.com/function-to-close-the-window-in-tkinter#:~:text=The%20destroy%20%28%29%20method%20in%20Python%20tkinter%20is,execution%20of%20the%20application%20after%20the%20mainloop%20function.
# Tkinter color chooser : https://coderslegacy.com/python/problem-solving/tkinter-color-chooser/
# Tkinter color chooser : https://www.pythonexample.org/gui/how-to-create-color-picker-with-tkinter-library-in-python/
# Tkinter new window : https://stackoverflow.com/questions/27639298/tkinter-open-a-new-window-with-a-button-prompt
# Tkinter menu : https://pythonguides.com/python-tkinter-menu-bar/
# Tkinter checkButton : https://www.tutorialspoint.com/python/tk_checkbutton.htm
# Tkinter topMost : https://stackoverflow.com/questions/8691655/how-to-put-a-tkinter-window-on-top-of-the-others
# Tkinter wait until the window is closed : https://stackoverflow.com/questions/28388346/what-does-thewait-window-method-do
# ================================
# Version Info
# v0.0.1 2021-04-05 First code write
# v0.0.2 2021-04-06 Step 1 completed with code management
# v0.0.3 2021-04-07 Changed editing program from visual studio -> pyCharm (reason: hard of maintenance)
# v0.0.4 2021-04-08 Total revision: removed all codes which is hard to maintain and replaced all code into OOP.
# v0.0.5 2021-04-09 Added [SubWindows]namespace and its components.
# v0.0.6 2021-04-10 Completed GridButtonWindow class to be functional.
# v0.1.0 2021-04-11 Added commend section and etc for additional maintainability.
# v0.1.1 2021-04-13 Added overview document.
# ================================
# Code rule : pip standard with small changes
# Commend rule : pycharm standard with formatted comments
# ================================
from GridButtonWindow import GridButtonWindow

# TODO: Additional row and column exceptional window (curent: automatically change into range)
# TODO: Resizing option

if __name__ == "__main__":
    main_window = GridButtonWindow()
    main_window.title("Guardian_demoN : Shortcut Launcher")

    main_window.ui_set_button_info(0, "Calculator", "calc")
    main_window.ui_set_button_info(1, "C:\\", "c:\\")
    main_window.ui_set_button_info(2, "e", "e")
    main_window.ui_set_button_info(3, "google", "www.google.com")

    main_window.mainloop()
