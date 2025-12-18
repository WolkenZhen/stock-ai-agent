# executor.py
import alpaca_trade_api as tradeapi
import os

# 初始化Alpaca API客户端
api = tradeapi.REST(
    os.getenv("APCA_API_KEY_ID"),
    os.getenv("APCA_API_SECRET_KEY"),
    base_url="https://paper-api.alpaca.markets"  # 模拟盘地址
)

def execute_trade(signal, symbol, qty):
    """执行交易订单（支持买入和卖出）"""
    try:
        if signal == "BUY":
            # 提交市价买入订单
            order = api.submit_order(
                symbol=symbol,
                qty=qty,
                side="buy",
                type="market",
                time_in_force="gtc"  # 取消前有效
            )
            return order
        elif signal == "SELL":
            # 提交市价卖出订单
            order = api.submit_order(
                symbol=symbol,
                qty=qty,
                side="sell",
                type="market",
                time_in_force="gtc"
            )
            return order
        else:
            print(f"⚠️ 不支持的信号类型: {signal}")
            return None
    except Exception as e:
        print(f"交易执行异常: {e}")
        return None