from bs4 import BeautifulSoup
import requests
import os
import functions
from flask import Flask, render_template, url_for, request


app = Flask(__name__)


@app.route("/")
def main():
    return render_template("index.html")


@app.route("/search", methods=["POST"])
def search():
    url = request.form["url"]
    result = scraper(url, "test")
    return render_template("index.html", result=result)


def scraper(url, dir):
    arr = []
    functions.create_directory(dir)
    result = requests.get(url)
    result_text = result.text
    soup = BeautifulSoup(result_text, "html.parser")

    divs = soup.find_all("div")
    a_tags = soup.find_all("a")
    img_tags = soup.find_all("img")
    h2_tags = soup.find_all("h2")
    p_tags = soup.find_all("p")

    for div in divs:
        div_text = div.text
        obj = {"div_text": div_text}
        arr.append(obj)

    for a_tag in a_tags:
        a_href = a_tag.get("href")
        obj = {"a_href": a_href}
        arr.append(obj)

    for img_tag in img_tags:
        img = img_tag.get("src")
        obj = {"img_src": img}
        arr.append(obj)

    for h2_tag in h2_tags:
        h2_text = h2_tag.text
        obj = {"h2_text": h2_text}
        arr.append(obj)

    for p_tag in p_tags:
        p_text = p_tag.text
        obj = {"p_text": p_text}
        arr.append(obj)

    return arr


if __name__ == '__main__':
    app.run(debug=True)
