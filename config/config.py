import yaml
from transformers import TrainingArguments

class ConfigManger:
    def __init__(self, confing_path="config.yaml"):
        with open(confing_path, "r") as f:
            self.config = yaml.safe_load(f)
    
    
    def get_raw_data_path(self):
        raw_data_path = self.config["data"]["raw_dataset"]
        raw_data = r"{}".format(raw_data_path)
        return raw_data
    

    def get_preprocessed_data_path(self):
        processed_data_path = self.config["data"]["preprocessed_dataset"]
        processed_data = r"{}".format(processed_data_path)
        return processed_data
    

    def get_base_model_name(self):
        base_model_name = self.config["models"]["base_model"]
        return base_model_name


    def get_fine_tuned_model_path(self):
        fine_tuned_model_path = self.config["models"]["fine_tuned_model"]
        fine_tuned_model = r"{}".format(fine_tuned_model_path)
        return fine_tuned_model
    

    def get_training_args(self):
        training_args = self.config["training_args"]
        return training_args



