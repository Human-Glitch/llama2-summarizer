# Llama2 Summarizer

Llama2 Summarizer is a Python-based application that utilizes Meta's Llama 2 Large Language Model (LLM) to generate concise summaries from input text. This tool assists users in quickly understanding large volumes of text by providing coherent and context-aware summaries. The model was fine tuned from the classic samsum.jsonl data set.

## Features

- **Text Summarization**: Generates concise summaries from input text using the Llama 2 model.
- **Command-Line Interface**: Provides a simple CLI for easy interaction.
- **Extensible**: Designed to allow integration with other applications or workflows.

## Prerequisites

- **Python 3.8 or higher**: Ensure Python is installed on your system.
- **Poetry**: A tool for dependency management and packaging in Python. Install it from the [official website](https://python-poetry.org/docs/#installation).

## Installation

1. **Clone the Repository**:

   \```
   git clone https://github.com/Human-Glitch/llama2-summarizer.git
   cd llama2-summarizer
   \```

2. **Install Dependencies**:

   \```
   poetry install
   \```

   This command will create a virtual environment and install all necessary dependencies as specified in the `pyproject.toml` file.

3. **Configure Environment Variables**:

   Create a `.env` file in the project root and add your configuration settings as needed.

## Usage

1. **Run the Summarizer**:

   ```bash
   poetry run python main.py --input your_input_file.txt --output summary_output.txt
   ```

   Replace `your_input_file.txt` with the path to your input text file, and `summary_output.txt` with the desired path for the output summary.

2. **Command-Line Options**:

   - `--input`: Path to the input text file.
   - `--output`: Path to save the generated summary.
   - `--model`: (Optional) Specify a different model if available.

## License

This project is licensed under the Apache License 2.0. See the [LICENSE](https://github.com/Human-Glitch/llama2-summarizer/blob/main/LICENSE) file for details.

## Acknowledgments

- **Meta AI**: For developing the Llama 2 model.

---
