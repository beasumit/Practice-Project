import streamlit as st


st.set_page_config(layout="wide")
#to print basic message
st.write("Hello World")
#To print the title
st.title("This is For Testing purpose")
#to create and print a header
st.header("This is a streamlit testing Website")
#to create and print markdown or p tag like a HTML p tag. Here Increase in #  symbol will decrease 
# the size of markdown
st.markdown("# Hello")
st.markdown("## Hello")
st.markdown("### Hello")
st.markdown("#### Hello")
st.markdown("##### Hello")
#To create caption which is used in any fill box or text box
st.caption("This is trial based caption")
#to create a box and print the code in a formated way
st.code('''
        import streamlit as st

st.write("Hello World")
st.title("This is For Testing purpose")
st.header("This is a streamlit testing Website")
st.markdown("# Hello")
st.markdown("## Hello")
st.markdown("### Hello")
st.markdown("#### Hello")
st.markdown("##### Hello")

st.caption("This is trial based caption")
        ''')

#create a text input box
user_name = st.text_input("Name",placeholder="Enter Your Name",max_chars=15)
st.write("User Name :",user_name)
#creating date box
import datetime
st.date_input(label = "Date",max_value=datetime.date.today(),format="DD/MM/YYYY")

#creating chat box
user_chat_history = st.chat_input("Chat box: ")
st.write("user Typed: ",user_chat_history)

#text area
st.text_area("Write Message....")

#slider
voting_limit = st.slider(label="Demo Slider",min_value=10,max_value=50,step=5)
st.write("Limit: ",voting_limit)


#radio button
options_val = ["Yes","No","Don't Know"]
Conformation = st.radio("Can Vote: ",options=options_val)
st.write("Response : " , Conformation)

#check box
conferm_val = st.checkbox(label="Can Vote: ")
st.write("Response: ",conferm_val)

#select Box
confirm_val = st.selectbox(label="Can Vote :",options=options_val)

#file upload
file_upload = st.file_uploader("Chose a File : ",type=["CSV","xlsx"])

import pandas as pd

if file_upload:
        #for reading CSV
        if file_upload.name.endswith(".csv"):
                data = pd.read_csv(file_upload)
        elif file_upload.name.endswith(".xlsx"):
                data = pd.read_excel(file_upload)
        
        
        st.write(data)