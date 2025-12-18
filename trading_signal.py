# trading_signal.py
import yfinance as yf
import pandas as pd

def generate_signal(symbol):
    # 下载1个月的日线数据（包含足够的均线计算周期）
    df = yf.download(symbol, period="1mo", interval="1d", auto_adjust=True)
    if df.empty:
        return "HOLD", {"price": None, "short_ma": None, "long_ma": None, 
                       "support": None, "resistance": None}
    
    # 提取最新收盘价（转为浮点数并保留2位小数）
    latest_close = round(float(df.iloc[-1]["Close"]), 2)
    
    # 计算均线（5日短期/20日长期）
    short_ma = round(float(df["Close"].rolling(window=5).mean().iloc[-1]), 2)  # 5日均线
    long_ma = round(float(df["Close"].rolling(window=20).mean().iloc[-1]), 2)  # 20日均线
    
    # 计算支撑位（近5日最低价区间）
    recent_lows = df["Low"].tail(5)  # 最近5天的最低价
    support_low = round(float(recent_lows.min() * 0.99), 2)  # 支撑下限（-1%）
    support_high = round(float(recent_lows.min() * 1.01), 2)  # 支撑上限（+1%）
    
    # 计算阻力位（近5日最高价区间）
    recent_highs = df["High"].tail(5)  # 最近5天的最高价
    resistance_low = round(float(recent_highs.max() * 0.99), 2)  # 阻力下限（-1%）
    resistance_high = round(float(recent_highs.max() * 1.01), 2)  # 阻力上限（+1%）
    
    # 生成信号（均线交叉策略）
    if short_ma > long_ma:
        signal = "BUY"  # 金叉：短期均线上穿长期均线
    elif short_ma < long_ma:
        signal = "SELL"  # 死叉：短期均线下穿长期均线
    else:
        signal = "HOLD"  # 均线粘合，趋势不明
    
    # 返回信号和市场信息字典
    return signal, {
        "price": latest_close,
        "short_ma": short_ma,
        "long_ma": long_ma,
        "support": (support_low, support_high),
        "resistance": (resistance_low, resistance_high)
    }