from flask import Flask, render_template
import requests
import os
from dotenv import load_dotenv

load_dotenv()

BLOG_ENDPOINT = os.environ.get("BLOG_ENDPOINT")
posts = requests.get(BLOG_ENDPOINT).json()

app = Flask(__name__)


@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=posts)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route('/posts/<int:num>')
def get_posts(num):
    return render_template('post.html', all_posts=posts, id=num)


if __name__ == "__main__":
    app.run(debug=True)
