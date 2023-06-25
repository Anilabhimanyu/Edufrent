import streamlit as st
import openai
from decouple import config

# Set up OpenAI API credentials
openai.api_key = config("OPENAI_API_KEY")

# Function to generate assessment questions
def generate_assessment(subject, topic, complexity):
    prompt = f"Subject: {subject}\nTopic: {topic}\nComplexity: {complexity}"
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=100,
        temperature=0.7,
        n=5,
        stop=None,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0
    )
    questions = [choice.text.strip() for choice in response.choices]
    return questions

# Streamlit app
def interview_topic():
    st.title("interview Bot")
    st.write("Welcome! I am an assessment bot. Please provide the subject, topic, and complexity level to generate assessment questions.")

    # User input form
    with st.form("input_form"):
        subject = st.text_input("Subject:")
        topic = st.text_input("Topic:")
        complexity = st.selectbox("Complexity:", ["Low", "Medium", "High"])
        submit_button = st.form_submit_button("Generate Questions")

    # Generate and display assessment questions
    if submit_button:
        questions = generate_assessment(subject, topic, complexity)
        st.write("Generated Questions:")
        for i, question in enumerate(questions):
            st.write(f"{i + 1}. {question}")


