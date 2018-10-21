import subprocess
import sys
#'''
def install(package):
    subprocess.call([sys.executable, "-m", "pip", "install", package])

install("Flask==0.10.0")
install('pymongo==3.0.3')

#'''
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_method():
    return "Hello World"

if __name__ == '__main__':
    app.run()