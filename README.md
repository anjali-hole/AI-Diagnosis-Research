# AI Research Repository
This repository contains all relevant files and scripts used for the AI-Assisted Diagnosis project titled "Evaluating LLMs for AI-Assisted Preliminary Medical Diagnosis: Accuracy, Risks, and Telehealth Integration". This project focuses on assessing the accuracy, safety, and potential integration of various large language models (LLMs) like Claude, Gemini, and OpenAI into telehealth platforms for preliminary medical diagnoses.

## Table of Contents

- [Introduction](#-introduction)
- [Project Structure](#-project-structure)
- [Requirements](#-requirements)
- [Installation](#-installation)
- [Usage](#-usage)
- [Querying Models](#-querying-models)
- [Analysis](#-analysis)
- [Data Files Explanation](#-data-files-explanation)
- [Contribution](#-contribution)
- [License](#-license)


## Introduction

The purpose of this project is to evaluate the performance of several state-of-the-art LLMs in providing preliminary medical diagnoses based on case descriptions. The evaluation is done by comparing their responses against professional medical assessments, conducting risk analysis, and proposing strategies for safe integration into telehealth platforms.

## Project Structure

```.
├── README.md                  # Project documentation
├── all_data_with_analysis.xlsx # Consolidated analysis file
├── claude_diagnostic_query.py  # Python script for querying Claude API
├── gemini_diagnostic_query.py  # Python script for querying Gemini API
├── openai_diagnostic_query.py  # Python script for querying OpenAI API
├── llm_responses_claude.csv    # CSV file storing Claude model responses
├── llm_responses_gemini.csv    # CSV file storing Gemini model responses
├── llm_responses_openai.csv    # CSV file storing OpenAI model responses
├── patient_cases.csv           # Dataset of medical cases used for evaluation
```
## Requirements

To run the code files, the following libraries are required:

```pandas```

```numpy```

```openai```

```requests```

Install them via:

```pip install pandas numpy openai requests```

## Installation

Clone the repository:

```git clone https://github.com/anjali-hole/ai-research.git```

Navigate to the project directory:

```cd AI-Diagnosis-Research```

Install the required libraries:

```pip install -r requirements.txt```

## Usage

The scripts are organized to allow querying of various LLMs and saving their responses. 

Make sure to create a .env file in the root directory of the project to store your API keys. The file should have the following format:

```
OPENAI_API_KEY=your_openai_key
CLAUDE_API_KEY=your_claude_key
GEMINI_API_KEY=your_gemini_key
```

Replace your_openai_key, your_claude_key, and your_gemini_key with your actual API keys.

## Querying Models

Claude Model:

```python claude_diagnostic_query.py```

Gemini Model:

```python gemini_diagnostic_query.py```

OpenAI Model:

```python openai_diagnostic_query.py```

## Analysis

All model responses are saved in respective CSV files (llm_responses_claude.csv, llm_responses_gemini.csv, llm_responses_openai.csv) for further analysis. Consolidated analysis is stored in all_data_with_analysis.xlsx.

## 📂 Data Files Explanation

```patient_cases.csv```: Contains the set of medical cases with descriptions, symptoms, and expected diagnoses for comparison.

```llm_responses_*.csv```: Files containing responses from the respective LLMs.

```all_data_with_analysis.xlsx```: Consolidated analysis of all models' performance, with statistical metrics and comparison tables.

## Contribution

Contributions are welcome! Feel free to submit a pull request or open an issue to discuss any changes.

## License

This repository is licensed under the MIT License.

### MIT License
MIT License

Copyright (c) 2025 Anjali Hole

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
