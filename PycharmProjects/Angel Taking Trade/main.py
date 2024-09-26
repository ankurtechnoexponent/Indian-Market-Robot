# package import statement
from SmartApi import SmartConnect  # or from SmartApi.smartConnect import SmartConnect
import pyotp
from logzero import logger
import pandas as pd
import websocket
import talib as ta
import time
from datetime import datetime
import datetime
import requests
import json
import re
import numpy as np
import time


# note that all ndarrays must be the same length!


STOCK_NAME = "POWERGRID-EQ"
QTY = "50"
TRANSACTION_TYPE = "BUY"
PRICE = "271"
EXCHANGE = "NSE"
ORDER_TYPE = "LIMIT"
PRODUCT_TYPE = "INTRADAY"

FETCH_OLD_DATE_FROM = "2023-09-25 09:00"
FETCH_OLD_DATE_TO = "2024-09-27 09:00"
TIME_FRAME = "ONE_DAY"

api_key = 'lnZlFunT' # Trading API
hapi_key = 'fxfy6i3M' # Historial API
username = 'A63499057'
pwd = '1308'

# Model 1
RSI_model = True
traded_stock = []
PER_TRADE_FUND = 10000
RSI_OVERBOUGHT = 70
RSI_OVERSOLD = 30

# Model 2
EMA_model = False
EMA_Period_1 = 3
EMA_Period_2 = 30

with open('symbol_token2.json', 'r') as file:
    script_list = json.load(file)

def get_token(symbol):
    x = script_list.get(symbol, "Symbol not found")
    return x

#
# def GettingLtpData(script, token, order):
#     LTP = obj.ltpData(EXCHANGE, script, token)
#     ltp = LTP["data"]["ltp"]
#     quantity = int(PER_TRADE_FUND/ltp)
#     orderparams = {
#             "variety": "NORMAL",
#             "tradingsymbol": STOCK_NAME,
#             "symboltoken": get_token(STOCK_NAME),
#             "transactiontype": TRANSACTION_TYPE,
#             "exchange": EXCHANGE,
#             "ordertype": ORDER_TYPE,
#             "producttype": PRODUCT_TYPE,
#             "duration": "DAY",
#             "price": PRICE,
#             "squareoff": "0",
#             "stoploss": "0",
#             "quantity": QTY
#         }
#     orderId = obj.placeOrder(orderparams)
#     print(f"{order} order Place for {script} at : {datetime.datetime.now()} with Order id {orderId}")
#
#
# def main():
#     global obj
#
#     obj = SmartConnect(api_key=api_key)
#     feedToken = obj.getfeedToken()
#     data = obj.generateSession(username,pwd)
#     refreshToken = data["data"]["refreshToken"]
#     jwtToken = data["data"]["jwtToken"]
#
#     orderplacetime = int(9) * 60 + int(15)
#     timenow = (datetime.datetime.now().hour * 60 + datetime.datetime.now().minute)
#     print("Waiting for 9.15 AM, CURRENT TIME:{}".format(datetime.datetime.now()))
#
#     while timenow < orderplacetime:
#         time.sleep(0.2)
#         timenow = (datetime.datetime.now().hour * 60 * datetime.datetime.now().minute)
#     print("Ready for Trading, CURRENT TIME:{}".format(datetime.datetime.now()))
#
#     try:
#         for script, token in script_list.items():
#             historicParam = {
#                         "exchange": EXCHANGE,
#                         "symboltoken": token,
#                         "interval": TIME_FRAME,
#                         "fromdate": FETCH_OLD_DATE_FROM,
#                         "todate": FETCH_OLD_DATE_TO
#                      }
#             hist_data = obj.getCandleData(historicParam)["data"]
#             if hist_data != None:
#                 df = pd.DataFrame(hist_data, coloums=['date', 'open', 'high', 'low', 'close', 'volume'])
#                 df["rsi"] = ta.RSI(df['close'],timeperiod=14).round(2)
#                 df.dropna(inplace=True)
#                 if not df.empty:
#                     rsi_value = df.rsi.values[-1]
#                     if(rsi_value > RSI_OVERBOUGHT) and (script not in traded_stock):
#                         traded_stock.append(script)
#                         # ltp = GettingLtpData(script, token, "SELL")
#                         print(f"{script} SELL THIS TOKEN {token}")
#                     if(rsi_value < RSI_OVERSOLD) and (script not in traded_stock):
#                         traded_stock.append(script)
#                         # ltp = GettingLtpData(script, token, "BUY")
#                         print(f"{script} BUY THIS TOKEN {token}")
#
#     except Exception as e:
#         print("Historic Api Failed: {}".format(e.message))
#
#     try:
#         logout=obj.terminate.Session(username)
#         print("Logout Successfull")
#     except:
#         print("Logout failed: {}".format(e.message))
#
# if(__name__ == '__main__'):
#     main()


