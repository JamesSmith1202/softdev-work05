#James Smith / Ish Mahdi
import work03
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/"):
def root():
    return "Howdy! Come to our occupations page! <a href = ""127.0.0.1:5000/occupations""> ITS HERE </a>"

@app.route("/occupations")
def occupations():
    dicRandTuple = run("occupations.csv");
    occDic = 
    


if __name__ = "__main__":
    app.debug = true
    app.run()