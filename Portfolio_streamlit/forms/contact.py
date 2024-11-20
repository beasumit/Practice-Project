import streamlit as st
import re
import requests as req


webhook_url = st.secrets["webhook_url"]

def is_valid_email(email):
    email_pattern = f"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return re.match(email_pattern,email) is not None



def contact_form():
    with st.form("contact form"):
        name = st.text_input(label="Name",placeholder="Enter Name Here...")
        email = st.text_input(label = 'E-mail',placeholder = "Enter Your E-mail here...")
        message = st.text_area(label="Message",placeholder="Write a Message Here..")
        submit_button = st.form_submit_button("submit")
    if submit_button:
        if not webhook_url:
            st.error(
                "Email service is not set up. Please try again later.",icon="📧"
            )
            st.stop()
        if not name:
            st.error("Please Provide Your Name",icon='😶')
            st.stop()
        if not email:
            st.error("Please Provide Your Email ",icon = '✉️')
            st.stop()
        if not is_valid_email(email):
            st.error("Please Provide Valid Email",icon = '📨')
            st.stop()
        if not message:
            st.error("Please Provide a Message ",icon='💬')
            st.stop()
        
        #prepare the data payload and send it to the specified webhook url
        data = {"email":email,"name":name,"message":message}
        response = req.post(webhook_url,json = data)
        
        if response.status_code == 200:
            st.success("Your Message is Sucsessfully Sent !!! ",icon='🚀')
        else:
            st.error("There was a Error Your message is not sent.",icon = '😔')