import streamlit as st
from curriculum import curriculum_making
from llm_model import chat_with_gpt

def user_personalization():
    st.title("User Information Form")

    # Ask for user information
    name = st.text_input("Name")
    # age = st.number_input("Age", min_value=0, max_value=150, step=1)
    class_level = st.selectbox("Class", ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"])
    complexity = st.radio("Complexity",["Easy","Medium","Hard"])
    # Display the submitted information
    if st.button("Submit"):
        st.subheader("Submitted Information")
        st.write("Name:", name)
        st.write("Class:", class_level)
        st.write("Complexity:", complexity)
    

# Main function
def main():
    curriculum_making()

if __name__ == "__main__":
    main()
    

# def learning_topics():
#     st.write("Learning Topics")

# def assignments_valuation():
#     st.write("Assignments Valuation")

# def interviews_vivavoce():
#     st.write("Interviews Vivavoce")

# def features():
#     if st.button("Curriculum"):
#         curriculum_making()
#         return
#     if st.button("Learning Topics"):
#         learning_topics()
#         return
#     if st.button("Assignments Valuation"):
#         assignments_valuation()
#         return
#     if st.button("Interviews Vivavoce"):
#         interviews_vivavoce()
#         return

# def main():
#     st.title("Feature Buttons")
#     st.markdown("Click the buttons to view features")

#     features()

# if __name__ == '__main__':
#     main()
