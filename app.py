from flask import render_template, flash, Flask, request
from get_data import get_data
from parse_url import parse_url

app = Flask(__name__)
app.config["DEBUG"] = True


@app.route("/")
def about():
    return render_template("about.html")


@app.route("/home", methods=["POST", "GET"])
def home():
    ha = None
    if request.method == "POST":
        url = request.form.get("search")
        limit = int(request.form.get("limit"))
        urlParsed = parse_url(url)
        if urlParsed == -1:
            ha = {"errors": "Not a valid amazon product url."}
        else:
            ha = get_data(urlParsed, limit)

    return render_template("index.html", text=ha)


app.run()
