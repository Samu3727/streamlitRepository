import streamlit as st

def SelectBox(label, options, key=None):
    return st.selectbox(label, options, key=key)