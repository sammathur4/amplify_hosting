from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return {1:"A"}

if __name__ == '__main__':
    app.run()
