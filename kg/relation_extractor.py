from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

class RelationExtractor:
    def __init__(self, model_name="dmis-lab/biobert-v1.1"):
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForSequenceClassification.from_pretrained(model_name)
        self.label_map = {0: "treats", 1: "causes", 2: "associated_with"}

    def extract_relation(self, sentence: str, e1: str, e2: str) -> str:
        # For demo, return dummy; replace with real inference in production
        return "treats"