# Start your code here!
import os
from dotenv import load_dotenv
from openai import APIStatusError, OpenAI

load_dotenv()

# Define the model to use
model = os.getenv("GEMINI_MODEL", "gemini-3.5-flash").removeprefix("models/")

# Read the API key from the environment or a local .env file
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise RuntimeError(
        "GEMINI_API_KEY is not set. Add it to a .env file or your environment."
    )

# Define the client
client = OpenAI(
    api_key=api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

# Start coding here
conversation = [
    {"role": "system", "content": """You are a Parision expert, delivering valuable insights into the cities iconic landmarks and hidden treasures.
- Answer in the first sentence, in 2 to 3 short sentences (under 60 words).
- Give accurate, practical facts and one useful tip.
- Give distances in miles.
- If you are unsure of a fact, say so. Never invent facts.
- Answer only Paris travel questions. Politely decline anything else.
- Tone: warm, friendly, and confident, like a local guide. Use plain English."""},
    {"role": "user", "content": "Where is Eiffel Tower?"},
    {"role": "assistant", "content": """Salam, Hope you are doing well. Eiffel Tower is located in Paris which is the capital of France. If you need any type of Tour guide about Paris, feel free to ask"""}
    
]

user_queries = [
    "How far away is the Louvre from the Eiffel Tower (in miles) if you are driving?",
    "Where is the Arc de Triomphe?",
    "What are the must-see artworks at the Louvre Museum?",
]

for q in user_queries:
    print("User: ", q)
    user_dict = {"role": "user", "content": q}
    conversation.append(user_dict)

    try:
        response = client.chat.completions.create(
            model=model,
            temperature=0.0,
            # max_tokens=100,
            messages=conversation,
        )
    except APIStatusError as error:
        print(
            f"API request failed ({error.status_code}): "
            f"{error.message or 'Unknown API error'}"
        )
        break

    answer = response.choices[0].message.content
    assistant_dict = {"role": "assistant", "content": answer}
    conversation.append(assistant_dict)
    print("Assistant: ", answer, "\n")