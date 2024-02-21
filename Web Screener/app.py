from flask import Flask, render_template, request
import yfinance as yf
import json
import os
import pandas as pd
from datetime import datetime, timedelta
from config import sample, filemap, datetime_dict, direction
app = Flask(__name__)
route = "../Database/Tickers"
@app.route('/')
def hello_world():
    pattern = request.args.get("pattern", "1")
    dat = request.args.get("datetime", "1")
    direct = request.args.get("direction", "2")
    data = {}
    with open("../Database/signals.json", "r") as f:
        python_dict = json.load(f)
        day_dict = python_dict[datetime_dict[dat]][direction[direct]]
    if str(pattern) == "0":
        data = day_dict
    for key, val in day_dict.items():
        if str(val) == str(pattern):
            data[key] = pattern
    data = dict(sorted(data.items(), key=lambda item: item[1]))
    # for key, val in day_dict.items():
    #     if str(val) == str(pattern):
    #         data[key] = val
    # print("data: ", data)
        
    return render_template("index.html", patterns=sample, datetime_dict = datetime_dict, stocks=data, direction=direction)
    # if pattern:

    #     datafiles = os.listdir(route)
    #     for filename in datafiles:
    #         df = pd.read_csv(route + "/" + filename)
    #         # print(df.head())
    # return render_template("index.html", patterns=sample, datetime_dict = datetime_dict, stocks=data)

@app.route('/snapshot')
def snapshot():
    return {
        "code": "success",
        "sucess": True,
        "message": "localhost:5000",
        "status": "200"
    }

if __name__ == "__main__":
    app.run(debug=True)
