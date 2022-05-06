import plotly.express as px
import csv
with open("data.csv") as f:
    df=csv.DictReader(f)
    fig=px.scatter(df,x="Marks In Percentage",y="Days Present")
    fig.show()