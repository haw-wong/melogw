import streamlit as st
import pandas as pd

def tabMach_arr(tab):
    with tab:
        col1, col2, col3, col4, col5 = st.columns([0.2,0.3,0.18,0.16,0.16])
        with col1:
            st.selectbox("Watch",["0000:0400","0400-0800","0800-1200"],index=0)
        with col2:
            selected = st.selectbox("Section",["Main Engine","Aux Engine","Boilers"],index=0)
            #st.radio("Section",["Main Engine","Aux Engine","Boiler"], index=0, \
            #                    help="Select the metric group to display : value (9), strength (10), performance (10). Not all metrics are calculated due to difference in \
            #                    terminology used in reporting for different sectors/industry/country. We only download financial statements \
            #                    from yahoo finance at this time. Note : When column \'Current\' only contains \'-\', it means that current \
            #                    values have not been successfully downloaded.", horizontal=True)
        with col3:
            st.markdown(" ")
        with col4:
            #st.markdown("Section Status: 🔴")
            st.markdown("Section Status: 🟢") #:red_circle:")
        with col5:
            st.markdown("Log Book Status: 🔴")
            #st.markdown("Log Book Status: 🟢")
        if selected=="Main Engine":
            dfME = pd.read_excel("erlb.xlsx",sheet_name="mainengine",
                            usecols='X:AP', skiprows=range(24), # Skip rows before the start
                            nrows=32 - 25)  # Read only the specified number of rows
            dfME = dfME.fillna("")
            st.dataframe(dfME, hide_index=True)
        elif selected=="Aux Engine":
            st.markdown(f"### :orange[This section for auxiliary engine.]")
        else:
            st.markdown(f"### :orange[This section for boilers.]")

    return