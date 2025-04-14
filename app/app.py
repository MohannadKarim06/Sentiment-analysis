from transformers import AutoTokenizer, AutoModelForSequenceClassification, pipeline, AutoConfig
import streamlit as st
import os, sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from scripts.predict import classifier
import plotly.express as px
from wordcloud import WordCloud
from collections import Counter
import matplotlib.pyplot as plt
import nltk
from nltk.corpus import stopwords

from scripts.logging import logger

stop_words = set(stopwords.words('english'))


def analyze_sentiment(text):
  result = classifier(text)[0]
  if result['label'] == 'LABEL_1':
    sentiment = "Positive"
  else:
    sentiment = "Negative"
  score = result['score']
  return sentiment, score


def visualize_sentiment_distribution(text):
     words = text.lower().split()

     sentiment_scores = [classifier(word)[0]['score'] for word in words if word not in stop_words]  

     plt.figure(figsize=(8, 6))
     plt.hist(sentiment_scores, bins=10, color='skyblue', edgecolor='black')
     plt.title('Sentiment Distribution')
     plt.xlabel('Sentiment Score')
     plt.ylabel('Frequency')
     st.pyplot(plt)  




# Streamlit app
def main():
    st.title("Sentiment Analysis App")
    text_input = st.text_area("Enter text for sentiment analysis")
    labels = []

    if st.button("Analyze"):
        if text_input.isdigit():  # Check if the input consists only of digits
            st.error("Please enter text, not numbers.")
        elif text_input.isalnum() and text_input.isdigit() : # Check if alphanumeric and only numbers
            st.error("Please enter text, not numbers.")
        else:  
          
          if text_input:
            try:
              sentiment, score = analyze_sentiment(text_input)
            except Exception as e:
              st.error("An unexpected error occurred. Please try again later.")
              logger.exception(e)
            except ValueError:
              st.error("Invalid input format. Please make sure your text is valid.")
            else:
              logger.info(f"User entered some text: '{text_input}'")
              st.write(f"Sentiment: {sentiment}")

              st.progress(score)
              st.write(f"Confidence: {score:.2f}")

              if sentiment == 'Positive':

                labels = ['Positive', 'Negative' ]
                values = [score, 1 - score]
              else:
                labels = ['Positive', 'Negative' ]
                values = [1 - score, score]

              fig = px.pie(values=values, names=labels, title="Sentiment Prediction")
              st.plotly_chart(fig)
            try: 
              visualize_sentiment_distribution(text_input)
            except ValueError:
              st.error("Invalid input format. Please make sure your text is valid.")
            except Exception as e:
              st.error("An unexpected error occurred. Please try again later.")
              logger.exception(e)
          else:
              st.write("Please enter some text")

if __name__ == "__main__":
    main()


