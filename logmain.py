import pandas as pd
import streamlit as st
import xlwings as xw
import mainengine
import system
import generator

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
tabs = ['ME', 'Generators', 'Systems', 'Aux','Report','Noon Rep', 'Emerg Eqpt']
tabMe, tabGen, tabSys, tabAux, tabRep, tabNrep, tabEmerg = st.tabs(tabs)
dfShip = pd.read_excel('mydata.xlsx', sheet_name="ship")

with st.sidebar:
    st.markdown(f"## :orange[Chief Engineer\'s Log Book]", help="Select system : ")
    st.dataframe(dfShip, hide_index=True)

mainengine.tabMe_arr(tabMe)
generator.tabGen_arr(tabGen)
system.tabSys_arr(tabSys)