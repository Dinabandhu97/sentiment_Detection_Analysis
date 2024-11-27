from flask import Flask, render_template, request
from textblob import TextBlob

app = Flask(__name__)
def analysis_sentiment(text):
    blob= TextBlob(text)

    sentiment = blob.sentiment
    polarity = sentiment.polarity

    if polarity > 0:
        sentiment_category = "Positive"
    elif polarity < 0:
        sentiment_category = "Negative"
    else:
        sentiment_category = "Neutral"
    
    return sentiment_category

@app.route('/', methods=['GET','POST'])
def index():
    sentiment = None

    if request.method == 'POST':
        text = request.form['text']
        sentiment = analysis_sentiment(text)

        return render_template('index.html', sentiment=sentiment)

if __name__ == '_main_':
  app.run(debug=True)
