import threading
import time

import emoji
import numpy as np
from flask import Flask

from CreationModule.InanimateModule.Rock import Rock
from CreationModule.ManModule.Man import Man
from CreationModule.ManModule.OrgansModule.EyesModule.HumanEyes import HumanEyes
from CreationModule.SpacetimeModule.Spacetime import SpaceTime
from FlaskProxyModule import Index
from RedisProxyModule import WorldRedisProxy
from UtilsModule.GlobalsUtil import Globals
from UtilsModule.PrintUtils import PrintUtils

app = Flask(__name__)
app.register_blueprint(Index.index)


def setup():
    Globals.SPACE_TIME = SpaceTime(20)
    global adam
    adam = Adam()
    Globals.SPACE_TIME.getSpacetime()[5][5] = adam
    print("setup done")


def loop(name):
    while 1:
        PrintUtils.print2DArray(Globals.SPACE_TIME.getSpacetime())
        PrintUtils.print2DArray(adam.see())
        PrintUtils.print2DArray(adam.remember())

        time.sleep(1)
        PrintUtils.clearTerminal()


def main():
    setup()
    loopThread = threading.Thread(target=loop, args=(1,), daemon=True)
    loopThread.start()
    while 1:
        x = input()
        print("ack, " + x)


if __name__ == "__main__":
    main()


class Adam:
    def __init__(self) -> None:
        goals = 
        Man.Builder().withEyes(HumanEyes()).withGoals([]).build()
