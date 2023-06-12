import streamlit as st
import pandas as pd
from pathlib import Path
import base64
from streamlit_elements import elements, mui, html
import logging
from binance.um_futures import UMFutures
from binance.lib.utils import config_logging
from datetime import datetime, timezone, timedelta
import math


# ----------------------------------------------------------------
um_futures_client = UMFutures()

btcusdt = um_futures_client.long_short_account_ratio("BTCUSDT","5m")
ethusdt = um_futures_client.long_short_account_ratio("ETHUSDT","5m")
pepeusdt = um_futures_client.long_short_account_ratio("1000PEPEUSDT","5m")
arpausdt = um_futures_client.long_short_account_ratio("ARPAUSDT","5m")
mtlusdt = um_futures_client.long_short_account_ratio("MTLUSDT","5m")

list_timestamp = [btcusdt[x].get("timestamp") for x in range(30)]



# ----------------------------------------------------------------

cryto_symbol = ("BTC / USDT", "ETH / USDT")

funding_ratio = (-0.01, -0.0025, 0.01, 0.0155, 0.0132, 0.009, 0.006, -0.0055, -0.0032), (-0.01, -0.0025, 0.01, 0.0155, 0.0132, 0.009, 0.006, -0.0055, -0.0032)
funding_time = ("20:00","20:05","20:10","20:15","20:20","20:25","20:30","20:35","20:40")

lsratio_data = (1.1, 1.2, 1.5, 2.3, 2.1, 1.9, 2.9, 2.0, 1.12), (1.4, 2.2, 3.5, 4.6, 4.8, 4.2, 3.5, 2.1, 1.05)
ratio_time = ("20:00","20:05","20:10","20:15","20:20","20:25","20:30","20:35","20:40")

graph_lsratio_data = (1.1, 1.2, 1.5, 2.3, 2.1, 1.9, 2.9, 2.0, 1.12)
graph_fr_data = (-0.01, -0.0025, 0.01, 0.0155, 0.0132, 0.009, 0.006, -0.0055, -0.0032)

page = 1 # 0: Home, 1: Binance Cryto Info, 2: Chart


def main(): # main
    cs_sidebar() # 사이드바 실행

    if page == 0 :  # 0
        pass
    elif page == 1 : # 1
        page_1()

    
    return None

#### sidebar ####

def cs_sidebar():       
    st.sidebar.header("**Streamlit cheat sheet**")
    global page
    if st.sidebar.button(":green[**Binance Cryto Info**]", use_container_width=True) :
        page = 1 #  

    if st.sidebar.button(":violet[**Chart**]", use_container_width=True) :
        page = 2 #
    
    return None

# ------------------------Frame------------------------ #
def LongShort_Ratio_Dataframe() : # 롱숏비율 시트화
    col1, col2, col3, col4, col5, col6 = st.columns(6)
    list_timestamp_5m = [btcusdt[x].get("timestamp") for x in range(30)]
    time_UST = pd.to_datetime(list_timestamp_5m, unit="ms")
    time_KST = (time_UST + timedelta(hours=9)).strftime('%H:%M') # strftime('%Y-%m-%d %H:%M:%S')
        
    btc_longShortRatio_5m = [[btcusdt[x].get("longShortRatio") for x in range(30)]]
    eth_longShortRatio_5m = [ethusdt[x].get("longShortRatio") for x in range(30)]
    pepe_longShortRatio_5m = [pepeusdt[x].get("longShortRatio") for x in range(30)]
    arpa_longShortRatio_5m = [arpausdt[x].get("longShortRatio") for x in range(30)]
    mtl_longShortRatio_5m = [mtlusdt[x].get("longShortRatio") for x in range(30)]


    list_longShortRatio_5m = pd.DataFrame(data=btc_longShortRatio_5m, index=["BTCUSDT"], columns=time_KST)
    list_longShortRatio_5m.loc["ETHUSDT"] = eth_longShortRatio_5m
    list_longShortRatio_5m.loc["PEPEUSDT"] = pepe_longShortRatio_5m
    list_longShortRatio_5m.loc["ARPAUSDT"] = arpa_longShortRatio_5m
    list_longShortRatio_5m.loc["MTLUSDT"] = mtl_longShortRatio_5m
    # df = df.T 하면 행렬 바뀜!!
    

    with col1 :
        st.caption(body="Long/Short Ratio", unsafe_allow_html=False, help=None)
        
    with col6 : # period 설정
        lsr_Period = st.selectbox(
        "***Period***",
        ("5m", "15m", "30m", "1h", "2h", "4h", "6h", "12h", "1D")
        )
        
    if lsr_Period == "5m": # 5분일 때, 시트 표시
        # list_longShortRatio_5m22.add(list_longShortRatio_5m22)
              
        st.dataframe(list_longShortRatio_5m, use_container_width=True)
    

def Funding_Rate_Dataframe() : # 펀딩비 시트화
    st.caption(body="Funding Rate", unsafe_allow_html=False, help=None)
    
    funding_df = pd.DataFrame(
        funding_ratio,
        index=cryto_symbol,
        columns=funding_time
    )
    st.dataframe(funding_df, use_container_width=True)


def Each_Graph_Detaframe() : # 그래프 표출 (각각 개별로 선택해야함. 롱숏비율, 펀딩비)
    list_longShortRatio_5m = (btcusdt[x].get("longShortRatio") for x in range(30))
    timeChange = pd.to_datetime(list_timestamp, unit="ms")
    symbol_option = st.selectbox(
    "***Select Cryto Symbol***",
    ('BTC / USDT', 'ETH / USDT')
    )
    
    if symbol_option == "BTC / USDT" :
        st.caption(body="LongShort Ratio", unsafe_allow_html=False, help=None)
        graph_lsratio_df = pd.DataFrame(
            data=list_longShortRatio_5m,
            index=timeChange,
            columns=["BTC / USDT"]
        )
        st.line_chart(graph_lsratio_df, use_container_width=True)

        st.caption(body="Funding Rate", unsafe_allow_html=False, help=None)
        graph_fr_df = pd.DataFrame(
            data=graph_fr_data,
            index=funding_time,
            columns=["BTC / USDT"]
        )
        st.line_chart(graph_fr_df, use_container_width=True)



# ------------------------Pages------------------------ #
def page_1() :
    colu1, colu2 = st.columns(2)
    
    with colu1 : # 왼쪽 위
        st.title(body="Binance_Futures :money_mouth_face:", anchor=False, help=None) # 타이틀
        st.subheader("LongShotrt Ratio / Funding Rate / Each Graph", anchor=False)        
    
    with colu2 : # 오른쪽 위
        
        st.caption(body="BTCUSDT Perpetual", unsafe_allow_html=False, help=None)
        graph_lsratio_df = pd.DataFrame(
            data=graph_lsratio_data,
            index=ratio_time,
            columns=["BTC / USDT"]
        )
        st.line_chart(graph_lsratio_df, use_container_width=True) # 추후 가격 그래프 차트로 바꿔야함
        
    tab1, tab2, tap3 = st.tabs(["**:green[LongShotrt Ratio]**", "**:blue[Funding Rate]**", "**:red[Each Graph]**"])

    with tab1 :
        LongShort_Ratio_Dataframe()

    with tab2 :
        Funding_Rate_Dataframe()

    with tap3 :
        Each_Graph_Detaframe()

def page_2() :

    pass
    


# Run main()

if __name__ == '__main__':
    st.set_page_config(
     page_title="DD_Binance_Data",
     page_icon=":money_mouth_face:",
     layout="wide"
    )
    main()




