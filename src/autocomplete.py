# src/autocomplete.py

import torch
from .model import CodeCompletionModel
from .config import MAX_LENGTH, TEMPERATURE, TOP_K, TOP_P


class CodeAutocomplete:
    def __init__(self):
        self.completion_model = CodeCompletionModel()
        self.tokenizer = self.completion_model.get_tokenizer()
        self.model = self.completion_model.get_model()

    def complete_code(self, prompt):
        # Tokenize the input prompt
        inputs = self.tokenizer(prompt, return_tensors="pt")

        # Move input tensors to GPU if available
        if torch.cuda.is_available():
            inputs = {key: value.to("cuda") for key, value in inputs.items()}

        # Generate code completions
        with torch.no_grad():
            outputs = self.model.generate(
                inputs["input_ids"],
                max_length=len(inputs["input_ids"][0]) + MAX_LENGTH,
                temperature=TEMPERATURE,
                top_k=TOP_K,
                top_p=TOP_P,
                do_sample=True
            )

        # Decode the output and format it
        completion = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
        return completion
