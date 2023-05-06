import threading
import time
import emoji
from flask import Flask
from creationModule.InanimateModule.Rock import Rock
from creationModule.spacetimeModule.spacetime import SpaceTime
from redisProxyModule import worldRedisProxy
from flaskProxyModule import index
import numpy as np

from utilsModule.PrintUtils import PrintUtils

app = Flask(__name__)
app.register_blueprint(index.index)

def setup():
    global spaceTime 
    spaceTime = SpaceTime()
    print("setup done")

def loop(name):
    while(1):
        PrintUtils.print2DArray(spaceTime.spacetime)
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