import streamlit as st
import pandas as pd
import yfinance as yf
import datetime
import plotly.express as px

st.set_page_config(layout= 'centered')
st.write('''
         # SIMPLE STOCK PRICE APPLICATION
         ## ***PNB***''')
stock_name = ['GOOGL','PNB.NS','SBIN.NS']
tickersymbol = st.selectbox('Select The Stock Name :- ',stock_name)
tickerData = yf.Ticker(tickersymbol)
start_date = st.date_input(label='Select Starting Date',max_value=datetime.date.today(),format='YYYY-MM-DD')
end_date = st.date_input(label='Select End Date',max_value=datetime.date.today(),format='YYYY-MM-DD')
tickerdf = tickerData.history(period='id',start=start_date, end=end_date)


# st.line_chart(tickerdf.Close,color='#58d68d')
# st.line_chart(tickerdf.Volume)


# Close price line chart with hover info
fig_close = px.line(
    tickerdf,
    x=tickerdf.index,
    y='Close',
    title=f"{tickersymbol} Close Prices Over Time",
    labels={"x": "Date", "Close": "Close Price"}
)
fig_close.update_traces(line_color='#58d68d', hovertemplate='Date: %{x}<br>Close Price: %{y}')
st.plotly_chart(fig_close)

# Volume line chart with hover info
fig_volume = px.line(
    tickerdf,
    x=tickerdf.index,
    y='Volume',
    title=f"{tickersymbol} Volume Over Time",
    labels={"x": "Date", "Volume": "Volume"}
)
fig_volume.update_traces(line_color='#ff6347', hovertemplate='Date: %{x}<br>Volume: %{y}')
st.plotly_chart(fig_volume)