    
import streamlit as st
from llm_model import chat_with_gpt,gpt_response

def assessment():
    st.title("Chatbot Demo")

    # Initialize message history
    message_history = []

    # User input
    user_input = st.text_input("User Input",key="user_input")

    # Chatbot response
    if st.button("Send"):
        message_history.append({"role": "user", "content": user_input})

        # Generate response from chatbot
        response = chat_with_gpt(message_history)

        # Display chatbot response
        st.text_area("Chatbot Response", value=response, height=200)

        # Add user and chatbot responses to message history
        message_history.append({"role": "user", "content": user_input})
        message_history.append({"role": "assistant", "content": response})

        # Clear user input
        st.text_input("User Input", value="",key="user_input_new")
