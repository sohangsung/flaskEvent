from flask import Flask, request, render_template,redirect, Response
import json
import time
import pandas as pd


df = pd.read_csv('./csv/Sample-Superstore.csv', encoding='cp949',  parse_dates=['Order Date'],)


df2 = pd.DataFrame(df.groupby('Order Date').count()['Row ID'])
df2['매출'] = df.groupby('Order Date').sum()['Sales']
df2.columns = ['구매건수','매출']
df3 = df2.resample('M').sum()

g3 = df3.groupby(pd.Grouper( freq='Y'))
dfs3 = [group for _,group in g3]
# print( df3)

datas = []
for i,sr in df3.iterrows():
    # print(sr['구매건수'], sr['매출'] )
    datas.append({'odate': f'{i.year}-{i.month}', 'cnt': sr['구매건수'], 'sum': sr['매출']})
    # datas.append({'cnt':sr['구매건수'], 'sum':sr['매출'] })

print( datas )