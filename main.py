from flask import Flask, request, jsonify
import os
from functions.strat import dota

# Init app
app = Flask(__name__)
app.config["DEBUG"] = True

# Actual logic
@app.route('/', methods=['GET'])
def home():
    return jsonify({'msg': 'poshel nahui'})


@app.route('/dota/<int:amount>', methods=['GET'])
def dotaStrat(amount):
    return dota(amount)


# Run Server
if __name__ == '__main__':
    app.run()
