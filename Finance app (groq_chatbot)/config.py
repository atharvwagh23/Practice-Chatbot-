# This file is responsible for initializing and storing application configurations

# Import the os module to interact with the operating system environment variables
import os
# Import load_dotenv to read variables from a local .env file
from dotenv import load_dotenv

# 1. Load environment variables from the .env file into the system environment
load_dotenv(override=True)  # override=True ensures that existing environment variables are overwritten by those in the .env file

# 2. Read the Groq API key from the environment variables
# This assumes you have GROQ_API_KEY=your_key in your .env file
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# (Optional) You can add validation here, e.g., if not GROQ_API_KEY: raise ValueError(...)

# 3. Define the LLM model to be used
# os.getenv() takes a second argument as a fallback default. 
# If "MODEL" isn't in the .env file, it defaults to "openai/gpt-oss-120b"
MODEL = os.getenv("MODEL", "openai/gpt-oss-120b")