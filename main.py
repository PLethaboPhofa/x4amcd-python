import threading
import time
import emoji
from flask import Flask
from UtilsModule.GlobalsUtil import Globals
from creationModule.InanimateModule.Rock import Rock
from creationModule.manModule.Man import Man
from creationModule.manModule.organsModule.EyesModule.HumanEyes import HumanEyes
from creationModule.spacetimeModule.spacetime import SpaceTime
from redisProxyModule import worldRedisProxy
from flaskProxyModule import index
import numpy as np

from UtilsModule.PrintUtils import PrintUtils

app = Flask(__name__)
app.register_blueprint(index.index)

def setup():
    Globals.SPACE_TIME = SpaceTime()
    global adam
    adam = Man(HumanEyes())
    Globals.SPACE_TIME.getSpacetime()[5][5] = adam
    print("setup done")

def loop(name):
    while(1):
        PrintUtils.print2DArray(Globals.SPACE_TIME.getSpacetime())
        PrintUtils.print2DArray(adam.see())
        time.sleep(1)
        PrintUtils.clearTerminal()
    
def main():
    setup()
    loopThread = threading.Thread(target=loop, args=(1,), daemon=True)
    loopThread.start()
    while(1):
        x = input()
        print('Hello, ' + x)

if __name__ == "__main__":
    main()