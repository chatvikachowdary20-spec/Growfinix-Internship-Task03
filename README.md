# Semantic Sentiment & Urgency Analyzer

This project analyzes customer feedback using the Hugging Face Inference API.

## Features

- Detects sentiment
- Predicts urgency level
- Summarizes the main complaint or praise
- Returns structured JSON

## Technologies

- Python
- Requests
- Hugging Face Inference API
- FLAN-T5 Model

## Installation

```bash
pip install -r requirements.txt
```

## Run

```bash
python app.py
```

## Sample Output

```json
{
  "sentiment":"Negative",
  "urgency":"High",
  "summary":"Internet outage affecting work and needs immediate resolution."
}
```
