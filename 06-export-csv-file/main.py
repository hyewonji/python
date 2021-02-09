from flask import Flask, render_template, request, redirect, send_file
from so import get_jobs
from wwr import get_jobs_wwr
from ro import get_jobs_ro
from exporter import save_to_file

app = Flask("SuperScrapper")

db = {}


@app.route("/")  # decorator : @--
def home():
    return render_template("potato.html")


@app.route("/report")
def report():
    word = request.args.get('word')
    if word:
        word = word.lower()
        existingJobs = db.get(word)
        if existingJobs:
            jobs = existingJobs
        else:
            jobs_so = get_jobs(word)
            jobs_wwr = get_jobs_wwr(word)
            jobs_ro = get_jobs_ro(word)
            jobs = jobs_so + jobs_wwr + jobs_ro
            db[word] = jobs
    else:
        return redirect("/")
    return render_template(
        "report.html",
        searchingBy=word,
        resultsNumber=len(jobs),
        jobs=jobs
    )


@app.route("/export")
def export():
    try:
        word = request.args.get('word')
        if not word:
            raise Exception()
        word = word.lower()
        jobs = db[word]
        if not jobs:
            raise Exception()
        save_to_file(jobs)
        return send_file("jobs.csv")
    except:
        return redirect("/")


app.run(host="0.0.0.0")
