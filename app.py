#coding: utf-8

from flask import (Flask, render_template, redirect, flash)
import flask.ext.login
import hashlib

import database
import forms


app = Flask(__name__)
app.debug = True

@app.route('/')
def list_tasks():
	pass

@app.route('/create_task', methods=['GET', 'POST'])
def create_task():
	pass

@app.route('/task_done/<int:taskid>', methods=['GET', 'POST'])
def task_done():
	pass

@app.route('/delete_done_tasks', methods=['GET', 'POST']])
def delete_done_tasks():
	pass

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=1337)