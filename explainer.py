# explainer.py
def explain(signal, symbol, market_info):
    """生成交易信号的分析报告"""
    price = market_info.get("price", "未知")
    short_ma = market_info.get("short_ma", "未知")
    long_ma = market_info.get("long_ma", "未知")
    support = market_info.get("support", ("未知", "未知"))
    resistance = market_info.get("resistance", ("未知", "未知"))
    
    if signal == "BUY":
        return (
            f"📈 买入信号分析：\n"
            f"标的：{symbol} | 当前价格：{price} 美元\n"
            f"技术指标：5日均线={short_ma}，20日均线={long_ma}\n"
            f"支撑区间（建议买入价）：{support[0]} - {support[1]} 美元\n"
            f"阻力区间（潜在止盈价）：{resistance[0]} - {resistance[1]} 美元\n\n"
            f"核心逻辑：5日均线上穿20日均线（金叉），短期趋势转强。\n"
            f"操作建议：可在支撑区间内分批买入，若价格跌破支撑下限3%以上建议止损。"
        )
    elif signal == "SELL":
        return (
            f"📉 卖出信号分析：\n"
            f"标的：{symbol} | 当前价格：{price} 美元\n"
            f"技术指标：5日均线={short_ma}，20日均线={long_ma}\n"
            f"支撑区间（潜在回调价）：{support[0]} - {support[1]} 美元\n"
            f"阻力区间（建议卖出价）：{resistance[0]} - {resistance[1]} 美元\n\n"
            f"核心逻辑：5日均线下穿20日均线（死叉），短期趋势转弱。\n"
            f"操作建议：可在阻力区间内分批卖出，若突破阻力上限2%以上可保留部分仓位。"
        )
    else:
        return (
            f"⏸️ 观望信号分析：\n"
            f"标的：{symbol} | 当前价格：{price} 美元\n"
            f"技术指标：5日均线={short_ma}，20日均线={long_ma}\n"
            f"支撑区间：{support[0]} - {support[1]} 美元\n"
            f"阻力区间：{resistance[0]} - {resistance[1]} 美元\n\n"
            f"核心逻辑：短期均线与长期均线粘合，趋势不明确。\n"
            f"操作建议：等待金叉/死叉信号明确后再行动，避免盲目操作。"
        )