#!flask/bin/python

import sys
import broadlink

from flask import Flask, render_template, request, redirect, Response
from flask import jsonify
import random, json

app = Flask(__name__)


devices=broadlink.discover(timeout=10)
devices[0].auth()
devices[1].auth()
devices[2].auth()

print(devices)

@app.route('/')
def output():
	devices = broadlink.discover(timeout=10)
	print(devices)
	return "ho gaya"

@app.route('/receiver', methods = ['GET'])
def worker():
	powerConsum=[]
	dev1power=devices[0].get_energy()
	dev2power=devices[1].get_energy()
	dev3power=devices[2].get_energy()
	powerConsum.append(dev1power);
	powerConsum.append(dev2power);
	powerConsum.append(dev3power);
	print (powerConsum)
	return jsonify(powerConsum)

if __name__ == '__main__':
	# run!
	app.run()