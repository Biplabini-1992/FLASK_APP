<<<<<<< HEAD
from flask import Flask

app = Flask(__name__)

# Let's create endpoints
@app.route('/')
def home():
    return "<h1>Flask WebAPI</h1>"

@app.route('/ping')
def pinger():
    return {'message': 'Hello there!'}

=======
from flask import Flask

app = Flask(__name__)

# Let's create endpoints
@app.route('/')
def home():
    return "<h1>Flask WebAPI</h1>"

@app.route('/ping')
def pinger():
    return {'message': 'Hello there!'}

>>>>>>> fb73bfbee66bb660457e45e5e374b8742aaa1f5e
