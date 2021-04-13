import os


def handle_directory(command: str) -> str:
    """
    :param command: command to be handled.
    :return: refined command string. [explorer (command)] will be returned if command is valid directory.

    handle_directory(command)

    Check given command string is valid directory, and convert into command string with executable.
    """
    if os.path.isdir(command) is True:
        command = "explorer " + command
    return command
