from flask import Flask, render_template, request
from textblob import TextBlob
from sentiment import   analyze

app=Flask(__name__)



@app.route('/',methods=["GET","POST"])

def index():
    sentiment=None
    if request.method == "POST":
        text=request.form["text"]
        sentiment=analyze(text)

    return render_template('index.html',sentiment=sentiment)
    

if __name__ ==  '__main__':
    app.run(debug=True)    



