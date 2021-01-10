import yfinance as yf
import streamlit as st
import pandas as pd
st.write(""" 
# Simple stock Price !!
Shown are the stock **closing** price and **volume** of Google !

""")
tickerSymbol='GOOGL'
tickerData=yf.Ticker(tickerSymbol)
tickerDf=tickerData.history(priod='1d',start='2001-3-21',end='2021-5-31')
st.write("""
## Closing Price
""")
st.line_chart(tickerDf.Close)
st.write("""
## Volume Price
""")
st.line_chart(tickerDf.Volume)