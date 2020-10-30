from flask import Flask, render_template

app = Flask("SuperScrapper")

@app.route("/") #decorator : @--
def home(): 
  return render_template("potato.html")

app.run(host = "0.0.0.0") 
