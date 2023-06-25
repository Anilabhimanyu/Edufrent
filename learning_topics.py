import streamlit as st
from llm_model import chat_with_gpt,gpt_response

def learning_topics():
    st.header("Learning topics")
    st.subheader("Enter required details to personalized learning")

    # Prompt user for a subject
    subject = st.text_input("enter a subject")
    topic=st.text_input("enter a topic")
    complexity = st.radio("Complexity",["Easy","Medium","Hard"])
    if st.button("Explore Topic"):
        # Check if subject is provided
        if subject and topic and complexity:
            prompt = f"Act as a guide for student or user,try to give 100% efforts to make personalized learning, because user enters subject choosen as {subject} and within that he choose particular topic as {topic}, now your role is based on their complexity i.e, {complexity}, you have to explaing the topic what user requires with suitable example and real time applications, make the bullet and arrow points for better understanding"
            curriculum = gpt_response(prompt)
            st.subheader("Learn here")
            st.write(curriculum)
        else:
            st.warning("Please enter necessary fileds for personalized learning.")