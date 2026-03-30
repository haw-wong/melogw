import streamlit as st

def tabMain_arr(tab):
    with tab:
        st.markdown(f"#### :blue[Main page with ship data common to all log modules.]")
        st.markdown(f"##### :yellow[Data on this page can only be edited by administrator.]")
    return