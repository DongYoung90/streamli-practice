import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import time
import random


# ------------------------Frame------------------------ #
def LongShort_Ratio_Dataframe() :    
    st.caption(body="Long/Short Ratio", unsafe_allow_html=False, help=None)
    
    cryto_symbol = ("BTC / USDT", "ETH / USDT")
    lsratio_data = (1.1, 1.2, 1.5, 2.3, 2.1, 1.9, 2.9, 2.0, 1.12), (1.4, 2.2, 3.5, 4.6, 4.8, 4.2, 3.5, 2.1, 1.05)
    ratio_time = ("20:00","20:05","20:10","20:15","20:20","20:25","20:30","20:35","20:40")
       
    longshort_df = pd.DataFrame(
        lsratio_data,
        index=cryto_symbol,
        columns=ratio_time
    )           
    st.dataframe(longshort_df, use_container_width=True)
    

def Funding_Rate_Dataframe() :
    st.caption(body="Funding Rate", unsafe_allow_html=False, help=None)
    
    cryto_symbol = ("BTC / USDT", "ETH / USDT")
    funding_ratio = (-0.01, -0.0025, 0.01, 0.0155, 0.0132, 0.009, 0.006, -0.0055, -0.0032), (-0.01, -0.0025, 0.01, 0.0155, 0.0132, 0.009, 0.006, -0.0055, -0.0032)
    funding_time = ("20:00","20:05","20:10","20:15","20:20","20:25","20:30","20:35","20:40")    
    
    funding_df = pd.DataFrame(
        funding_ratio,
        index=cryto_symbol,
        columns=funding_time
    )
    st.dataframe(funding_df, use_container_width=True)


# ------------------------Main------------------------ #
    # st.empty(main())
with st.sidebar :
    st.title("*Menu*\n:blue[LongShortRatio / FundingRate]")
    chart_button = st.button("**:green[Chart]** (Show all top 30 by volume)",use_container_width=True)
    st.write("")    
    graph_button = st.button("**:green[Graph]** (Choose Cryto after entering)",use_container_width=True)

if chart_button :
    st.title(body='Binance_Futures :money_mouth_face:', anchor=False, help=None) # 타이틀
    st.header("LongShotrtRatio / FundingRate", anchor=False)
    LongShort_Ratio_Dataframe()
    st.write(" ")
    Funding_Rate_Dataframe()

if graph_button :
    pass




# ------------------------실행------------------------ #

   
