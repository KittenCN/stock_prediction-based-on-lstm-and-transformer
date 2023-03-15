import os
import tushare as ts
from tqdm import tqdm

pro = ts.pro_api('546dfa0ae0cee993337b8e1d755912059be77d436b49b95e7cf7732d')

def get_stock_list(ts_code=""):
    # get stock list
    df = pro.stock_basic(**{
        "ts_code": ts_code,
        "name": "",
        "exchange": "",
        "market": "",
        "is_hs": "",
        "list_status": "",
        "limit": "",
        "offset": ""
    }, fields=[
        "ts_code"
    ])
    stock_list = df["ts_code"].tolist()
    # print(stock_list)
    return stock_list

def get_stock_data(ts_code=""):
    stock_list = get_stock_list(ts_code)
    pbar = tqdm(total=len(stock_list), leave=False)
    for code in stock_list:
        df = pro.daily(**{
        "ts_code": code,
        "trade_date": "",
        "start_date": "",
        "end_date": "",
        "offset": "",
        "limit": ""
        }, fields=[
            "ts_code",
            "trade_date",
            "open",
            "high",
            "low",
            "close",
            "change",
            "pct_chg",
            "vol",
            "amount",
            "pre_close"
        ])
        df.to_csv("./stock_daily/"+code+".csv", index=False)
        pbar.update(1)
    pbar.close()

if __name__ == "__main__":
    if os.path.exists("./stock_daily") == False:
        os.mkdir("./stock_daily")
    get_stock_data()