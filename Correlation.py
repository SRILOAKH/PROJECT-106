import plotly.express as px
import csv
import numpy as np
def plotfig(data_path):
    with open(data_path) as f:
     df=csv.DictReader(f)
     fig=px.scatter(df,x="Marks In Percentage",y="Days Present")
     fig.show()
def getdatasource(data_path):
    days_present=[]
    marks_in_percentage=[]
    with open(data_path) as f:
        csv_reader=csv.DictReader(f)
        for row in csv_reader:
            marks_in_percentage.append(float(row["Marks In Percentage"]))
            days_present.append(float(row["Days Present"]))
    return{"x": marks_in_percentage,"y":days_present}
def findcorrelation(datasource):
    correlation=np.corrcoef(datasource["x"],datasource["y"])
    print(correlation)
def setup():
    data_path="data.csv"
    datasource=getdatasource(data_path)
    findcorrelation(datasource)
    plotfig(data_path)
setup()