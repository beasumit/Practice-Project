import streamlit as st

import re
import requests


webhook_url = st.secrets['webhook_url']

def is_valid_email(email):
    #basic regex pattern for email
    email_pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return re.match(email_pattern,email) is not None



def contact_form():
    with st.form("Contact Form"):
        name = st.text_input(label="Name",placeholder="Enter Your Name.")
        email = st.text_input(label = "E-mail",placeholder="Enter Your E-mail.")
        message = st.text_area(label="Message Box",placeholder="Enter your Message Here.")
        submit_button = st.form_submit_button("Submit")
        if submit_button:
            if not webhook_url:
                st.error(
                    "E-mail Service is not setup. Please Try Again Later.",icon='😔'
                )
                st.stop()
            if not name:
                st.error(
                    "Please Provide Your Name.",icon='😯'
                )
                st.stop()
            if not email:
                st.error("Please Enter Your E-mail.",icon="✉️")
                st.stop()
            if not is_valid_email(email):
                st.error("Please Enter a Valid E-mail Address.",icon='📧')
                st.stop()
            if not message:
                st.error("Please Enter Your Message, Dont Leave It Blank.",icon='😇')
                st.stop()
            #prepairing the data payload and sent it to specified website
            data = {"email":email,'name':name,'message':message}
            response = requests.post(webhook_url,json=data)
            
            if response.status_code == 200:
                st.success("Message Successfully Sent !!! 🥳")
            else:
                st.error("Message Not Sent, Check For Error.",icon='🥲')