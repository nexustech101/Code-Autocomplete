# src/config.py

MODEL_NAME = "Salesforce/codegen-350M-mono"  # Model trained for code generation
MAX_LENGTH = 50                              # Max length of the generated text
TEMPERATURE = 0.7                            # Controls creativity of the model
TOP_K = 50                                   # Limits tokens considered at each step
TOP_P = 0.95                                 # Controls nucleus sampling probability
