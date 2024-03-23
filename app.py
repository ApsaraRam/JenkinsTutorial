from flask import *

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Welcome! Universe is listening!<h1/>"

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
