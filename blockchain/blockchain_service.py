#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 28 10:31:44 2020

@author: diego
"""

from blockchain import Blockchain

blockchain = Blockchain()

def get_mine_block():
    previous_block = blockchain.get_previous_block()
    previous_proof = previous_block['proof']
    proof = blockchain.proof_of_work(previous_proof)
    previous_hash = blockchain.hash(previous_block)
    block = blockchain.create_block(proof, previous_hash)
    return {
        'message':'Mined a block',
        'index': block['index'],
        'timestamp': block['timestamp'],
        'proof': block['proof'],
        'previous_hash': block['previous_hash']
        }

def get_chain():
    return {
        'chain': blockchain.chain,
        'length': len(blockchain.chain)
        }

def is_chain_valid():
    is_valid = blockchain.is_chain_valid(blockchain.chain)
    if is_valid:
        response = {'message' : 'Blockchain is valid'}
    else:
        response = {'message' : 'Blockchain is not valid'}
    return response        