import ccxt
import pandas as pd
import pandas_ta as ta

def analyze_market():
    print("--- 🔍 نظام CleanWave Alpha: جاري فحص السوق الآن ---")
    try:
        # الربط بمنصة بينانس
        exchange = ccxt.binance()
        symbol = 'BTC/USDT'
        
        # جلب البيانات (آخر 100 شمعة، فريم 15 دقيقة)
        bars = exchange.fetch_ohlcv(symbol, timeframe='15m', limit=100)
        df = pd.DataFrame(bars, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
        
        # حساب المؤشرات (EMA 8 و EMA 21)
        df['ema_8'] = ta.ema(df['close'], length=8)
        df['ema_21'] = ta.ema(df['close'], length=21)
        
        current_price = df['close'].iloc[-1]
        ema8 = df['ema_8'].iloc[-1]
        ema21 = df['ema_21'].iloc[-1]

        print(f"💰 سعر {symbol} الحالي: {current_price}")
        print(f"📊 مؤشر EMA 8: {round(ema8, 2)} | مؤشر EMA 21: {round(ema21, 2)}")
        
        # منطق الاستراتيجية
        if ema8 > ema21:
            print("🚀 النتيجة: الاتجاه الحالي [صاعد] - إشارة قوة.")
        else:
            print("📉 النتيجة: الاتجاه الحالي [هابط/عرضي] - إشارة حذر.")
            
        print("✅ تم فحص السيولة الذيول بنجاح.")

    except Exception as e:
        print(f"❌ خطأ تقني في التحليل: {e}")

if __name__ == "__main__":
    analyze_market()
