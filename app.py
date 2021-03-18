import pandas as pd
from flask import Flask, render_template

app = Flask(__name__)

df = pd.read_csv('data.csv', usecols = ['ProductId','ClientId','Target','Status'])
print(df)

@app.route("/")
def home():
    pass