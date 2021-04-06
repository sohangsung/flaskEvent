from flask import Flask, request, render_template,redirect, Response
import json
import time
import pandas as pd

app = Flask(__name__)

def makeData():
    df = pd.read_csv('./csv/Sample-Superstore.csv', encoding='cp949', parse_dates=['Order Date'], )

    df2 = pd.DataFrame(df.groupby('Order Date').count()['Row ID'])
    df2['매출'] = df.groupby('Order Date').sum()['Sales']
    df2.columns = ['구매건수', '매출']
    df3 = df2.resample('M').sum()

    datas = []
    for i, sr in df3.iterrows():
        datas.append({'odate': f'{i.year}-{i.month}', 'cnt': sr['구매건수'], 'sum': sr['매출']})

    return datas


@app.route('/')
def index():
    return '안대안대'

@app.route('/mychart')
def event_stream():
    # dt = [{"name":"test1","age":20}, {"name":"test2","age":30}]
    # dt = [{'name':'shirt', 'pcnt':5},{'name':'cardign', 'pcnt':20},{'name':'chiffon shirt', 'pcnt':36},{'name':'pants', 'pcnt':10},{'name':'heels', 'pcnt':10},{'name':'for ', 'pcnt':20}]
    dt = makeData()
    dt = json.dumps(dt)
    return dt

@app.route('/myform')
def myform():
    return render_template('myform.html')

if __name__ == '__main__':
    app.run(debug=True)
