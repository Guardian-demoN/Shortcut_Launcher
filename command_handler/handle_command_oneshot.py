from .handle_directory import handle_directory
from .handle_executable import handle_executable
from .handle_web_url import handle_web_url


def handle_command_oneshot(command: str) -> str:
    """
    :param command: command string to be handled
    :return: refined command string. "" will be returned if command is not available

    handle_command_oneshot(command)

    Check whether command is executable. This function will check whether command is either one of these:

    - directory string: converted as [explorer (directory)] so that this command will be executable.
    - web url: converted as [start (url)] so that this address will be executed in web browser.
    - other exe file: returns "as-is" unless exe is not executable or not found. which will returns ""(empty string).
    """
    # NOTE: These three functions below depends on order executed. Do not change these order.
    command = handle_directory(command)
    command = handle_web_url(command)
    command = handle_executable(command)
    return command
