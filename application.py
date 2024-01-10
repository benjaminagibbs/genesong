'''convert genetic sequences to 3 nucleotide codons to music'''

from flask import Flask, render_template, request, redirect, url_for, jsonify

from process import sequence_to_notes


application = app = Flask(__name__)

@app.route('/')
def index():
    return render_template('static/templates/index.html')

@app.route('/process', methods=['POST'])
def process():
    sequence = request.form['sequence']
    notes = sequence_to_notes()
    return jsonify( { 'notes': notes } )