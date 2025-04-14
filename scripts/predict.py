from transformers import pipeline, AutoModelForSequenceClassification, AutoTokenizer
import sys, os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from config.config import ConfigManger
config = ConfigManger()

model = AutoModelForSequenceClassification.from_pretrained(config.get_fine_tuned_model_path())
tokenizer = AutoTokenizer.from_pretrained(config.get_base_model_name())

classifier = pipeline("sentiment-analysis", model=model, tokenizer=tokenizer)
 
