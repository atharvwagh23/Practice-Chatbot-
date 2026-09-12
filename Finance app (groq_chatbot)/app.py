# Import the Streamlit library for building the web interface
import streamlit as st

# Import our custom function from llm.py to get the chatbot's response
from llm import get_chat_response

# Configure the main settings for the web page (title in the browser tab and the favicon)
st.set_page_config(page_title="Finance chatbot",
                   page_icon=":money_with_wings:")

# Display the main title on the web page
st.title("Finance chatbot app")

# Check if "chat_history" exists in Streamlit's session_state
# session_state preserves variables across page reruns so the chat doesn't delete itself
if "chat_history" not in st.session_state:
    # If it doesn't exist, initialize it as an empty list
    st.session_state.chat_history = []

# Create a header for the sidebar on the left side of the screen
st.sidebar.header("Chat History")

# Extract only the user's questions from the full conversation history to show in the sidebar
# We use a list comprehension to filter out the assistant's replies
user_queries = [
    msg["content"]
    for msg in st.session_state.chat_history
    if msg["role"] == "user"
]

# Check if there are any user questions to display
if user_queries:
    # Loop through the questions and number them using enumerate (starting at 1)
    for i, query in enumerate(user_queries, 1):
        # Write each question into the sidebar
        st.sidebar.write(f"{i}. {query}")
else:
    # If the list is empty, display a placeholder message in the sidebar
    st.sidebar.write("No chat history available")

# Create a text input box on the main page for the user to type their question
user_input = st.text_input("Ask me anything about finances")

# Create a "Send" button. The indented code runs only when the button is clicked.
if st.button("Send"):
    # Validate the input: .strip() removes accidental spaces at the beginning or end
    if user_input.strip() == "":
        # Show a warning if the user submitted an empty string
        st.warning("Please enter a valid query.")
    else:
        # Call our LLM function, passing the new question and the existing chat history
        response = get_chat_response(
            user_input,
            st.session_state.chat_history
        )

        # Append the user's new question to the session state history
        st.session_state.chat_history.append(
            {
                "role": "user",
                "content": user_input
            }
        )

        # Append the AI's generated response to the session state history
        st.session_state.chat_history.append(
            {
                "role": "assistant",
                "content": response
            }
        )

# Display a subheader for the main chat area
st.subheader("Conversation")

# Loop through the entire chat history (both user and assistant messages)
for msg in st.session_state.chat_history:
    # Check who sent the message
    if msg["role"] == "user":
        # Display user messages in bold
        st.write(f"**User:** {msg['content']}")
    else:
        # Display chatbot messages in bold
        st.write(f"**Chatbot:** {msg['content']}")