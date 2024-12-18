import openai
import json

def chat_with_user(user_query, api_key):
    """Use OpenAI GPT API to generate responses."""
    openai.api_key = api_key
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": user_query},
            ]
        )
        return response['choices'][0]['message']['content']
    except Exception as e:
        return f"Error: {e}"

def get_faq_response(query, faq_file='faq_data.json'):
    """Fetch FAQ response for a user query."""
    try:
        with open(faq_file, 'r') as f:
            faqs = json.load(f)
        for category, faq_list in faqs.items():
            for faq in faq_list:
                if query.lower() in faq['question'].lower():
                    return faq['answer']
        return "I’m not sure about that. Please reach out to support."
    except Exception as e:
        return f"Error loading FAQs: {e}"

def get_all_faqs(faq_file='faq_data.json'):
    """Fetch and return all FAQs in a structured format."""
    try:
        with open(faq_file, 'r') as f:
            return json.load(f)
    except Exception as e:
        return f"Error loading FAQs: {e}"
