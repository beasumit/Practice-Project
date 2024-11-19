import streamlit as st
from forms.contact import contact_form


#contact form
@st.dialog("Contact Me")
def show_contact_form():
    contact_form()



#creating top columns
col1, col2 = st.columns(2,gap='small',vertical_alignment='center')

with col1:
    st.image(r"C:\Users\bensu\Desktop\ML Projects\Practice-Project\Portfolio_streamlit\assets\1 (2) (1).jpg")
with col2:
    st.title("Sumit Kumar",anchor=False)
    st.write(
        "Entry Level Data Scientist"
    )
    if st.button("✉️ Contact Me"):
        show_contact_form()
        
#Projects
st.title("Projects")
st.write("\n")
st.subheader("Distracted Driver Detection Machine Learning Model.",anchor=False)
st.write('''
         
* Developed a machine learning model to detect distracted driving behaviors using computer vision techniques.
* Leveraged deep learning algorithms with image processing to classify driver states accurately.
* Implemented an interactive Jupyter Notebook to demonstrate model training and evaluation results.
* Utilized visualizations to analyze model performance and improve interpretability of distraction factors.
         ''')
st.page_link("https://github.com/beasumit/Project_Work/blob/main/Machine_Learning_projects/Distracted%20Driver%20Detection%20project/driver-distraction-ml-model.ipynb",label='Github',icon='🔗')


#skills
st.title('Skills')
st.write("\n")
st.write('''
         Python , MySQL, TensorFlow, scikit-learn, Tableau, Jupyter Notebook, Keras, Pandas, 
         NumPy, Data Visualization, Data Cleaning, Statistical Analysis, Machine Learning, 
         Linear Regression, Logistic Regression, CNNs, Decision Trees, K-NN, NLP, RNN, LSTM, GIT, 
         Neural Network, Excel, Streamlit.
         ''')
