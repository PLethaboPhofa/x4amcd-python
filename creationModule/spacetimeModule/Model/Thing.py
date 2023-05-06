from abc import ABC

import emoji

class Thing(ABC):
    def __init__(self) -> None:
        self.emoji = "alien_monster"
        pass

    def __str__(self) -> str:
        return emoji.emojize(':'+self.emoji+':')
    