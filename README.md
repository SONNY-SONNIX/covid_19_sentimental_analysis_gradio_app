---
title: Covid Tweets Sentimental Analysis App
emoji: 🐠
colorFrom: yellow
colorTo: green
sdk: gradio
sdk_version: 3.38.0
app_file: app.py
pinned: false
---

Check out the configuration reference at https://huggingface.co/docs/hub/spaces-config-reference

# Sentiment Analysis with Twitter RoBERTa

This code demonstrates a Sentiment Analysis application using the Twitter RoBERTa model.
The model predicts whether a given text is positive, negative, or neutral in sentiment.

# Setup and Dependencies

To run the code, ensure you have the required dependencies installed:

gradio: A web-based interface for interactive machine learning model deployment.

transformers: A library for state-of-the-art Natural Language Processing models.

torch :
You can install the necessary packages using pip:

bash
Copy code

pip install gradio transformers

Model Initialization

The code uses the "twitter-roberta-base-sentimental-analysis-of-covid-tweets" pre-trained model from the Hugging Face model hub. The model is loaded and initialized for sentiment analysis:

python
Copy code

model_name = "Sonny4Sonnix/twitter-roberta-base-sentimental-analysis-of-covid-tweets"
model = AutoModelForSequenceClassification.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)
sentiment = pipeline("sentiment-analysis", model=model, tokenizer=tokenizer)
Sentiment Prediction
The get_sentiment function uses the loaded model to predict the sentiment of the input text:

python

Copy code

def get_sentiment(input_text):
    prediction = sentiment(input_text)
    label = prediction[0]['label']
    if label == 'LABEL_0':
        return "Negative"
    elif label == 'LABEL_1':
        return "Neutral"
    else:
        return "Positive"
Gradio Interface

The code creates a web-based interface using Gradio to interact with the sentiment analysis model. Users can input a text, and the model will predict its sentiment in real-time:

python

Copy code

iface = gr.Interface(fn=get_sentiment, title="Sentiment Analysis", inputs="text", outputs="text")
iface.launch(inline=True)
Usage
To use the Sentiment Analysis application, run the script, and a web page will open with an input field. Enter your text, and the model will predict the sentiment. The result will be displayed on the web page.

Please make sure to have an internet connection to download the model if you haven't previously downloaded it.

Note: The model's prediction might not be perfect and may vary based on the input text.

DONE.
