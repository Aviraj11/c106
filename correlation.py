import numpy as np
import csv
import plotly_express as px
import pandas as pd
from numpy.lib import corrcoef

def scatter():
    with open ("correlation_data.csv") as f:
        df = pd.read_csv(f)
        fig = px.scatter(df, x = "Days Present", y = "Marks In Percentage")
        fig.show()

def getDataSource(datapath):
    days_spent = []
    marks_percentage = []

    with open (datapath) as f:
        df = csv.DictReader(f)
        for row in df:
            days_spent.append(float(row["Days Present"]))
            marks_percentage.append(float(row["Marks In Percentage"]))
    return{"x":days_spent, "y":marks_percentage}

def findCorrelation(dataSource):
    correlation = np.corrcoef(dataSource["x"],dataSource["y"])
    print("Correlation is -> " , correlation[0,1])

def setUp():
    datapath = "correlation_data.csv"
    dataSource = getDataSource(datapath)
    findCorrelation(dataSource)

setUp()
scatter()