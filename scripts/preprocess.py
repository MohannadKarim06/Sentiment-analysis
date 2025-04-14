import pandas as pd
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from transformers import AutoTokenizer
from datasets import Dataset
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from config.config import ConfigManger

config = ConfigManger()

tokenizer = AutoTokenizer.from_pretrained(config.get_base_model_name())

def download_files():  
    nltk.download("stopwords")
    nltk.download("wordnet")
stop_words = set(stopwords.words("english"))
lemmatizer = WordNetLemmatizer()

def preprocess_text(text):
    text = text.lower()
    text = ' '.join([word for word in text.split() if word not in stop_words])
    text = ' '.join([lemmatizer.lemmatize(word) for word in text.split()])
    return text

def preprocessing(df):
    df['review'] = df['review'].apply(preprocess_text)  
    df['sentiment'] = df['sentiment'].map({'positive': 1, 'negative': 0})
    return df

def tokenize_dataset(df):

    def tokenize_function(df):
            return tokenizer(df['review'], padding="max_length", truncation=True, return_tensors='pt')  

    df = Dataset.from_pandas(df).map(tokenize_function, batched=True)
    df = df.rename_column("sentiment", "labels")
    return df

def split_save_dataset(df):
    train_testvalid_dataset = df.train_test_split(test_size=0.2, seed=42)
    temp_dataset = train_testvalid_dataset['train'].train_test_split(test_size=0.1, seed=42)
    train_testvalid_dataset['validation'] = temp_dataset['test']
    train_testvalid_dataset['train'] = temp_dataset['train']
    train_testvalid_dataset.save_to_disk(config.get_preprocessed_data_path())
    print('Data saved!')


def preprocessing_dataset():
    df = pd.read_csv(config.get_raw_data_path())
    download_files()
    preprocessed_df = preprocessing(df)
    tokenized_dataset = tokenize_dataset(preprocessed_df)
    split_save_dataset(tokenized_dataset)
    return preprocessed_df

