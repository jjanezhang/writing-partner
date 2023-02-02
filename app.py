from flask import Flask, render_template, request
from transformers import pipeline

app = Flask(__name__)

generator = pipeline('text-generation', model = 'gpt2')

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/get_writing", methods=["POST"])
def submit_query():
    if request.method == "POST":
        response = request.form.get("response")
        result = generator(response, max_length=30, num_return_sequences=1)
    return render_template("index.html", result=result)
