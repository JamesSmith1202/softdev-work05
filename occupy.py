#James Smith / Ish Mahdi

from flask import Flask, render_template
from utils import work03
app = Flask(__name__)

@app.route("/")
def root():
    return render_template("home.html")

@app.route("/occupations")
def occupations():
    dicRandTuple = work03.run("data/occupations.csv");
    return render_template("job.html", occDic = dicRandTuple[0], randomOcc = dicRandTuple[1])

if __name__ == "__main__":
    app.debug = True
    app.run()
