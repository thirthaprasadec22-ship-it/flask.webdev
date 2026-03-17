from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():

    if request.method == "POST":
        note = request.form["note"]

        with open("notes.txt", "a") as file:
            file.write(note + "\n")

    notes = []

    try:
        with open("notes.txt", "r") as file:
            notes = file.readlines()
    except:
        pass

    return render_template("index.html", notes=notes)

if __name__ == "__main__":
    app.run(debug=True)