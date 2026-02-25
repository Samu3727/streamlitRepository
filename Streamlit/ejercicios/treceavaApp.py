import streamlit as st
import pandas as pd
import numpy as np

if st.checkbox('Show DataFrame'):
    
    char_data = pd.DataFrame(
        
        np.random.randn(20, 3),
        columns=['a', 'b', 'c']
    )
    
    char_data