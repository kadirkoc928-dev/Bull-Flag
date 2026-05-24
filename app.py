import streamlit as st
import pandas as pd
from scanner import scan_all


# =========================
# TICKERS
# =========================
def get_all_tickers():

    return [
        "AAPL","MSFT","NVDA","TSLA","AMZN","META","GOOGL","AMD","NFLX","PLTR",
        "UBER","CRM","INTC","BABA","BA","COIN","MSTR","GOOG","SPY","QQQ"
    ]


# =========================
# UI
# =========================
st.set_page_config(page_title="Bull Flag Scanner", layout="wide")

st.title("🐂 Bull Flag Scanner (Daily)")

if st.button("Scan Market"):

    tickers = get_all_tickers()

    with st.spinner("Scanning stocks..."):
        results = scan_all(tickers)

    if results:
        df = pd.DataFrame(results)
        df = df.sort_values("Score", ascending=False)

        st.success(f"{len(df)} Bull Flags gefunden")

        st.dataframe(df, use_container_width=True)

    else:
        st.warning("Keine Bull Flags gefunden")
