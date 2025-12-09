import json
# import openai  # Uncomment and configure when you are ready to use the OpenAI API

from src.preprocess import preprocess_data

def generate_insights():
    # Get the summary from the preprocessing step
    data_summary = preprocess_data()

    # This is the prompt we would send to an AI model
    prompt = f"""
You are an AI data analyst.

Based on this data summary, provide:
- 5 key insights
- Any anomalies or unusual patterns
- 3 practical recommendations for a business stakeholder

Data summary:
{json.dumps(data_summary, indent=2)}
"""

    # --- Placeholder for real AI call ---
    # When you are ready to use an LLM (e.g. OpenAI), you can use something like:
    #
    # response = openai.ChatCompletion.create(
    #     model="gpt-4",
    #     messages=[{"role": "user", "content": prompt}]
    # )
    #
    # insights = response["choices"][0]["message"]["content"]
    # return insights
    # ------------------------------------

    # For now, we just return the prompt so we can see what would be sent to the AI
    return prompt

if __name__ == "__main__":
    # Print the prompt that would go to the AI
    print(generate_insights())
