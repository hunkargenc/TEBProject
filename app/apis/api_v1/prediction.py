from __future__ import annotations

from .utils import get_data, get_model

# TODO - add error handling
# TODO - add async
# TODO - add cache (maybe REDIS)
def prediction(errors):
    # Get json data
    data = get_data(errors)
    # Define a list of customer messages to classify
    customer_messages = [message.get("message") for message in data if message["speaker"] == "customer"]
    
    # Load the BART model and tokenizer
    bart_model = get_model()

    sentiments = sentiment_prediction(customer_messages, bart_model, errors)
    intentions = intention_prediction(customer_messages, bart_model, errors)

    return sentiments, intentions

def sentiment_prediction(customer_messages, bart_model, errors):
    sentiments = []
    
    # Define labels for sentiment
    sentiment_labels = ["positive", "negative", "neutral"]
    
    # Perform sentiment classification for each customer message
    for text in customer_messages:
        result = bart_model(text, sentiment_labels)
        predicted_sentiment = result['labels'][0]
        score = result['scores'][0]
        sentiments.append({"message": text, "sentiment": predicted_sentiment, "score": score})

    return sentiments


def intention_prediction(customer_messages, bart_model, errors):
    intentions = []

    # Define labels for intention
    intention_labels = [
        "greeting", 
        "inquiry", 
        "information", 
        "confirmation", 
        "gratitude",
        "closing",
        "follow-up",
        "acknowledgment",
        "praise"
        ]
    # Perform sentiment classification for each customer message
    for text in customer_messages:
        result = bart_model(text, intention_labels)
        predicted_intention = result['labels'][0]
        score = result['scores'][0]
        intentions.append({"message": text, "intention": predicted_intention, "score": score})

    return intentions
