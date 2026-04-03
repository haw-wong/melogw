import streamlit as st
import pandas as pd

def tabShip_arr(tab):
    with tab:
        st.markdown(f"##### :blue[Ship Information]")
        dfShip = pd.read_excel('erlb.xlsx', sheet_name="ship")
        dfShip = dfShip.fillna("")
        st.dataframe(dfShip, hide_index=True, width=500)
    return