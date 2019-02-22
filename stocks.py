#from nsepy import get_history
#from datetime import date
import pandas as pd
import numpy as np

#from bokeh.io import show
#from bokeh.plotting import figure

infy=pd.read_csv("E:/JOB EXAMS/APPLIED EXAMS/redcarpet/01-01-2015-TO-01-01-2016INFYALLN.csv")
tcs=pd.read_csv("E:/JOB EXAMS/APPLIED EXAMS/redcarpet/01-01-2015-TO-01-01-2016TCSALLN.csv")
nifty_it=pd.read_csv("E:/JOB EXAMS/APPLIED EXAMS/redcarpet/data.csv")
#data = get_history(symbol="INFY", start=date(2015,1,1), end=date(2015,12,31))
print(infy.head())
print("\n")
print(tcs.head())
print("\n")
print(nifty_it.head())
print("\n")

infy["4w"] = np.round(infy["Close Price"].rolling(window = 10, center = False).mean(), 2)
infy["16w"] = np.round(infy["Close Price"].rolling(window = 10, center = False).mean(), 2)
infy["32w"] = np.round(infy["Close Price"].rolling(window = 10, center = False).mean(), 2)
infy["48w"] = np.round(infy["Close Price"].rolling(window = 10, center = False).mean(), 2)
infy["52w"] = np.round(infy["Close Price"].rolling(window = 10, center = False).mean(), 2)

tcs["4w"] = np.round(tcs["Close Price"].rolling(window = 10, center = False).mean(), 2)
tcs["16w"] = np.round(tcs["Close Price"].rolling(window = 10, center = False).mean(), 2)
tcs["32w"] = np.round(tcs["Close Price"].rolling(window = 10, center = False).mean(), 2)
tcs["48w"] = np.round(tcs["Close Price"].rolling(window = 10, center = False).mean(), 2)
tcs["52w"] = np.round(tcs["Close Price"].rolling(window = 10, center = False).mean(), 2)

nifty_it["4w"] = np.round(nifty_it["Close"].rolling(window = 10, center = False).mean(), 2)
nifty_it["16w"] = np.round(nifty_it["Close"].rolling(window = 10, center = False).mean(), 2)
nifty_it["32w"] = np.round(nifty_it["Close"].rolling(window = 10, center = False).mean(), 2)
nifty_it["48w"] = np.round(nifty_it["Close"].rolling(window = 10, center = False).mean(), 2)
nifty_it["52w"] = np.round(nifty_it["Close"].rolling(window = 10, center = False).mean(), 2)

#infy.plot(['2016-01-04':'2016-08-07',:], otherseries = ["4w", "16w", "32w","48w","52w"])
infy_closeprice=[infy["4w"],infy["16w"],infy["32w"],infy["48w"],infy["52w"]]
infy_result=pd.concat(infy_closeprice)
#plot=figure()
#infyDate_list=list(infy['Date'])
#plot.line(infyDate_list,infy_result)
#show(plot)
infy_result.plot(figsize=(10,10) ,linewidth=5)

print("\n")

tcs_closeprice=[tcs["4w"],tcs["16w"],tcs["32w"],tcs["48w"],tcs["52w"]]
tcs_result=pd.concat(tcs_closeprice)
tcs_result.plot(figsize=(10,10) ,linewidth=5)

print("\n")

nifty_it_closeprice=[nifty_it["4w"],nifty_it["16w"],nifty_it["32w"],nifty_it["48w"],nifty_it["52w"]]
nifty_it_result=pd.concat(nifty_it_closeprice)
nifty_it_result.plot(figsize=(10,10) ,linewidth=5)