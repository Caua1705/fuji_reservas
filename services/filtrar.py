import pandas as pd
import streamlit as st
def filtrar_dataframe(df_reservas, data):
    if isinstance(data, str):
        data = pd.to_datetime(data, format="%d/%m/%Y", errors="coerce").date()
    oi=df_reservas.loc[df_reservas["Data"] == data]
    st.write(oi)
    return oi