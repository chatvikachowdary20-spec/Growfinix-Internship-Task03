import json
import requests

# Replace with your Hugging Face API Token
API_TOKEN = "YOUR_HUGGINGFACE_API_KEY"

API_URL = "https://api-inference.huggingface.co/models/google/flan-t5-base"

headers = {
    "Authorization": f"Bearer {API_TOKEN}"
}


def analyze_feedback(feedback):
    prompt = f"""
You are an AI customer support assistant.

Analyze the customer feedback below.

Return ONLY valid JSON in this exact format:

{{
  "sentiment": "",
  "urgency": "",
  "summary": ""
}}

Rules:
- Sentiment must be Positive, Negative, or Neutral.
- Urgency must be High, Medium, or Low.
- Summary should be one short sentence describing the main complaint or praise.

Customer Feedback:
{feedback}
"""

    response = requests.post(
        API_URL,
        headers=headers,
        json={"inputs": prompt}
    )

    return response.json()


def main():
    print("=" * 50)
    print(" Semantic Sentiment & Urgency Analyzer ")
    print("=" * 50)

    feedback = input("\nEnter customer feedback:\n\n")

    result = analyze_feedback(feedback)

    print("\nAI Response:\n")

    if isinstance(result, list):
        print(result[0]["generated_text"])
    else:
        print(json.dumps(result, indent=4))


if __name__ == "__main__":
    main()
