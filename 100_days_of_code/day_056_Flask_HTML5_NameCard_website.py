from flask import Flask, render_template
# website located here
# https://sidorkinandrew.github.io/templates/index.html

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)

