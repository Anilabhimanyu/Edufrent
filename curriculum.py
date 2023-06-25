import streamlit as st
from llm_model import chat_with_gpt

def curriculum_making():
    st.header("Curriculum Generator")
    st.subheader("Enter a subject to generate a curriculum")

    # Prompt user for a subject
    subject = st.text_input("Enter a subject")

    if st.button("Generate Curriculum"):
        # Check if subject is provided
        if subject:
            prompt = f"user enters the subject name as {subject}, now you have to give the main topics and then you have to mention subtopics of it as a bullet points"
            curriculum = chat_with_gpt(prompt)
            st.subheader("Curriculum")
            st.write(curriculum)
        else:
            st.warning("Please enter a subject to generate the curriculum.")