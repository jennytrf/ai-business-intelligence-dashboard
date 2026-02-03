from openai import OpenAI

def generate_insights(api_key, summary_text):
    client = OpenAI(api_key=api_key)

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": (
                    "You are a senior business intelligence analyst. "
                    "Analyze the provided KPIs and generate clear, concise, "
                    "executive-level business insights and recommendations."
                )
            },
            {
                "role": "user",
                "content": summary_text
            }
        ]
    )

    return response.choices[0].message.content
