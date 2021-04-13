# Guardian_demoN-Shortcut_Launcher

---
## Objectives

### Level 1

* Summary
    * Implement [Shortcut Launcher].
        * Utility program, which allows users to execute specific executable or directory, website via one click.

* Functionality
    * Implemented program is required to:
        * Consisted of 2x4 grid, which every cell is filled with button.
        * Built with single window.
        * Execute specified command below.
    
* Constraints
    * Program have constraints below:
        * Window does not resize.
        * Program command is specified as below:
            * Button #01 : Execute notepad (command: "notepad")
            * Button #02 : Execute calculator (command: "calc")
            * Button #03 : Open C:\ directory (command: "explorer C:\")
            * Button #04 : Browse google.com (command: "start http://www.google.com")
            * Onto other buttons can, but not required to specify any command.
        * Program does not have any UI beside buttons, but not limited.
        * Program runs on Windows OS.
            * Developer does not have to consider of other OS.
        * Window size is specified as 800x200.

---
### Level 2

* Summary
    * Implement [Shortcut Launcher] but with more settings available.
        * Utility program, which allows users to execute specific executable or directory, website via one click.
        * User can set options for program in small range.
    
* Functionality
    * Implemented program is required to:
        * Everything listed in the level 1.
        * Program now have menu.
            * [menu]-[Program settings] : Let users to set program settings noted below.
                * Program settings are displayed on new window.
            * [menu]-[Program Info] : Shows information of program.
            * [menu]-[Exit] : Terminates program.
        * Window frame can be resized.
            * Specify width and height in settings window.
                * Button size must be uniform.
                    * [Button width] = [Window width] / [Grid Column Count]
                    * [Button height] = [Window height] / [Grid Row Count]
        * [Always Top] option is added onto menu.
            * If set, this window needs to be in front of all other programs.
        * User can specify program color.
            * User can set R, G, B value.
            * 0 ≤ [R/G/B value] ≤ 255, Integer.

* Constraints
    * Program have constraints below:
        * Everything listed in the level 1.
        * If unexpected value is set in [menu]-[Program setting], Developer must handle this properly.
    
---
### Level 3

* Summary
    * Implement [Shortcut Launcher] but with more settings available.
        * Utility program, which allows users to execute specific executable or directory, website via one click.
        * User can set options for program in small range.
        * User can set grid row and count in value range.
    
* Functionality
    * Implemented program is required to:
        * Everything listed in the level 2.
        * [menu]-[Program setting] : New feature - Settings window can modify grid column and row count in main window.
            * User can specify row and column directly.
                * Naturally, total button count will be [row] * [column].
                * 2 ≤ [row] ≤ 10, Integer
                * 2 ≤ [column] ≤ 10, Integer
            * Button sequence needs to be intact between grid modification.
                * Ex) Let there are button 1, 2, 3, 4, 5, 6, ... .
                    * If program is set to 2 row and 4 column, button will be placed at [1, 2, 3, 4], [5, 6, 7, 8] for each row.
                    * If program is set to 3 row and 3 column, button will be placed at [1, 2, 3], [4, 5, 6], [7, 8, 9] for each row.
                    * Command must not change between button.
                
* Constraints
    * Program have constraints below:
        * Everything listed in the level 2.
---
### Level 4

* Summary
    * Implement [Shortcut Launcher] but with more settings available.
        * Utility program, which allows users to execute specific executable or directory, website via one click.
        * User can set options for program in small range.
        * User can set grid row and count in value range.
        * User can add label text and color for each button.
    
* Functionality
    * Implemented program is required to:
        * Everything listed in the level 3.
        * [Right click on button] now browse [Button setting] window.
            * Not to be confused with [Program setting] window.
            * User can specify button text and column in [Button setting] window.
            * Command must not change between button while grid modification.
                
* Constraints
    * Program have constraints below:
        * Everything listed in the level 3.

---
### Level 5

* Summary
    * Implement [Shortcut Launcher] but with more settings available.
        * Utility program, which allows users to execute specific executable or directory, website via one click.
        * User can set options for program in small range.
        * User can set grid row and count in value range.
        * User can add label text, command and color for each button.
    
* Functionality
    * Implemented program is required to:
        * Everything listed in the level 4.
        * [Button setting] window modification.
            * Now [Button setting] window should set command string.
            * If command string is not one of the below, button click must do nothing.
                * Directory
                * Valid web url (NOTE: website does not have to be valid.)
                * Executable program w/ path
                
* Constraints
    * Program have constraints below:
        * Everything listed in the level 3.

---
## Objective analysis

* Final objectives: Implement [Shortcut Launcher].
    * Bigger objective : Implement button on GUI.
        * Big objective : Create a window for GUI.
        * Big objective : Create a Button control and add into window.
            * Normal objective : Create a Button control.
            * Normal objective : Create a Grid control for Button placement.
            * Normal objective : Place Grid control into window.
            * Normal objective : Place Button control into Grid control.
 	* Bigger objective : Implement button functionality.
        * Big objective : Implement button left-click functionality.
            * Normal objective : Show text on button, according to label.
            * Normal objective : Paint color on button.
            * Normal objective : Set command on button.
        * Big objective : Implement button right-click functionality.
            * Normal objective : Generate Button setting window.
                * Small objective : Get color information.
                * Small objective : Get label information.
                * Small objective : Get command information.
                    * Smaller objective : Check whether the command is valid.
    * Bigger objective : Implement menu.
        * Big objective : Add menu control details.
        * Big objective : Generate General setting window for program.
            * Normal objective : Get user input of row and column value.
                * Small objective : Check whether the values are in range of 2~10, inclusive.
        * Big objective : Generate Information window for program.

---
## Development environment
### Hardware
* CPU : AMD Ryzen 7 4800H with Radeon Graphics, 2900Mhz, 8 core, 16 logic processor
* RAM : 16.0GB
* SSD : 476.39GB, NTFS, Micron_2200_MTFDHBA512TCK
* GPU : GeForce RTX 3060 Laptop GPU, NVIDIA Compatible

### Software
* OS : Microsoft Windows 10 Home, build 19041, 64 bit
* Dev Framework/Module : Tkinter
    * Reason of using Tkinter
        * Rich amount of reference website
        * Intuitive GUI development interface
* Dev Program : PyCharm
    * Reason of using PyCharm
        * High compatibility of venv and github
        * Speedy intellisense system for python
        * Easy to setting environment
        * Convenient for documentation comment
* Dev Language : Python v3.8.2

---
## Code rule
### Example code

    # variable name
    test_variable = 1

    # class name
    class TestClass:
        def __init__(self):
            # property name
            self.test_property = 1

        # method name
        def test_method(self):
            print(self.test_property)

    if __name__ == "__main__":
        test_variable = TestClass(2)
        test_variable.test_method()