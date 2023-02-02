from flask import Flask, render_template, request
from transformers import pipeline

app = Flask(__name__)

generator = pipeline('text-generation', model = 'gpt2')

global_results = []

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/restart", methods=["POST"])
def restart():
    global global_results 
    global_results = []
    return render_template("index.html", results=global_results)

@app.route("/get_writing", methods=["POST"])
def get_writing():
    global global_results 
    if request.method == "POST":
        response = request.form.get("response")
        result = generator(response, max_length=50, num_return_sequences=1)[0]
        global_results.append(result["generated_text"])
    return render_template("index.html", results=global_results)
