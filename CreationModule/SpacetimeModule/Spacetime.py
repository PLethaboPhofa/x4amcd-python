from CreationModule.InanimateModule.Rock import Rock
from RedisProxyModule import WorldRedisProxy
import numpy as np


class SpaceTime:
    def __init__(self, size):
        self.n = 10 if size is None else size
        self.__spacetime = np.array(
            [[Rock() for _ in range(self.n)] for _ in range(self.n)]
        )

    def refresh(self):
        pass
        # create new redis entry

    def getSpacetime(self):
        return self.__spacetime

    # request for something from space time ( Role checking can be done here)
    # https://stackoverflow.com/questions/59301523/cutting-a-subset-from-middle-of-numpy-array
    def get(self, individual, spaceTimeAOEInputDTO) -> np.array:
        leftBound = -spaceTimeAOEInputDTO.aoe
        rightBound = spaceTimeAOEInputDTO.aoe + 1

        midPoints = self.SightAPI().getUniqueCoordinate(individual, self.__spacetime)
        margins = [
            [bound + minPoint for bound in [leftBound, rightBound]]
            for minPoint in midPoints
        ]

        x_slice = slice(
            max(0, margins[0][0]), min(self.__spacetime[0].size, margins[0][1])
        )
        y_slice = slice(
            max(0, margins[1][0]), min(self.__spacetime[1].size, margins[1][1])
        )

        return self.__spacetime[x_slice, y_slice]
        # get redis entry

    # request that something is done to spacetime
    # or object in spacetime
    def do(self):
        pass
        # do something

    def testRedis(self):
        WorldRedisProxy.set("test", "wow")
        print(WorldRedisProxy.get("test"))
        print("yellow")

    class SightAPI:
        def getUniqueCoordinate(self, individual, spacetime) -> np.array:
            unzippedCoordinates = np.nonzero(spacetime == individual)
            if unzippedCoordinates[0].size == 0:
                raise Exception("individual tried to get but was not found")
            if unzippedCoordinates[0].size > 1:
                raise Exception("individual tried to get but was not unique")
            return list(zip(unzippedCoordinates[0], unzippedCoordinates[1])).pop()
