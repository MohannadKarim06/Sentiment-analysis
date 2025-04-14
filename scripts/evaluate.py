from transformers import AutoModelForSequenceClassification, Trainer
from datasets import load_from_disk
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from config.config import ConfigManger

config = ConfigManger()

train_testvalid = load_from_disk(config.get_preprocessed_data_path())

fine_tuned_model = AutoModelForSequenceClassification.from_pretrained(config.get_fine_tuned_model_path())

test_data = train_testvalid['test']

trainer = Trainer(
    model=fine_tuned_model
)

def evaluate_model():
    predictions = trainer.predict(test_data)
    predicted_labels = predictions.predictions.argmax(-1)
    true_labels = predictions.label_ids
    accuracy = accuracy_score(true_labels, predicted_labels)
    precision = precision_score(true_labels, predicted_labels)
    recall = recall_score(true_labels, predicted_labels)
    f1 = f1_score(true_labels, predicted_labels)
    print(f"Accuracy: {accuracy}")
    print(f"Precision: {precision}")
    print(f"Recall: {recall}")
    print(f"F1 Score: {f1}")
