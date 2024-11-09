# Code Autocomplete Project

This project is a Python-based code autocompletion tool that uses a GPT-based transformer model from the Hugging Face library. The tool generates code suggestions based on partial code input, making it useful for enhancing programming efficiency.

## Features
- Utilizes pre-trained GPT models, such as `Salesforce/codegen-350M-mono`, optimized for code generation.
- Generates natural and contextually relevant code completions.
- Modular design with separate configuration and model loading for easy customization.

## Project Structure

```
code_autocomplete/
│
├── src/
│   ├── __init__.py
│   ├── autocomplete.py         # Contains the main code autocompletion logic
│   ├── model.py                # Handles model loading and configuration
│   └── config.py               # Configuration settings for the model and parameters
│
├── main.py                     # Main script to run the autocompletion with a sample prompt
├── requirements.txt            # Project dependencies
└── README.md                   # Documentation
```

### File Descriptions

- **`src/config.py`**: Stores configuration settings like model name and generation parameters.
- **`src/model.py`**: Contains the `CodeCompletionModel` class that loads and initializes the GPT model and tokenizer.
- **`src/autocomplete.py`**: Contains the `CodeAutocomplete` class, which uses `CodeCompletionModel` to handle autocompletion logic.
- **`main.py`**: Main entry point to run a sample code completion.
- **`requirements.txt`**: Lists required dependencies for easy installation.

## Setup

### Prerequisites
Make sure you have Python 3.8+ installed.

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/code_autocomplete_project.git
   cd code_autocomplete_project
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Running the Project

To generate a code completion from a sample prompt, run:

```bash
python main.py
```

This will output a code suggestion based on a partial code snippet defined in `main.py`.

### Example Output

For the input prompt:
```python
def factorial(n):
    if n == 0:
        return 1
    else:
        return
```

The output might be:
```python
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
```

## Configuration

You can adjust parameters in `src/config.py` to fine-tune the completion behavior:

- `MODEL_NAME`: Specifies the model to use. For example, `"Salesforce/codegen-350M-mono"` for code-specific generation.
- `MAX_LENGTH`: Maximum length of generated code.
- `TEMPERATURE`: Controls creativity in code suggestions. Lower values make output more deterministic.
- `TOP_K` and `TOP_P`: Control sampling diversity, limiting output to the most probable tokens (`top_k`) and cumulative probability (`top_p`).

## Customizing the Model

To use a different pre-trained model, modify the `MODEL_NAME` in `src/config.py` to any other model from the Hugging Face Model Hub (e.g., `"gpt-2"`). Ensure the chosen model is suitable for code if you need precise code suggestions.

## Adding a Custom Prompt

You can modify `prompt` in `main.py` to test different prompts. This tool can autocomplete various programming languages if the model is sufficiently trained on those languages.

## License

This project is licensed under the MIT License. See `LICENSE` for more details.

## Acknowledgments

- [Hugging Face Transformers](https://huggingface.co/transformers/) for the pre-trained models and tokenizer tools.
- [OpenAI](https://openai.com/) for pioneering GPT models.
