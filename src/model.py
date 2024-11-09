# src/model.py

from transformers import AutoTokenizer, AutoModelForCausalLM
import torch
from .config import MODEL_NAME


class CodeCompletionModel:
    def __init__(self):
        # Load the model and tokenizer
        self.tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
        self.model = AutoModelForCausalLM.from_pretrained(MODEL_NAME)
        self.model.eval()  # Set model to evaluation mode

        # Check for CUDA availability and move the model to GPU if available
        if torch.cuda.is_available():
            self.model = self.model.to("cuda") or self.model.to("cpu")  # Check if GPU is available

    def get_tokenizer(self):
        return self.tokenizer

    def get_model(self):
        return self.model
