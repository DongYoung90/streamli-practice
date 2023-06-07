import streamlit as st
import pandas as pd



# ------------------------Frame------------------------ #
def LongShort_Ratio_Dataframe() : # 롱숏비율 시트화
    col1, col2, col3, col4, col5, col6 = st.columns(6)
    with col1 :
        st.caption(body="Long/Short Ratio", unsafe_allow_html=False, help=None)
        
    with col6 : # period 설정
        lsr_Period = st.selectbox(
        "***Period***",
        ("5m", "15m", "30m", "1h", "2h", "4h", "6h", "12h", "1D")
        )
        
    if lsr_Period == "5m": # 5분일 때, 시트 표시
        longshort_df = pd.DataFrame(
            lsratio_data,
            index=cryto_symbol,
            columns=ratio_time
        )           
        st.dataframe(longshort_df, use_container_width=True)
    

def Funding_Rate_Dataframe() : # 펀딩비 시트화
    st.caption(body="Funding Rate", unsafe_allow_html=False, help=None)
    
    funding_df = pd.DataFrame(
        funding_ratio,
        index=cryto_symbol,
        columns=funding_time
    )
    st.dataframe(funding_df, use_container_width=True)


def Each_Graph_Detaframe() : # 그래프 표출 (각각 개별로 선택해야함. 롱숏비율, 펀딩비)
    symbol_option = st.selectbox(
    "***Select Cryto Symbol***",
    ('BTC / USDT', 'ETH / USDT')
    )
    
    if symbol_option == "BTC / USDT" :
        st.caption(body="LongShort Ratio", unsafe_allow_html=False, help=None)
        graph_lsratio_df = pd.DataFrame(
            data=graph_lsratio_data,
            index=ratio_time,
            columns=["BTC / USDT"]
        )
        st.bar_chart(graph_lsratio_df, use_container_width=True)

        st.caption(body="Funding Rate", unsafe_allow_html=False, help=None)
        graph_fr_df = pd.DataFrame(
            data=graph_fr_data,
            index=funding_time,
            columns=["BTC / USDT"]
        )
        st.line_chart(graph_fr_df, use_container_width=True)



# ------------------------Main------------------------ #
# 데이터
cryto_symbol = ("BTC / USDT", "ETH / USDT")

funding_ratio = (-0.01, -0.0025, 0.01, 0.0155, 0.0132, 0.009, 0.006, -0.0055, -0.0032), (-0.01, -0.0025, 0.01, 0.0155, 0.0132, 0.009, 0.006, -0.0055, -0.0032)
funding_time = ("20:00","20:05","20:10","20:15","20:20","20:25","20:30","20:35","20:40")

lsratio_data = (1.1, 1.2, 1.5, 2.3, 2.1, 1.9, 2.9, 2.0, 1.12), (1.4, 2.2, 3.5, 4.6, 4.8, 4.2, 3.5, 2.1, 1.05)
ratio_time = ("20:00","20:05","20:10","20:15","20:20","20:25","20:30","20:35","20:40")

graph_lsratio_data = (1.1, 1.2, 1.5, 2.3, 2.1, 1.9, 2.9, 2.0, 1.12)
graph_fr_data = (-0.01, -0.0025, 0.01, 0.0155, 0.0132, 0.009, 0.006, -0.0055, -0.0032)

# 시작
st.title(body='Binance_Futures :money_mouth_face:', anchor=False, help=None) # 타이틀
st.subheader("LongShotrt Ratio / Funding Rate / Each Graph", anchor=False)
tab1, tab2, tap3 = st.tabs(["**:green[LongShotrt Ratio]**", "**:blue[Funding Rate]**", "**:red[Each Graph]**"])

with tab1 :
    LongShort_Ratio_Dataframe()

with tab2 :
    Funding_Rate_Dataframe()

with tap3 :
    Each_Graph_Detaframe()

   
