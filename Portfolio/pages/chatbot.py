import streamlit as st
from langchain_groq import ChatGroq

# Initialize the Groq client
llm = ChatGroq(
    temperature=0,
    groq_api_key=st.secrets['groq_api_key'],
    model_name="llama-3.1-70b-versatile"
)

# Streamlit application
def main():
    st.title("Chatbot Application with Custom Text Area")

    # Instructions
    st.write("Welcome to The Chatbot App! Type your message below to get a response.")

    # Input box for user message
    user_input = st.text_input(label="Message Box", placeholder="Write your message here")

    # Chatbot logic
    if st.button("Send"):
        if user_input.strip():
            # Process user input
            with st.spinner("Processing your message..."):
                response = llm.invoke(user_input)

            # Display response with custom background
            st.markdown(f'<div class="custom-text-area">{response.content}</div>', unsafe_allow_html=True)
        else:
            st.warning("Please enter a message before sending!")

# Run the app
main()
