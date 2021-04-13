import validators


def handle_web_url(command: str) -> str:
    """
    :param command: command to be handled.
    :return: refined command string. [start (command)] will be returned if command is not valid.

    handle_executable(command)

    Check given command string is valid directory, and convert into command string with executable.
    """
    command = command.lower()

    if command.split(".")[0] == "www":
        command = "https://" + command

    if validators.url(command) is True:
        command = "start " + command
    return command
