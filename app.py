from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello from GCP MIG running app.py!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
