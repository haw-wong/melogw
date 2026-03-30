import pandas as pd
import streamlit as st
import xlwings as xw

def init_page(title, layout, icon):
    st.set_page_config(page_title=title, layout=layout, page_icon=icon)
    #st.write(f'#### :violet[Shipboard Electronic Log Books]')
    st.markdown("""<style>[data-testid="stElementToolbar"] {display: none;}</style>""",unsafe_allow_html=True)

    # Custom CSS to inject
    style = """
    <style>
        .stSelectbox > div {font-size: 14px;}
        .stTabs [data-baseweb="tab-list"] button [data-testid="stMarkdownContainer"] p {
            font-size:1.2rem;}
    </style>
    """
    st.markdown(style, unsafe_allow_html=True)
    return

init_page('Ship Logs','wide',':bulb:')
tabs = ['Main', 'Deck', 'Engine', 'ORB-1','ORB-2','Cargo Record', 'Garbage', 'ODS', 'NoX', 'SoX']
tabMain, tabDk, tabEn, tabOrb1, tabOrb2, tabCargo, tabGarbage, tabODS, tabNox, tabSoX = st.tabs(tabs)
dfShip = pd.read_excel('mydata.xlsx', sheet_name=sheet)

with st.sidebar:
    st.markdown(f"## :orange[Electronic Logs Application]", help="Click radio button to select")
    st.dataframe(dfShip, hide_index=True)

