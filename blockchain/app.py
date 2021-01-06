#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 28 10:35:52 2020

@author: diego
"""

from flask import Flask, jsonify
          
from blockchain_service import get_mine_block, get_chain, is_chain_valid

app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = False

@app.route('/mine_block', methods = ['GET'])
def mine_block():
    return jsonify(get_mine_block()), 200
 
@app.route('/chain', methods = ['GET'])
def chain():
    return jsonify(get_chain()), 200


@app.route('/valid_chain', methods = ['GET'])
def valid_chain():
    return jsonify(is_chain_valid()), 200


app.run(host= '0.0.0.0', port=5000)