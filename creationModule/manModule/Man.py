import numpy as np
from UtilsModule.GlobalsUtil import SPACE_TIME, Globals
from creationModule.spacetimeModule.Model.Thing import Thing


class Man(Thing):
    def __init__(self, eyes) -> None:
        super().__init__()
        self.emoji = "alien"
        self.eyes = eyes

    def see(self) -> np.array:
        return Globals.SPACE_TIME.get(self.eyes)
