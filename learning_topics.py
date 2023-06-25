import streamlit as st
from llm_model import chat_with_gpt,gpt_response

def learning_topics():
    st.header("Learning topics")
    st.subheader("Enter required details to personalized learning")

    # Prompt user for a subject
    subject = st.text_input("enter a subject")
    topic=st.text_input("enter a topic")
    complexity = st.radio("Complexity",["Easy","Medium","Hard"])
    if st.button("Generate Curriculum"):
        # Check if subject is provided
        if subject and topic and complexity:
            prompt = f"user enters subject as {subject} and subtopic as {topic} and the level of complexity as {complexity}, by considering all these parameters you have to make the notes simple and understandable manner, you can use bullet points and numbers for better representation"
            curriculum = gpt_response(prompt)
            st.subheader("Learn here")
            st.write(curriculum)
        else:
            st.warning("Please enter necessary fileds for personalized learning.")