import streamlit as st
from curriculum import curriculum_making
from learning_topics import learning_topics
from assessment import assessment
from interview import interview_topic

def main():
    # Sidebar contents
    with st.sidebar:
        st.title('🤗💬 Edufrent')
        st.markdown("skills over certifications")
        st.markdown('''
        ## About
        "Unlock your potential with technology-powered learning!"
        ''')
        st.write('Made with ❤️ by Gagana, Siddhanth, Anil')

    st.title("Edufrent")
    st.write("Please provide your information.")

    # Buttons for different functions
    button_curriculum = st.button("Curriculum")
    button_learning_topics = st.button("Learning Topics")
    button_assessment = st.button("Assignments Valuation")
    button_interview = st.button("Interviews Viva Voce")

    # Button actions
    if button_curriculum:
        curriculum_making()
    elif button_learning_topics:
        learning_topics()
    elif button_assessment:
        assessment()
    elif button_interview:
        interview_topic()

if __name__ == "__main__":
    main()
