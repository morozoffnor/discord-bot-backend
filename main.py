from flask import Flask, request, jsonify
import os
from functions.strat import dota
from functions.corona import currentCorona, newCorona
from functions.webStrat import singledraft

# Init app
app = Flask(__name__)
app.config["DEBUG"] = True
basedir = os.path.abspath(os.path.dirname(__file__))


# Actual logic
@app.route('/', methods=['GET'])
def home():
    return jsonify({'msg': 'poshel nahui'})


@app.route('/dota/<int:amount>', methods=['GET'])
def dotaStrat(amount):
    return dota(amount)


@app.route('/dota/singledraft')
def getsingledraft():
    return singledraft()


@app.route('/corona/current', methods=['GET'])
def getCurrentCorona():
    return jsonify(currentCorona())


@app.route('/corona/new', methods=['POST'])
def postNewCorona():
    data = request.data
    return newCorona(data)


# Run Server
if __name__ == '__main__':
    app.run()
