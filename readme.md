 ## COVID-19 Vaccination Sentiment Analysis and Deployment as a Gradio Web App on Huggingface
 
 ### Introduction
 
The creation of COVID-19 vaccinations was a key milestone in public health, suggesting a solution to restrict the virus’s

transmission and save lives. However, the ‘anti-vaxxer’ movement has emerged in some regions, leading to lower vaccination

rates and potential outbreaks of preventable diseases. To help solve this issue, I created a gradio web app by fine-tuning 

some huggingface text classification models. The 3 test classification models I fine-tuned were Twitter_roBETRa_base, 

distilbert-base-uncased and BERT-base-uncased. These models can assess public sentiment toward vaccination by categorizing 

Twitter messages as favorable, neutral, or negative. Governments and public health players can better understand the 

prevailing attitudes by monitoring sentiment and tailoring communication methods and immunization programs accordingly.



# Summary
| Code      | Name        | Published Article |  Deployed App |
|-----------|-------------|:-------------:|------:|
| P5|The Sentiment Analysis Project| [Article]https://medium.com/@otchie.sonny/covid-19-vaccination-sentiment-analysis-and-deployment-as-a-gradio-web-app-on-huggingface-ef01c8ff851d| [Deployed App](https://huggingface.co/spaces/Sonny4Sonnix/Covid_tweets_sentimental_analysis_app) |

Gradio_App

Building Machine Learning Applications on huggingface With Gradio ✨

## 📚 Description

Welcome to Building Machine Learning Applications With Gradio! 

This project is designed embed a machine learning file into an app for users.

It's uses a previously pre-trained hugging text classification model(Twitter-roBERTa-case).

## 📖 Table of Contents

Installation

Usage

Authors

Acknowledgement

contact

## 🔧 Installation

To get started , follow these installation steps:

# setup the environment on windows by running the following code.

Make sure you have Python installed on your system.

Clone this repository to your local machine.


git clone <repository-url>
Navigate to the project directory.


cd <project-directory>
Set up a virtual environment (optional but recommended).


python -m venv myenv
Activate the virtual environment.

On Windows:


myenv\Scripts\activate
On macOS and Linux:


source myenv/bin/activate
Install the required packages.


pip install -r requirements.txt
The Two commands are of the same structure 

1.Activate the python environment 

2.Upgrade pip to it current version 

3.install the requirements located in requirements.txt: You should be at the root of your env

## 🚀 Usage

### To see how the app works, follow these instructions: 

1.After setting up enviroment,activatig the environment, and installing requirments, type

gradio run <python_script> #in the terminal

This will open the App in your browser

## 👥 Authors
This project is developed and maintained by:

Sonny Agorvor -Otchie feel free to reach out to me with any questions or feedback!

## ✨ Acknowledgments

I would like to express my gratitude to The Azubi Africa team for their valuable contributions to this project.

## 📞 Contact
For any questions, concerns, or suggestions regarding this project, please contact us at otchie.sonny@gmail.com.



Install the required packages to be able to run the evaluation locally.

You need to have Python3 on your system. Then you can clone this repo and being at the repo's root (root :: repo_name> ...) follow the steps below:

Windows:

  python -m venv venv; venv\Scripts\activate; python -m pip install -q --upgrade pip; python -m pip install -qr requirements.txt  
Linux & MacOs:

  python3 -m venv venv; source venv/bin/activate; python -m pip install -q --upgrade pip; python -m pip install -qr requirements.txt  
The both long command-lines have a same structure, they pipe multiple commands using the symbol ; but you may manually execute them one after another.

Create the Python's virtual environment that isolates the required libraries of the project to avoid conflicts;

Activate the Python's virtual environment so that the Python kernel & libraries will be those of the isolated environment;

Upgrade Pip, the installed libraries/packages manager to have the up-to-date version that will work correctly;

Install the required libraries/packages listed in the requirements.txt file so that it will be allow to import them into the 

python's scripts and notebooks without any issue.

NB: For MacOs users, please install Xcode if you have an issue.

##Resources

### Quick intro to NLP

[Getting Started With Hugging Face in 15 Minutes>](https://www.youtube.com/watch?v=CMrHM8a3hqw)

[Fine-tuning a Neural Network explained](https://www.youtube.com/watch?v=QEaBAZQCtwE)

Fine-Tuning-DistilBert - Hugging Face Transformer for Poem Sentiment Prediction | NLP(https://www.youtube.com/watch?v=5T-iXNNiwIs)https://www.youtube.com/watch?v=5T-iXNNiwIs

[Introduction to NLP: Playlist](https://www.youtube.com/watch?v=zcW2HouIIQg)

[](https://www.youtube.com/watch?v=zcW2HouIIQg)

[](https://www.youtube.com/playlist?list=PLM8wYQRetTxCCURc1zaoxo9pTsoov3ipY)
