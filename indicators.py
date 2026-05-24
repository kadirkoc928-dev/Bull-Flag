import ta

def add_indicators(df):

    df["SMA20"] = ta.trend.sma_indicator(df["Close"], window=20)
    df["RSI"] = ta.momentum.rsi(df["Close"], window=14)
    df["ADX"] = ta.trend.adx(df["High"], df["Low"], df["Close"], window=14)

    df["MACD"] = ta.trend.macd(df["Close"])
    df["MACD_SIGNAL"] = ta.trend.macd_signal(df["Close"])

    df["ATR"] = ta.volatility.average_true_range(
        df["High"], df["Low"], df["Close"], window=14
    )

    df["VOL_SMA"] = df["Volume"].rolling(20).mean()
    df["VOL_RATIO"] = df["Volume"] / df["VOL_SMA"]

    return df
