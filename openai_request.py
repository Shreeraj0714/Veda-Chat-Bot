import openai
import userPass

openai.api_key = userPass.OpenAIapi_key

completion = openai.ChatCompletion.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {
            "role": "user",
            "content": "Write 2 lines about VEDAS."
        }
    ]
)

print(completion.choices[0].message['content'])