import streamlit as st
import pandas as pd

def tabShip_arr(tab):
    with tab:
        st.markdown(f"##### :blue[Ship Information]")
        dfShip = pd.read_excel('mydata.xlsx', sheet_name="ship")
        st.dataframe(dfShip, hide_index=True)
    return