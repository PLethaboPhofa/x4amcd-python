from flask import Flask
from redisProxy import worldRedisProxy
from flaskProxy import index

app = Flask(__name__)
app.register_blueprint(index.index)

def setup():
    print("setup")

def loop():
    print("loop")
    while(1):
        pass    
    
def main():
    worldRedisProxy.set("test", "wow")
    print(worldRedisProxy.get("test"))
    setup()
    loop()

if __name__ == "__main__":
    main()