import streamlit as st


st.set_page_config(layout='centered')
#page setup
about_page = st.Page(
    page = r"C:\Users\bensu\Desktop\ML Projects\Practice-Project\Portfolio_streamlit\pages\about_me.py",
    title = "About Me",
    icon = "😁",
    default = True
)

sale_dashboard_page = st.Page(
    page = r"C:\Users\bensu\Desktop\ML Projects\Practice-Project\Portfolio_streamlit\pages\sale_dashboard.py",
    title = "Sales Dashboard",
    icon = "💵"
)

chat_bot_page = st.Page(
    page = r"C:\Users\bensu\Desktop\ML Projects\Practice-Project\Portfolio_streamlit\pages\chatbot.py",
    title = "Chat-Bot",
    icon = "🤖"
)

#old and messy way 
# pg = st.navigation(pages = [about_page,sale_dashboard_page,chat_bot_page])
# pg.run()

# creating navigation pane
#new and starightforward
pg = st.navigation(
    {
        "info" : [about_page],
        "Apps" : [sale_dashboard_page,chat_bot_page]
    }
)


#sharing om all the page data
st.logo(r"C:\Users\bensu\Desktop\ML Projects\Practice-Project\Portfolio_streamlit\assets\logo.png")
st.sidebar.text("Made By 👷🏻‍♂️🤖 Sumit Kumar")
#run navifation
pg.run()



# hiding the header, footer and mainmenu use this code below at the time of deployment
hide_st_style = '''
<style>
#mainMenu {visibility :hidden;}
footer{visibility : hidden;}
header{visibility:hidden;}
</style>
'''

st.markdown(hide_st_style,unsafe_allow_html=True)