# Reading the JSON data from a file
# with open('data.json', 'r') as file:
#     data = json.load(file)

# Creating a new dictionary with symbol as key and token as value
# symbol_token_dict = {item['symbol']: item['token'] for item in data}

# Printing the resulting dictionary
# print(type(symbol_token_dict))

# with open('symbol_token.json', 'w') as file:
#     json.dump(symbol_token_dict,file,indent=4)

# url = 'https://margincalculator.angelbroking.com/OpenAPI_File/files/OpenAPIScripMaster.json'
#
# response = requests.get(url)
#
# if response.status_code == 200:
#     # Save the content as a JSON file
#     print(type(response.text))
#     with open('data.json', 'w') as file:
#         file.write(response.text)
#     print('File downloaded successfully.')
# else:
#     print(f'Failed to download file. Status code: {response.status_code}')
#




# df = pd.read_json('https://margincalculator.angelbroking.com/OpenAPI_File/files/OpenAPIScripMaster.json')
# tokendf = pd.DataFrame.from_dict(df)
# print(type(df))
#
# def get_token(stk):
#     x = tokendf[tokendf.symbol == stk]
#     return (list(x.token))[0]

def get_token(symbol):
    x = script_list.get(symbol, "Symbol not found")
    return x

#
# api_key = 'lnZlFunT'
# username = 'A63499057'
# pwd = '1308'
smartApi = SmartConnect(api_key)
try:
    token = "ZFMBKZVH2DUVPU2JYP5HMLC7KE"
    totp = pyotp.TOTP(token).now()
except Exception as e:
    logger.error("Invalid Token: The provided token is not valid.")
    raise e

correlation_id = "abcde"
data = smartApi.generateSession(username, pwd, totp)

if data['status'] == False:
    logger.error(data)

