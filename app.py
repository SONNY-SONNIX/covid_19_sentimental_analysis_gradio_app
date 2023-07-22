import gradio as gr 
import transformers as pipeline 
from transformers import AutoTokenizer,AutoModelForSequenceClassification
from transformers import AutoModelForSequenceClassification, AutoTokenizer, pipeline

model_name = "Sonny4Sonnix/twitter-roberta-base-sentimental-analysis-of-covid-tweets"  # Replace with the name of the pre-trained model you want to use
model = AutoModelForSequenceClassification.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

sentiment = pipeline("sentiment-analysis", model=model, tokenizer=tokenizer)

def get_sentiment(input_text):
    return sentiment(input_text)



#Function to predict sentiments from the input text using the model
    prediction = model.predict([text])[0]
    if label==-1:
       return "Negative"
    elif label== 0:
        return "Neutral"
    else:
        return "Positive"

iface = gr.Interface(fn=get_sentiment,title="Sentimental Analysis", inputs="text",outputs="text")
iface.launch(inline=True)
# import pandas as pd 
# import gradio as gr
# import numpy as np
# import nltk
# import joblib
# import transformers
# from transformers import RobertaForSequenceClassification
# from transformers import AutoTokenizer
# from transformers import pipeline 
# from transformers import utils
# import torch 



# Disabe W&B
#os.environ["WANDB_DISABLED"] = "true"
#Load the model
# model = joblib.load("models/sentiment_analysis_model.joblib")

#Function to predict sentiments from the input text using the model
# def predict_sentiment(text):
#     prediction = model.predict([text])[0]
#     if prediction==0:
#         return "Negative"
#     elif prediction == 1:
#         return "Neutral"
#     else:
#         return "Positive"


# Create the Gradio app interface
# demo = gr.Interface(fn=predict_sentiment, input=gr.inputs.Textbox(),outputs="text")
# demo.launch()

#demo = gr.Interface(fn= ,input=gr.inputs.Textbox(),outputs="text")
#demo.launch()

