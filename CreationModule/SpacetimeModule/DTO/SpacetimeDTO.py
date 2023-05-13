from abc import ABC

class SpaceTimeAOEInputDTO(ABC):

    def __init__(self):
        self.aoe = 0

    @classmethod
    def getAccuity(self):
        return self.aoe