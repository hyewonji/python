from flask import Flask, render_template, request, redirect

app = Flask("SuperScrapper")

@app.route("/") #decorator : @--
def home(): 
  return render_template("potato.html")

@app.route("/report")
def report():
  word = request.args.get('word')
  if word:
      word = word.lower()
    else:
        return redirect("/")

  return render_template("report.html",searchingBy=word )

app.run(host = "0.0.0.0") 