from flask import Flask, redirect, render_template, request, url_for

import os
import sys
import helpers
from analyzer import Analyzer

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/search")
def search():

    # validate screen_name
    screen_name = request.args.get("screen_name", "")
    if not screen_name:
        return redirect(url_for("index"))

    # get screen_name's tweets
    tweets = helpers.get_user_timeline(screen_name, count=5)
    if tweets == None:
        return redirect(url_for("index"))

    positives = os.path.join(sys.path[0], "positive-words.txt")
    negatives = os.path.join(sys.path[0], "negative-words.txt")
    analyzer = Analyzer(positives, negatives)

    positive_post, negative_post, neutral_post = 0, 0, 0

    for post in tweets:
        score = analyzer.analyze(post)
        if score > 0:
            positive_post += 1
        elif score < 0:
            negative_post += 1
        else:
            neutral_post += 1

    sum = positive_post + negative_post + neutral_post

    positive, negative, neutral = positive_post / sum, negative_post / sum, neutral_post / sum

    # generate chart
    chart = helpers.chart(positive, negative, neutral)

    # render results
    return render_template("search.html", chart=chart, screen_name=screen_name)
