import pandas as pd
import streamlit as st
import mainengine
import systems
import generator
import ship

def init_page(title, layout, icon):
    st.set_page_config(page_title=title, layout=layout, page_icon=icon)
    st.write(f'### :violet[Shipboard Engine Room Log]')
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

init_page('ER Log','wide',':bulb:')
tabs = ['Ship','ME', 'Generators', 'Systems', 'Aux','Report','Noon Rep', 'Emerg Eqpt']
tabShip, tabMe, tabGen, tabSys, tabAux, tabRep, tabNrep, tabEmerg = st.tabs(tabs)


with st.sidebar:
    st.header(f" :blue[Control Panel]")
    st.date_input("Select date ",value='today')
    st.selectbox("Select watch ", ['0000-0400','0400-0800','0800-1200','1200-1600','1600-2000','2000-2400'])
    #st.selectbox("Select section ",["Ship", "ME", "Generators","Systems","Aux","Report","Noon Rep", "Emerg Eqpt"])
    df = pd.DataFrame({
    'Complete': ['Daily Log','For the Watch','For eachsection','ME','Gen','Systems','Aux','Report','Noon Rep','Emerg Eqpt'],
    'Status': ['🟢','🟠',' ','🔴','🟠','🟠','🟠','🟠','🟠','🟠']})
    st.dataframe(df,column_config={
                "Complete": st.column_config.Column(width=None),
                "Status": st.column_config.Column(width=12)
               }, hide_index=True)
    
    #st.markdown("Section Status: 🔴🟠🟢⚫️⚪️")
    
mainengine.tabMe_arr(tabMe)
generator.tabGen_arr(tabGen)
systems.tabSys_arr(tabSys)
ship.tabShip_arr(tabShip)