import shutil


def handle_executable(command: str) -> str:
    """
    :param command: command to be handled.
    :return: refined command string. ""(empty string) will be returned if command is not valid.

    handle_executable(command)

    Check given command string is valid directory, and convert into command string with executable.
    """
    # str would be like [command arg1 arg2 arg3 ..]
    # check whether command is one of below:
    # 1. normal executable file -> starts with executable name
    # 2. directory -> starts with explorer
    # 3. web directory -> starts with start
    if shutil.which(command.split(" ")[0]) is not None or command.split(" ")[0] == "start":
        return command
    else:
        return ""
