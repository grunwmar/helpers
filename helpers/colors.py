"""Colorize console output"""


class Clrs:

    RESET: str = "\033[0m"
    BOLD: str = "\033[1m"
    SHADOW: str = "\033[2m"
    ITALIC: str = "\033[3m"

    FG_RED: str = "\033[31m"
    FG_GREEN: str = "\033[32m"
    FG_YELLOW: str = "\033[33m"
    FG_BLUE: str = "\033[34m"
    FG_MAGENTA: str = "\033[35m"
    FG_CYAN: str = "\033[36m"
    FG_WHITE: str = "\033[37m"

    BG_RED: str = "\033[41m"
    BG_GREEN: str = "\033[42m"
    BG_YELLOW: str = "\033[43m"
    BG_BLUE: str = "\033[44m"
    BG_MAGENTA: str = "\033[45m"
    BG_CYAN: str = "\033[46m"
    BG_WHITE: str = "\033[47m"

    @staticmethod
    def list(*args: int) -> str:
        """Uses tuple of ANSI codes to colorize text."""
        """ Returns \033[<codes>m string. """

        args_str = ";".join([str(arg) for arg in args])
        return f"\033[{args_str}m"

    def __init__(self, *args: int) -> None:
        """Uses tuple of ANSI codes to colorize text."""
        """ Sets them as string variable for object. """

        self._args_str = ";".join([str(arg) for arg in args])

    def __ror__(self, string: str) -> str:
        """Uses | operator to apply color codes to a string."""
        """ Syntax: 'Some string content' | clsrs_instance """

        return f"\033[{self._args_str}m{string}{self.RESET}"
