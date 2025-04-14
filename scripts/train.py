from transformers import TrainingArguments, Trainer, AutoModelForSequenceClassification
from datasets import load_from_disk

import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from config.config import ConfigManger

config = ConfigManger()

training_args_dict = config.get_training_args()
training_args = TrainingArguments(**training_args_dict)

model = AutoModelForSequenceClassification.from_pretrained(config.get_base_model_name(), num_labels=2)

train_testvalid_dataset = load_from_disk(config.get_preprocessed_data_path())

train_dataset = train_testvalid_dataset['train']
validation_dataset = train_testvalid_dataset['validation']


trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=train_dataset,
    eval_dataset=validation_dataset,
)



def train_model():
    trainer.train()
    trainer.save_model(config.get_fine_tuned_model_path())
    

