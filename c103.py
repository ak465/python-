import pandas as pd
import plotly.express as px

df=pd.read_csv("data.csv")
fig=px.scatter(df,x="Population",y="Per capita",size="Percentage",size_max=20,color="Country")
fig.show()



df=pd.read_csv("line_chart.csv")
data=px.line(df,x="Year", y="Per capita income", title="Per capita income", color="Country")
data.show()



df=pd.read_csv("data.csv")
data=px.bar(df, x="Country", y="InternetUsers")
data.show()

