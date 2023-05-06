from creationModule.InanimateModule.Rock import Rock
from redisProxyModule import worldRedisProxy
import numpy as np


class SpaceTime:

    def __init__(self):
        self.n = 10
        self.__spacetime = np.array([[Rock() for i in range(self.n)] for j in range(self.n)])
        pass

    def refresh():
        pass
        # create new redis entry

    def getSpacetime(self):
        return self.__spacetime

    # request for something from space time ( Role checking can be done here)
    # https://stackoverflow.com/questions/59301523/cutting-a-subset-from-middle-of-numpy-array
    def get(self, spaceTimeAOEInputDTO) -> np.array:

        leftBound = -spaceTimeAOEInputDTO.aoe
        rightBound = spaceTimeAOEInputDTO.aoe+1 
        
        midPoints = [round(dim / 2) for dim in self.__spacetime.shape]
        margins = [[bound + minPoint for bound in [leftBound, rightBound]] for minPoint in midPoints]

        x_slice = slice(max(0,margins[0][0]), min(self.__spacetime[0].size,margins[0][1]))
        y_slice = slice(max(0,margins[1][0]), min(self.__spacetime[1].size,margins[1][1]))

        return self.__spacetime[x_slice, y_slice]
        # get redis entry


    # request that something is done to spacetime
    # or object in spacetime
    def do():
        pass
        # do something


    def test():
        worldRedisProxy.set("test", "wow")
        print(worldRedisProxy.get("test"))
        print("yellow")
