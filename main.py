# main.py

from src.autocomplete import CodeAutocomplete


def main():
    autocomplete_tool = CodeAutocomplete()

    # Sample prompt for code completion
    prompt = "def factorial(n):\n    if n == 0:\n        return 1\n    else:\n        return"

    # Get the completion
    completion = autocomplete_tool.complete_code(prompt)
    print("Code Completion:\n")
    print(completion)


if __name__ == "__main__":
    main()
