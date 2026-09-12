import streamlit as st

from llm import get_response

## 1. page title
st.title("Chat with LLM")

## 2. Inialize session state for messages

if "messages" not in st.session_state:
    st.session_state.messages = []

## 3. Display previous messages

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

## 4. Accept user input

user_input = st.chat_input("Type your message here...")

### 5. If user input is not empty, process it
if user_input:
    # Append user message to session state
    st.session_state.messages.append(
        {"role": "user", "content": user_input}
        )
    
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(user_input)

    # Get response from LLM

    with st.chat_message("assistant"):
        with st.spinner("Generating response..."):
            response = get_response(st.session_state.messages)
            st.markdown(response)
            
        st.write("Response generated successfully.")
        
    
    ## save the assistant response to session state
    st.session_state.messages.append(
        {"role": "assistant", "content": response}
    )