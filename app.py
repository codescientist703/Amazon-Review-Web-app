from flask import render_template, flash, Flask, request
from get_data import get_data

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
        ha = get_data(url, limit)
        print(ha)
    return render_template("index.html", text=ha)


app.run()
