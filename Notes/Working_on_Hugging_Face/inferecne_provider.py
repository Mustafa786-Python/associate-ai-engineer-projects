from huggingface_hub import InferenceCLlient

client = InferenceClient(
provider="together",
api_key=os.environ["HF_TOKEN"],

completion = client.chat.compLletions.create(
    model="deepseek-ai/DeepSeek-V3",
    messages=[
        {
            "role": "user",
            "content": "What is the capital of Belgium?"
        }
    ]

)

print(completion.choices[0].message)