else:
    # login api call
    # logger.info(f"You Credentials: {data}")
    authToken = data['data']['jwtToken']
    refreshToken = data['data']['refreshToken']
    # fetch the feedtoken
    feedToken = smartApi.getfeedToken()
    # fetch User Profile
    res = smartApi.getProfile(refreshToken)
    smartApi.generateToken(refreshToken)
    res = res['data']['exchanges']

    # place order
    try:
        orderparams = {
            "variety": "NORMAL",
            "tradingsymbol": STOCK_NAME,
            "symboltoken": get_token(STOCK_NAME),
            "transactiontype": TRANSACTION_TYPE,
            "exchange": EXCHANGE,
            "ordertype": ORDER_TYPE,
            "producttype": PRODUCT_TYPE,
            "duration": "DAY",
            "price": PRICE,
            "squareoff": "0",
            "stoploss": "0",
            "quantity": QTY
        }
        # Method 1: Place an order and return the order ID
        # orderid = smartApi.placeOrder(orderparams)
        # logger.info(f"PlaceOrder : {orderid}")
        # Method 2: Place an order and return the full response
        # response = smartApi.placeOrderFullResponse(orderparams)
        # logger.info(f"PlaceOrder : {response}")
    except Exception as e:
        logger.exception(f"Order placement failed: {e}")
    #
    # # gtt rule creation
    # try:
    #     gttCreateParams = {
    #         "tradingsymbol": "SBIN-EQ",
    #         "symboltoken": "3045",
    #         "exchange": "NSE",
    #         "producttype": "MARGIN",
    #         "transactiontype": "BUY",
    #         "price": 100000,
    #         "qty": 10,
    #         "disclosedqty": 10,
    #         "triggerprice": 200000,
    #         "timeperiod": 365
    #     }
    #     rule_id = smartApi.gttCreateRule(gttCreateParams)
    #     logger.info(f"The GTT rule id is: {rule_id}")
    # except Exception as e:
    #     logger.exception(f"GTT Rule creation failed: {e}")
    #
    # # gtt rule list
    # try:
    #     status = ["FORALL"]  # should be a list
    #     page = 1
    #     count = 10
    #     lists = smartApi.gttLists(status, page, count)
    # except Exception as e:
    #     logger.exception(f"GTT Rule List failed: {e}")
    name = STOCK_NAME + TIME_FRAME + FETCH_OLD_DATE_FROM + FETCH_OLD_DATE_TO
    name_sanitized = re.sub(r'[\/:*?"<>| ]', '_', name)
    # Historic api

    try:
        historicParam = {
            "exchange": EXCHANGE,
            "symboltoken": get_token(STOCK_NAME),
            "interval": TIME_FRAME,
            "fromdate": FETCH_OLD_DATE_FROM,
            "todate": FETCH_OLD_DATE_TO
        }
        # print(smartApi.getCandleData(historicParam))
        try:
            hist_data = smartApi.getCandleData(historicParam)["data"]
            time.sleep(2)
        except smartApi.smartExceptions.DataException as e:
            if "Access denied because of exceeding access rate" in str(e):
                print("Rate limit exceeded. Retrying after a delay...")
                time.sleep(60)  # Wait for 1 minute before retrying
            else:
                raise  # Raise the exception if it's a different error

        if hist_data != None:
            if (RSI_model == True):
                df = pd.DataFrame(hist_data, columns=['date', 'open', 'high', 'low', 'close', 'volume'])
                df["rsi"] = ta.RSI(df['close'], timeperiod=14).round(2)
                df.dropna(inplace=True)
                if not df.empty:
                    rsi_value = df.rsi.values[-1]
                    if (rsi_value > RSI_OVERBOUGHT) and (STOCK_NAME not in traded_stock):
                        traded_stock.append(STOCK_NAME)
                        # ltp = GettingLtpData(script, token, "SELL")
                        print(f"{STOCK_NAME} SELL IN {TIME_FRAME} THIS TOKEN {get_token(STOCK_NAME)} BASED ON RSI {rsi_value}")

                    if (rsi_value < RSI_OVERSOLD) and (STOCK_NAME not in traded_stock):
                        traded_stock.append(STOCK_NAME)
                        # ltp = GettingLtpData(script, token, "BUY")
                        print(f"{STOCK_NAME} BUY IN {TIME_FRAME} THIS TOKEN {get_token(STOCK_NAME)} BASED ON RSI {rsi_value}")
                    if (rsi_value < RSI_OVERBOUGHT) and (rsi_value > RSI_OVERSOLD):
                        print(f"{STOCK_NAME} HOLD IN {TIME_FRAME} THIS TOKEN {get_token(STOCK_NAME)} BASED ON RSI {rsi_value}")
                df['Signal'] = 'Hold'
                df.loc[df['rsi'] < RSI_OVERSOLD, 'Signal'] = 'Buy'
                df.loc[df['rsi'] > RSI_OVERBOUGHT, 'Signal'] = 'Sell'
                df.to_csv(f'{name_sanitized}.csv', index=False)
                # print(df)

            if (EMA_model == True):
                dfema = pd.DataFrame(hist_data, columns=['date', 'open', 'high', 'low', 'close', 'volume'])
                dfema["Ema"] = ta.EMA(dfema['close'], timeperiod=3).round(2)
                dfema["Ematwo"] = ta.EMA(dfema['close'], timeperiod=30).round(2)
                dfema.dropna(inplace=True)
                if not dfema.empty:
                    EMA1P = dfema.Ema.values[-1]
                    EMA2P = dfema.Ematwo.values[-1]
                    EMA1PP = dfema.Ema.values[-2]
                    EMA2PP = dfema.Ematwo.values[-2]
                    if (EMA1P < EMA2P) and (STOCK_NAME not in traded_stock):
                        traded_stock.append(STOCK_NAME)
                        # ltp = GettingLtpData(script, token, "SELL")
                        print(f"{STOCK_NAME} SELL THIS TOKEN {get_token(STOCK_NAME)} EMA {EMA1P} EMA {EMA2P}")

                    if (EMA1P > EMA2P) and (STOCK_NAME not in traded_stock):
                        traded_stock.append(STOCK_NAME)
                        # ltp = GettingLtpData(script, token, "BUY")
                        print(f"{STOCK_NAME} BUY THIS TOKEN {get_token(STOCK_NAME)}  EMA {EMA1P} EMA {EMA2P}")
                    if (EMA_model == False):
                        print(f"{STOCK_NAME} HOLD THIS TOKEN {get_token(STOCK_NAME)}  EMA {EMA1P} EMA {EMA2P}")
                dfema['Signal'] = 'Hold'
                for i in range (1, len(dfema)):
                    if dfema.loc[i, 'Ema'] > dfema.loc[i, 'Ematwo'] and dfema.loc[i - 1, 'Ema'] < dfema.loc[i - 1, 'Ematwo']:
                        dfema.loc[i, 'Signal'] = 'Buy'
                    if dfema.loc[i, 'Ema'] < dfema.loc[i, 'Ematwo'] and dfema.loc[i - 1, 'Ema'] > dfema.loc[i - 1, 'Ematwo']:
                        dfema.loc[i, 'Signal'] = 'Sell'
                # dfema.loc[dfema["Ema"] > dfema["Ematwo"], 'Signal'] = 'Buy'
                # dfema.loc[dfema["Ema"] < dfema["Ematwo"], 'Signal'] = 'Sell'
                    dfema.to_csv(f'{name_sanitized}two.csv', index=False)
                    print(dfema)

        else:
                print(hist_data)
        for script, token in script_list.items():
            historicParam = {
                "exchange": EXCHANGE,
                "symboltoken": token,
                "interval": TIME_FRAME,
                "fromdate": FETCH_OLD_DATE_FROM,
                "todate": FETCH_OLD_DATE_TO
            }
            try:
                hist_data = smartApi.getCandleData(historicParam)["data"]
                time.sleep(2)
            except smartApi.smartExceptions.DataException as e:
                if "Access denied because of exceeding access rate" in str(e):
                    print("Rate limit exceeded. Retrying after a delay...")
                    time.sleep(60)  # Wait for 1 minute before retrying
                else:
                    raise  # Raise the exception if it's a different error
            if hist_data != None:
                df = pd.DataFrame(hist_data, columns=['date', 'open', 'high', 'low', 'close', 'volume'])
                df["rsi"] = ta.RSI(df['close'],timeperiod=14).round(2)
                df.dropna(inplace=True)
                if not df.empty:
                    rsi_value = df.rsi.values[-1]
                    if(rsi_value > RSI_OVERBOUGHT) and (script not in traded_stock):
                        traded_stock.append(script)
                        # ltp = GettingLtpData(script, token, "SELL")
                        print(f"{script} SELL THIS TOKEN {get_token(script)} BASED ON RSI {rsi_value}")
                    if(rsi_value < RSI_OVERSOLD) and (script not in traded_stock):
                        traded_stock.append(script)
                        # ltp = GettingLtpData(script, token, "BUY")
                        print(f"{script} BUY THIS TOKEN {get_token(script)} BASED ON RSI {rsi_value}")
                    # if(rsi_value < RSI_OVERBOUGHT) and (rsi_value > RSI_OVERSOLD):
                        # print(f"{script} HOLD THIS TOKEN {get_token(script)} BASED ON RSI {rsi_value}")

            else:
                print(hist_data)

    except Exception as e:
        logger.exception(f"Historic Api failed: {e}")
    # logout
    try:
        logout = smartApi.terminateSession(username)
        logger.info("Logout Successfull")
    except Exception as e:
        logger.exception(f"Logout failed: {e}")