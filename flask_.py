from flask import Flask

app=Flask(__name__)

@app.route('/')
def hi():
    return "salom"

jamshid_page="""<!DOCTYPE html>
<html>
<body>

<h1>This is heading 1</h1>

<h3>This is heading 3</h3>


<h6>This is heading 6</h6>

<p><b>Tip:</b> Use h1 to h6 elements only for headings. Do not use them just to make text bold or big. Use other tags for that.</p>

</body>
</html>
"""

@app.route("/jamshid")
@app.route("/student")
def i():
    return jamshid_page


app.run(debug=True)