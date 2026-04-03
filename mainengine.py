import streamlit as st
import pandas as pd

def tabMe_arr(tab):
    with tab:
        colA, colB= st.columns([0.5,0.5])
        with colA:
            col1, col2= st.columns([0.6,0.35])
            with col1:
                st.markdown(f"##### :blue[Main Engine Temperatures (deg C)]")
            with col2:
                #st.markdown("Section Status: 🔴🟠🟢⚫️⚪️")
                st.markdown("Status : 🟠") #:red_circle:")
            dfME = pd.read_excel("erlb.xlsx",sheet_name="ME",
                            usecols='B:E', skiprows=range(3), # Skip rows before the start
                            nrows=11 - 3)  # Read only the specified number of rows
            dfME = dfME.fillna("")
            st.data_editor(dfME, disabled=["Temp"],width=400, height="content", hide_index=True)
            col3, col4= st.columns([0.6,0.35])
            with col3:
                st.markdown(f"##### :blue[Turbochargers]")
            with col4:
                #st.markdown("Section Status: 🔴🟠🟢⚫️⚪️")
                st.markdown("Status : 🔴") #:red_circle:")
            dfTurbo = pd.read_excel("erlb.xlsx",sheet_name="mainengine",
                            usecols='P:R', skiprows=range(47), # Skip rows before the start
                            nrows=63 - 47)  # Read only the specified number of rows
            dfTurbo = dfTurbo.fillna("")
            st.data_editor(dfTurbo, disabled=["Turbocharger", "In/Out"],width=400, height="content", hide_index=True)

        with colB:
            col1, col2= st.columns([0.6,0.35])
            with col1:
                st.markdown(f"##### :blue[Main Engine Parameters]")
            with col2:
                st.markdown("Status : 🟠") #:red_circle:")
            dfRunhrs = pd.read_excel("erlb.xlsx",sheet_name="mainengine",
                            usecols='C:D', skiprows=range(6), # Skip rows before the start
                            nrows=20 - 7)  # Read only the specified number of rows
            dfRunhrs = dfRunhrs.fillna("")

            st.data_editor(dfRunhrs, disabled=["Parameter"], width=250, height="content", hide_index=True)


    return