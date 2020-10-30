from flask import Flask, render_template, request

app = Flask("SuperScrapper")

@app.route("/") #decorator : @--
def home(): 
  return render_template("potato.html")

@app.route("/report")
def report():
  word = request.args.get('word')
  return f"You are looking for a job in {word}"

app.run(host = "0.0.0.0") 