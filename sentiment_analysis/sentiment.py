from textblob import TextBlob

def analyze(text):
    blob=TextBlob(text)
    sentiment=blob.sentiment
    polarity=sentiment.polarity  #-1 to +1.. -1 negative and +1 means positive sentiment
   
    if polarity >0:
        category="Positive"
    elif polarity<0:
        category="Negative"
    else:
        category="Neutral"

    return category

'''text=input("enter Text::")
result=analyze(text)
print(f"Sentiment ranked as :::{result} ")'''