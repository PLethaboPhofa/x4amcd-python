from creationModule.InanimateModule.Rock import Rock
from redisProxyModule import worldRedisProxy
import numpy as np


class SpaceTime:

    def __init__(self):
        self.n = 10
        self.spacetime = np.array([[Rock() for i in range(self.n)] for j in range(self.n)])
        pass

    def refresh():
        pass
        # create new redis entry


    # Input request
    def see():
        pass
        # get redis entry


    # request for something from space time ( Role checking can be done here)
    def get(self, spaceTimeAOEInputDTO):
        return 
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
