import streamlit as st


#page setup

about_page = st.Page(
    page = 'pages/aboutme.py',
    title='About Me',
    icon='😎',
    default=True
)
chat_bot_page = st.Page(
    page = 'pages/chatbot.py',
    title = "Chat Bot",
    icon='🤖'
)

pg = st.navigation(
    {
        'info':[about_page],
        "app":[chat_bot_page]
    }
)

#visible on all the pages
st.logo(image='corner_logo',link='./asset/logo.png',icon_image='corner_logo')
st.sidebar.text("Made By 😎 Sumit Kumar")
#running navigation
pg.run()