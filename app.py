import streamlit as st
from streamlit_chat import message
# from streamlit_extras.colored_header import colored_header
# from streamlit_extras.add_vertical_space import add_vertical_space
from hugchat import hugchat
from hugchat.login import Login
from llm_model import chat_with_gpt,gpt_response
from decouple import config
from curriculum import curriculum_making
from interview import interview_topic
from learning_topics import learning_topics
from assessment import assessment


st.set_page_config(page_title="HugChat - An LLM-powered Streamlit app")

user_input = None
hf_email = config("hf_email")
hf_pass = config("hf_pass")

def first_page():
    # Sidebar contents
    with st.sidebar:
        st.title('🤗💬 Edufrent')
        st.markdown("skills over certifications")
        st.markdown('''
        ## About
        "Unlock your potential with technology-powered learning!"
        ''')
        
        # Button states
        cur = st.button("Curriculum")
        lrn = st.button("Learning material")
        asm = st.button("Assessment creator")
        inv = st.button("Interview prep")
        for i in range(15):
            st.write('')
        st.write('Made with ❤️ by ')
        st.write(' Gagana')
        st.write(' Siddhanth')
        st.write(' Anil Kumar')



    st.title("Edufrent")
    st.write("Please provide your information.")

    # Execute functions based on button states
    page_option = st.selectbox("Select an option", ('Curriculum creator', 'Learning topics','Assessment Bot','Interview Bot'))

    if page_option == "Curriculum creator":
        curriculum_making()
    if page_option == "Learning topics":
        learning_topics()


# Run the first_page() function
first_page()
