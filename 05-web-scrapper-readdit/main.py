"""
Send the 'headers' on my request.
How to use: requests.get(url, headers=headers)
"""

"""
Use this url to get top posts in per month :
https://www.reddit.com/r/{subreddit}/top/?t=month
"""

import requests
from bs4 import BeautifulSoup
from flask import Flask, render_template, request
from operator import itemgetter
app = Flask("DayEleven")
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'}

reddit_url = "https://www.reddit.com"

subreddits = [
    "javascript",
    "reactjs",
    "reactnative",
    "programming",
    "css",
    "golang",
    "flutter",
    "rust",
    "django"
]


@app.route("/")
def home():
    #home_url = request.url

    return render_template("home.html", subreddits=subreddits)


@app.route("/read")
def read():
    words = list(request.args.to_dict().keys())

    current_page_data = []
    for word in words:
        read_url = f"{reddit_url}/r/{word}/top/?t=month"
        read_request = requests.get(read_url, headers=headers)
        read_soup = BeautifulSoup(read_request.text, "html.parser")

        lists = read_soup.find_all("div", class_="_1poyrkZ7g36PawDueRza-J")
        for li in lists:
            link_row = li.find("a", {"class": "SQnoC3ObvgnGjWt90zD9Z"})
            title = li.find("h3", {"class": "_eYtD2XCVieq6emjKBH3m"})
            upvote = li.find(
                "div", class_="_1rZYMD_4xY3gRcSS3p8ODO _25IkBM0rRUqWX5ZojEMAFQ")
            if link_row and title and upvote:
                link = link_row['href']
                try:
                    contents = {
                        'word': word,
                        'reddit': f"{reddit_url}{link}",
                        'title': title.text,
                        'upvote': int(upvote.text)
                    }
                    current_page_data.append(contents)
                except:
                    pass

    current_page_data = sorted(
        current_page_data, key=itemgetter("upvote"))[::-1]

    return render_template("read.html", words=words, current_page_data=current_page_data)


app.run(host="0.0.0.0")
