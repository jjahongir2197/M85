from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        name = request.form["name"]
        age = request.form["age"]
        return render_template("result1.html", name=name, age=age)

    return render_template("index1.html")

if __name__ == "__main__":
    app.run(debug=True)
