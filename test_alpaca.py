import alpaca_trade_api as tradeapi
import os

print(">>> Script started")

# 初始化API客户端
api = tradeapi.REST(
    os.getenv("APCA_API_KEY_ID"),
    os.getenv("APCA_API_SECRET_KEY"),
    base_url="https://paper-api.alpaca.markets"
)

print(">>> API client created")

# 测试API连接
try:
    account = api.get_account()
    print(">>> API call success")
    print(f"Account status: {account.status}")
    print(f"Cash: {account.cash} USD")
    print(f"Buying power: {account.buying_power} USD")
except Exception as e:
    print(f">>> API call failed: {e}")
    print("请检查API密钥是否正确配置（环境变量）")