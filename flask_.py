from flask import Flask

app=Flask(__name__)

@app.route('/')
def hi():
    return "salom"


@app.route("/jamshid")

def i():
    return "i am student"


app.run(debug=True)