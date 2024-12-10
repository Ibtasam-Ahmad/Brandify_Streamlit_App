from openai import OpenAI
import json

def chat_with_user(user_query, api_key):
    """Use OpenAI GPT API to generate responses."""
    client = OpenAI(api_key=api_key)
    try:
        completion = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": user_query},
            ]
        )
        return completion.choices[0].message.content
    except Exception as e:
        return f"Error: {e}"

def get_faq_response(query, faq_file='faq_data.json'):
    """Fetch FAQ response for a user query."""
    try:
        with open(faq_file, 'r') as f:
            faqs = json.load(f)
        return faqs.get(query, "I’m not sure about that. Please reach out to support.")
    except Exception as e:
        return f"Error loading FAQs: {e}"
