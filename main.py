# main.py
import sys
from datetime import datetime

# 打印运行标志，方便排查
print(f"\n[{datetime.now().strftime('%H:%M:%S')}] Python 脚本开始加载...")

# --- 1. 导入核心模块 ---
try:
    from trading_signal import generate_signal
    from executor import execute_trade
    from explainer import explain
    from config import SYMBOL, QTY
    print("✅ 模块加载成功")
except ImportError as e:
    print(f"❌ 导入失败: 请检查文件名是否拼写正确（特别是 trading_signal.py）。")
    print(f"详细报错信息: {e}")
    sys.exit(1)

def run_agent():
    print(f"\n" + "="*40)
    print(f"🚀 AI 股票助手启动")
    print(f"📅 时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"🎯 目标: {SYMBOL} | 数量: {QTY} 股")
    print("="*40 + "\n")

    # --- STEP 1: 获取信号 ---
    print("📊 [1/3] 正在获取行情并计算信号...")
    try:
        trade_signal, market_info = generate_signal(SYMBOL)
        current_price = market_info.get('price', '未知')
        print(f"   👉 信号结果: 【{trade_signal}】")
        print(f"   👉 当前参考价: {SYMBOL} {current_price} 美元")  # 显示股票代码+价格
    except Exception as e:
        print(f"❌ 信号获取异常: {e}")
        return

    # --- STEP 2: 核心决策逻辑 ---
    if trade_signal == "HOLD":
        print("\n😴 [结束] 当前无操作指令 (HOLD)。")
        return

    # --- STEP 3: AI 策略解释 ---
    print("\n🤖 [2/3] 正在生成分析报告...")
    try:
        reason = explain(trade_signal, SYMBOL, market_info)
        # 修复：先处理换行符替换，再放入f-string（避免反斜杠语法错误）
        formatted_reason = reason.replace('\n', '\n   ')
        print(f"   📝 AI 分析报告:\n   {'-'*30}\n   {formatted_reason}\n   {'-'*30}")
    except Exception as e:
        print(f"⚠️  AI 解释生成失败（不影响交易）: {e}")

    # --- STEP 4: 交易执行 ---
    print(f"\n💸 [3/3] 正在发送 {trade_signal} 订单到 Alpaca 模拟盘...")
    try:
        order = execute_trade(trade_signal, SYMBOL, QTY)
        if order:
            print(f"✅ [下单成功]")
            print(f"   订单 ID: {order.id}")
            print(f"   订单状态: {order.status}")
        else:
            print("❌ [下单失败] 请检查 executor.py 中的 API 配置或账户权限。")
    except Exception as e:
        print(f"❌ 交易执行出错: {e}")

    print(f"\n" + "="*40)
    print(f"🏁 任务执行完毕")
    print("="*40 + "\n")

if __name__ == "__main__":
    run_agent()