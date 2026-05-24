import numpy as np
import yfinance as yf
from indicators import add_indicators


# =========================
# TICKER FETCH
# =========================
def fetch_data(ticker):
    df = yf.Ticker(ticker).history(period="6mo", interval="1d")
    if df.empty or len(df) < 60:
        return None
    return df


# =========================
# BULL FLAG DETECTION
# =========================
def detect_bull_flag(df):

    close = df["Close"]
    volume = df["Volume"]

    # ---- FLAGPOLE ----
    pole_start = close.iloc[-40]
    pole_end = close.iloc[-20]

    pole_return = (pole_end - pole_start) / pole_start

    if pole_return < 0.10:
        return False, 0

    vol_spike = volume.iloc[-40:-20].mean() > volume.iloc[-60:-40].mean() * 1.3

    # ---- FLAG ----
    flag = close.iloc[-20:]
    slope = np.polyfit(range(len(flag)), flag.values, 1)[0]

    consolidation = abs(slope) < (pole_end * 0.0015)

    vol_down = volume.iloc[-20:].mean() < volume.iloc[-40:-20].mean()

    # ---- BREAKOUT NEAR ----
    resistance = flag.max()
    breakout = close.iloc[-1] >= resistance * 0.98

    score = 0
    if pole_return > 0.15: score += 30
    if vol_spike: score += 20
    if consolidation: score += 20
    if vol_down: score += 15
    if breakout: score += 15

    return score >= 60, score


# =========================
# TRADE SETUP
# =========================
def build_setup(df):

    flag_df = df.iloc[-20:]

    resistance = flag_df["High"].max()
    support = flag_df["Low"].min()

    price = df["Close"].iloc[-1]
    atr = df["ATR"].iloc[-1]

    entry = round(resistance * 1.005, 2)

    sl_structure = support
    sl_atr = price - (atr * 2)

    stop_loss = round(min(sl_structure, sl_atr), 2)

    risk = entry - stop_loss
    if risk <= 0:
        return None

    tp1 = round(entry + risk * 2, 2)
    tp2 = round(entry + risk * 3, 2)

    # Pole projection
    pole_move = df["Close"].iloc[-40:-20].pct_change().sum()
    tp3 = round(entry * (1 + abs(pole_move)), 2)

    return {
        "Entry": entry,
        "StopLoss": stop_loss,
        "TP1": tp1,
        "TP2": tp2,
        "TP3": tp3,
        "Risk": round(risk, 2),
    }


# =========================
# MAIN SCAN
# =========================
def scan_ticker(ticker):

    try:
        df = fetch_data(ticker)
        if df is None:
            return None

        df = add_indicators(df)

        is_flag, flag_score = detect_bull_flag(df)
        if not is_flag:
            return None

        latest = df.iloc[-1]

        if latest["ADX"] < 18:
            return None

        setup = build_setup(df)
        if setup is None:
            return None

        return {
            "Ticker": ticker,
            "Price": round(latest["Close"], 2),
            "Score": flag_score,
            "RSI": round(latest["RSI"], 1),
            "ADX": round(latest["ADX"], 1),
            "VolRatio": round(latest["VOL_RATIO"], 2),
            **setup
        }

    except:
        return None


# =========================
# SCAN ALL
# =========================
def scan_all(tickers):

    results = []

    for t in tickers:
        res = scan_ticker(t)
        if res:
            results.append(res)

    return results
