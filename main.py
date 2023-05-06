from flask import Flask
from redisProxy import worldRedisProxy
from flaskProxy import index
from creationModule.spacetimeModule import spacetime
import numpy as np

app = Flask(__name__)
app.register_blueprint(index.index)


def setup():
    this.adam = 
    print("setup")

def loop():
    print("loop")
    while(1):
        pass    
    
def main():
    spacetime.test()
    setup()
    loop()

if __name__ == "__main__":
    main()