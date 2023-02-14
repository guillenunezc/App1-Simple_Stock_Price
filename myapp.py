import yfinance as yf
import streamlit as st
import pandas as pd

st.write("""
# Que pasa pajaron!

Muestra el precio de **cierre** y **volumen** de Google!

""")

# Define el simbolo del ticker
tickerSymbol = "GOOGL"

# Obten los datos del ticker
tickerData = yf.Ticker(tickerSymbol)

# Obten el historico de precios de este ticker
tickerDf = tickerData.history(period="1d", start="2010-5-31", end="2023-02-13")
# Los datos que se obtienen son: Open, High, Low, Close, Volume, Dividens, Stock Splits

st.write("""
## Precio de cierre
""")
st.line_chart(tickerDf.Close)

st.write("""## Volumen de acciones""")
st.line_chart(tickerDf.Volume)