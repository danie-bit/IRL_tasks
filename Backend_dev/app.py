from flask import Flask, render_template, request
import re

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    highlighted = ""
    matches = []
    error = None
    text = ""

    if request.method == "POST":
        text = request.form.get("test_string")
        regex = request.form.get("regex")

        try:
            pattern = re.compile(regex)
            last = 0

            for m in pattern.finditer(text):
                start, end = m.span()
                highlighted += text[last:start]
                highlighted += f"<mark>{text[start:end]}</mark>"
                matches.append(text[start:end])
                last = end

            highlighted += text[last:]

        except re.error as e:
            error = str(e)

    return render_template("index.html",
                           highlighted=highlighted,
                           matches=matches,
                           error=error,
                           text=text)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
