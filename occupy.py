#James Smith / Ish Mahdi
import work03
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def root():
    return "Howdy! Come to our occupations page! <a href = ""http://127.0.0.1:5000/occupations""> ITS HERE </a>"

@app.route("/occupations")
def occupations():
    dicRandTuple = work03.run("occupations.csv");
    return render_template("job.html", occDic = dicRandTuple[0], randomOcc = dicRandTuple[1])

if __name__ == "__main__":
    app.debug = True
    app.run()
