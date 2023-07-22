pip install transformers 

import pandas as pd 
import gradio as gr
import numpy as np
import nltk
import joblib
import transformers
from transformers import RobertaForSequenceClassification
from transformers import AutoTokenizer
from transformers import pipeline 
from transformers import utils
import torch 


#Load the model
model = joblib.load("models/sentiment_analysis_model.joblib")

#Function to predict sentiments from the input text using the model
def predict_sentiment(text):
    prediction = model.predict([text])[0]
    if prediction==0:
        return "Negative"
    elif prediction == 1:
        return "Neutral"
    else:
        return "Positive"


# Create the Gradio app interface
demo = gr.Interface(fn=predict_sentiment, input=gr.inputs.Textbox(),outputs="text")
demo.launch()