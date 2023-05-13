import numpy as np
from UtilsModule.GlobalsUtil import SPACE_TIME, Globals
from CreationModule.SpacetimeModule.Model.Thing import Thing


class Man(Thing):
    def __init__(self, eyes, goals) -> None:
        super().__init__()
        self.emoji = "neutral_face"
        self.eyes = eyes
        self.goals = goals

    def see(self) -> np.array:
        return Globals.SPACE_TIME.get(self, self.eyes)
    
    def remember(self) -> np.array:
        

    class Builder:
        def __init__(self) -> None:
            pass

        def withEyes(self, eyes) -> "Builder":
            self.eyes = eyes
            return self

        def withGoals(self, goals) -> "Builder":
            self.goals = goals
            return self

        def build(self) -> Man:
            return Man(self.eyes, self.goals)
