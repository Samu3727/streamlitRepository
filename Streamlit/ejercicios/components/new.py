import streamlit as st

conn = st.connection("mi_basededatos")
df = conn.query("select * from my_basededatos")

st.dataframe(df)