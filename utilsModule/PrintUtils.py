from enum import Enum
import emoji
import os 

class PrintUtils:

    spacing = "  "

    def __init__(self) -> None:
        pass

    @staticmethod
    def print2DArray(array) -> None:
        for row in array:
            for item in row:
                print(PrintUtils.spacing+str(item)+PrintUtils.spacing, end='')
            print("\n")

    @staticmethod
    def clearTerminal() -> None:
        os.system('cls' if os.name == 'nt' else 'clear')
            