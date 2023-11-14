import datetime
import efinance as ef
import matplotlib.pyplot as plt

code = '600519'

date = datetime.date.today().strftime("%Y%m%d")

print(date)
df = ef.stock.get_quote_history(
    stock_codes=code,
    beg=date,
    end=date,
    klt=1,
)

print(df)