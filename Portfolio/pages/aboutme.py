import streamlit as st
from forms.contact import contact_form




@st.dialog("Contact Me")
def show_contact_form():
    contact_form()

#hero column

col1, col2 = st.columns(2, gap='small',vertical_alignment='center')

with col1:
    st.image('image.png',width= 300)
with col2:
    st.title("Sumit Kumar",anchor=False)
    st.write("## Data Scientist")
    if st.button("✉️ Contact Me"):
        show_contact_form()

st.write('\n')
st.subheader("Skills")        
st.write('''Python , MySQL, TensorFlow, scikit-learn, Tableau, Jupyter Notebook, 
         Keras, Pandas, NumPy, Data Visualization, Data Cleaning, Statistical Analysis, 
         Machine Learning, Linear Regression, 
         Logistic Regression, CNNs, Decision Trees, K-NN, NLP, RNN, LSTM, GIT, Neural Network, Excel, Streamlit.
         ''')

