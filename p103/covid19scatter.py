import pandas as pd
import plotly.express as px

df=pd.read_csv('/Users/raama/Documents/White hat jr./python/p103/covid19data.csv')
figure=px.scatter(df,x="Date",y="Cases",color="Country",title="Covid 19 Cases Per Date In Countries")
figure.show()