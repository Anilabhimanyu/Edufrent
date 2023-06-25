import streamlit as st
from llm_model import chat_with_gpt,gpt_response

def curriculum_making():
    st.header("Curriculum Generator")
    st.subheader("Enter a subject to generate a curriculum")

    # Prompt user for a subject
    subject = st.text_input("Enter a subject")

    if st.button("Generate Curriculum"):
        # Check if subject is provided
        if subject:
            prompt = f"user enters subject name as {subject}, now you have to make all topics undercomes in that, make sure to give all topics that undercomes, also make sure to give all subtopics that undercomes in that each topic as bullet points if possible can you give best books links for reference"
            curriculum = gpt_response(prompt)
            st.subheader("Curriculum")
            st.write(curriculum)
        else:
            st.warning("Please enter a subject to generate the curriculum.")