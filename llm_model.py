import openai
import streamlit as st
from decouple import config

# Load API key from .env file
api_key = config("OPENAI_API_KEY")

# Set up OpenAI API credentials
openai.api_key = api_key

# Define the function to interact with the ChatGPT model
def chat_with_gpt(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,  
        max_tokens=50,
        temperature=0.7,
        n=1,
        stop=None,
    )
    return response.choices[0].text.strip()

# Main function
