# =========================================================
# IMPORTS
# =========================================================
import os
from dotenv import load_dotenv
from openai import OpenAI, OpenAIError # ADDED OpenAIError for Requirement 5

# =========================================================
# 1. LOAD API KEY
# =========================================================

# Load environment variables, overriding any cached ones in the terminal
load_dotenv(override=True)

# Fetch the API key from the .env file
api_key = os.getenv("OPENAI_API_KEY")

# Safety check: crash the app early if the key is missing
if not api_key:
    raise ValueError("OPENAI_API_KEY is not set.")


# =========================================================
# 2. OPENAI CLIENT
# =========================================================

# Initialize the official OpenAI client using the validated API key
client = OpenAI(api_key=api_key)


# =========================================================
# 3. CHECK IF QUESTION IS ABOUT GENAI (THE ROUTER)
# =========================================================

def is_genai_question(user_input):
    """
    This function asks a small, strict LLM to classify if the question
    is about GenAI. It returns True if YES, False if NO.
    """
    print("====================================")
    print("CLASSIFIER INPUT:", user_input)

    try:
        # Call OpenAI using the correct chat.completions.create syntax
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "user",
                    "content": f"""
Classify the following question.

Return ONLY YES or NO.

YES = the question is directly related to Generative AI,
LLMs, ChatGPT, OpenAI, prompt engineering, RAG, embeddings,
AI agents, fine-tuning, tokens, transformers used in GenAI,
multimodal GenAI, text/image/audio generation, or GenAI applications.

NO = anything unrelated to Generative AI.

Question:
{user_input}
"""
                }
            ],
            temperature=0.0 # Set to 0.0 so the AI is purely analytical, not creative
        )

        # Extract the exact text from the OpenAI response object
        result = response.choices[0].message.content.strip().upper()
        
        # Strip out any random punctuation just in case the AI replies "YES."
        result = result.replace(".", "")

        print("CLASSIFIER RESULT:", result)
        print("====================================")

        # Return True if the result is exactly "YES", otherwise False
        return result == "YES"
        
    except Exception as e:
        # If the classifier fails (e.g., network error), log it and allow it to pass to the main error handler
        print(f"Classifier Error: {e}")
        return True # Default to True so the main get_response block handles the API error gracefully


# =========================================================
# 4. GENERATE GENAI ANSWER (WITH REQUIREMENT 5 ERROR HANDLING)
# =========================================================

def get_response(messages):
    """
    This function takes the full chat history (including the system prompt),
    checks the latest question using the router, and then gets the final answer.
    """
    print("GET_RESPONSE CALLED")

    # Get the latest user message from the end of the messages list
    user_input = messages[-1]["content"]

    print("USER INPUT:", user_input)

    try:
        # -----------------------------------------------------
        # FIRST: CHECK TOPIC USING THE CLASSIFIER
        # -----------------------------------------------------
        
        # If the classifier returns False (Not GenAI), block it immediately
        if not is_genai_question(user_input):
            print("NON-GENAI QUESTION - BLOCKED")
            
            # Return the canned refusal message without calling the main LLM again
            return (
                "Sorry, I can only help with Generative AI topics. "
                "Please ask me a question about GenAI, LLMs, "
                "prompt engineering, RAG, AI agents, or another "
                "GenAI topic."
            )

        # -----------------------------------------------------
        # SECOND: ANSWER THE GENAI QUESTION
        # -----------------------------------------------------
        
        print("GENAI QUESTION - SENDING TO TUTOR")

        # Pass the full conversation history to OpenAI for the final answer
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=messages, 
            temperature=0.5, 
        )

        # Extract and return the final text response
        return response.choices[0].message.content

    # -----------------------------------------------------
    # ERROR HANDLING (Requirement 5)
    # -----------------------------------------------------
    except OpenAIError as e:
        # Handles specific OpenAI errors (bad keys, rate limits, server down)
        print(f"API Error: {e}")
        return "I'm having trouble connecting to OpenAI right now. Please check your API key or try again later."
    except Exception as e:
        # Handles any other unexpected Python errors
        print(f"Unexpected Error: {e}")
        return "An unexpected error occurred. Please try again."