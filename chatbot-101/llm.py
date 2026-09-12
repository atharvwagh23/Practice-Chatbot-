from openai import OpenAI
import os
from dotenv import load_dotenv

# 1. Load environment variables from the .env file
load_dotenv(override=True)

# 2. Get the OpenAI API key from the environment variables
api_key1 = os.getenv("OPENAI_API_KEY")

# 3. Validate that the API key is present
if not api_key1:
    raise ValueError("OPENAI_API_KEY is not set in the environment variables.")

# 4. Initialize the OpenAI client with the API key
client = OpenAI(api_key=api_key1)

# 5. Define a function to generate a response from the OpenAI API
def get_response(messages):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages
    )
    
    return response.choices[0].message.content