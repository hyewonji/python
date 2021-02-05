import requests
import json
from bs4 import BeautifulSoup
from flask import Flask, render_template, request, redirect


app = Flask("DayNine")

base_url = "http://hn.algolia.com/api/v1"
# This URL gets the newest stories.
new = f"{base_url}/search_by_date?tags=story"
# This URL gets the most popular stories
popular = f"{base_url}/search?tags=story"


news_request = requests.get(new)
news_soup = str(BeautifulSoup(news_request.text, "html.parser"))
news_text = json.loads(news_soup)
news_json = news_text.get("hits")


popular_request = requests.get(popular)
popular_soup = str(BeautifulSoup(popular_request.text, "html.parser"))
popular_text = json.loads(popular_soup)
popular_json = popular_text.get("hits")

db = {}
new = []
popular = []


def input_popular():
    db['popular'] = popular


for idx, content in enumerate(popular_json):
    contents = {
        'title': content.get("title"),
        'url': content.get("url"),
        'points': content.get("points"),
        'author': content.get("author"),
        'num_comments': content.get("num_comments"),
        'obj_id': content.get("objectID")
    }
    popular.append(contents)
    if idx == len(popular_json)-1:
        input_popular()


def input_new():
    db['new'] = new


for idx, content in enumerate(news_json):
    contents = {
        'title': content.get("title"),
        'url': content.get("url"),
        'points': content.get("points"),
        'author': content.get("author"),
        'num_comments': content.get("num_comments"),
        'obj_id': content.get("objectID")
    }
    new.append(contents)
    if idx == len(news_json)-1:
        input_new()


@app.route("/")
def home():
    order_by = request.args.get("order_by")
    if order_by:
        order_by = order_by.lower()
        fromDb = db.get(order_by)
        if fromDb:
            result = fromDb
        else:
            if order_by == "popular":
                result = popular
            else:
                result = new
            db[order_by] = result
        print(db)
    else:
        return redirect("/?order_by=popular")

    return render_template("index.html", documents=result)


@app.route("/<id>")
def item(id):
    comments = []

    detail = f"{base_url}/items/{id}"
    detail_request = requests.get(detail)
    detail_soup = str(BeautifulSoup(detail_request.text, "html.parser"))
    detail_text = json.loads(detail_soup)

    data = {
        'title': detail_text.get("title"),
        'url': detail_text.get("url"),
        'points': detail_text.get("points"),
        'author': detail_text.get("author")
    }

    children = detail_text.get("children")

    for child in children:
        comment = {
            'author': child["author"],
            'text': child["text"]
        }

        comments.append(comment)
    return render_template("detail.html", data=data, comments=comments)


# 새로운 웹이 생성된다.
app.run(host="0.0.0.0")
